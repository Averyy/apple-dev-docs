# Transferring browsing data to another browser

**Framework**: BrowserKit

Allow people to transfer browsing history, bookmarks, reading lists, and browser extensions to or from your app using a system-provided sheet.

#### Overview

When someone wants to transfer data from your browser to another browser on their device, your app can present a BrowserKit  that walks them through the process. In the sheet, they can choose a destination browser to which to export data. The sheet also supports importing data to your app; the person chooses the source browser from which to import data. In the sheet, the person also selects the type of data they want to transfer, including page visit history, bookmarks, reading list items, and browser extensions.

To display the framework-provided sheet, call [`requestExport(for:token:completionHandler:)`](bebrowserdataexportmanager/requestexport(for:token:completionhandler:).md) when the person requests exporting data from your app, and call [`requestImport(for:completionHandler:)`](bebrowserdataimportmanager/requestimport(for:completionhandler:).md) when the person requests importing data to your app.

If a person uses the sheet in a browser other than your own, the system lists your browser as available when you register for specific launch activities using [`NSUserActivityTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserActivityTypes). Add the data-transfer activity strings (`BEBrowserDataExchangeExportActivity` and `BEBrowserDataExchangeImportActivity`) to your app’s target properties.

When a person chooses your app in the sheet as the source browser for a data export, the system launches your app with the [`BEBrowserDataExportManager`](bebrowserdataexportmanager.md) class’s [`userActivityType`](bebrowserdataexportmanager/useractivitytype-4ar5j.md). When the person chooses your app as the destination browser for a data import, the system launches your app with the [`BEBrowserDataImportManager`](bebrowserdataimportmanager.md) class’s [`userActivityType`](bebrowserdataimportmanager/useractivitytype-35jes.md). Add individual [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) launch handlers to fillful each type of data request.

> ❗ **Important**: To use the browser-to-browser data transfer API, your app needs to meet the criteria. For more information, see [`Preparing your app to be the default web browser`](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser).

#### Initiate a Browsing Data Export

To export data in response to someone’s request in your app, make information available to the transfer sheet. To begin, prepare high-level information about what data is available by configuring an [`BEExportMetadata`](beexportmetadata.md) instance. Also, create a [`BEBrowserDataExportManager`](bebrowserdataexportmanager.md) object and provide it with the window that displays your app’s view hierarchy.

```swift
let browserDataExportManager = BEBrowserDataExportManager(window: self.view.window)
let exportMetadata = BEExportMetadata(
    supportingExportToFiles: false,
    bookmarksCount: self.bookmarksCount,
    readingListCount: self.readingListCount,
    historyCount: self.historyCount,
    extensionsCount: self.extensionsCount
)
```

After creating the export metadata, intiate the export process by calling [`requestExport(for:token:completionHandler:)`](bebrowserdataexportmanager/requestexport(for:token:completionhandler:).md). As arguments to the call, pass the export metadata, `nil` for the token, and a completion handler.

```swift
let exportOptions = try await browserDataExportManager.requestExport(
    for: exportMetadata,
    token: nil
)
// Continue the export using the exportOptions result. 
```

The call triggers the system to present the sheet, which includes the items available for export, as defined by the metadata.

The person chooses a destination browser and items to export, and submits the sheet. The system gives your completion handler a [`BEExportOptions`](beexportoptions.md) instance, which includes the selected data types. The sheet also indicates whether the person wants to export the data to files rather than directly to another installed browser:

- If [`exportToFiles`](beexportoptions/exporttofiles.md) is `true` in the returned options, the person chooses to export to files. In this case, the system cancels the browser-to-browser data exchange and your app exports the browsing data to disk using a file format of your choosing.
- If [`exportToFiles`](beexportoptions/exporttofiles.md) is `false` in the returned options, stream the requested data types to the system by calling [`exportBrowserData(_:)`](bebrowserdataexportmanager/exportbrowserdata(_:).md). The framework handles the transfer automatically as you yield each data item. Create separate tasks for each data type to enable concurrent processing.

The following example demonstrates a request to export bookmark data:

```swift
try await browserDataExportManager.exportBrowserData(AsyncStream<BEBrowserData> { 
    continuation in
    var exportedData: BEExportOptions.DataTypes = []
    // Create a bookmark data export task. 
    if exportOptions.dataTypes.contains(.bookmarks) {
        Task { 
            for await bookmark in self.bookmarks {
                let browserDataBookmark = BEBrowserDataBookmark(
                    isFolder: bookmark.isFolder,
                    title: bookmark.title,
                    identifier: bookmark.id,
                    url: bookmark.url,
                    parentIdentifier: bookmark.parentID
                )
                continuation.yield(browserDataBookmark)
            }
            exportedData.insert(.bookmarks)            
            if exportedData == exportOptions.dataTypes {
                continuation.finish()
            }
        }        
    } 
    // ...
}
```

This call exports data for the types indicated by [`dataTypes`](beexportoptions/datatypes-swift.property.md). After you check whether to export bookmarks, check for other data types, including browsing history, reading list items, and browser extensions, as shown below:

```swift
// Create a browsing history data export task.
if exportOptions.dataTypes.contains(.history) {
    Task { 
        for await visit in self.historyVisits {
            let historyVisit = BEBrowserDataHistoryVisit(
                url: visit.url,
                dateOfLastVisit: visit.date,
                title: visit.title,
                loadedSuccessfully: visit.didLoad,
                httpGet: visit.wasHTTPGet,
                redirectSourceURL: visit.redirectSource,
                redirectSourceDateOfVisit: visit.redirectSourceDate,
                redirectDestinationURL: visit.redirectDestination,
                redirectDestinationDateOfVisit: visit.redirectDestinationDate,
                visitCount: visit.count
            )
            continuation.yield(historyVisit)
        }
        exportedData.insert(.history)
        if exportedData == exportOptions.dataTypes {
            continuation.finish()
        }
    }
}
// Create a reading list data export task. 
if exportOptions.dataTypes.contains(.readingList) {
    Task { 
        for await item in self.readingListItems {
            let readingListItem = BEBrowserDataReadingListItem(
                title: item.title,
                url: item.url,
                dateOfLastVisit: item.lastVisited
            )
            continuation.yield(readingListItem)
        }
        exportedData.insert(.readingList)
        if exportedData == exportOptions.dataTypes {
            continuation.finish()
        }
    }
}
// Create an extensions export task.
if exportOptions.dataTypes.contains(.extensions) {
    Task { 
        for await ext in self.extensions {
            let browserExtension = BEBrowserDataExtension(
                displayName: ext.name,
                developerName: ext.developer,
                identifier: ext.id,
                storeIdentifier: ext.appStoreID
            )
            continuation.yield(browserExtension)
        }
        exportedData.insert(.extensions)
        if exportedData == exportOptions.dataTypes {
            continuation.finish()
        }
    }
} //...
```

#### Initiate a Browsing Data Import

Use the BrowserKit sheet to import data in response to someone’s request in your app’s user interface. Prepare high-level information about the data transfer methods you support by providing a [`BEImportMetadata`](beimportmetadata.md) instance. First create a [`BEBrowserDataImportManager`](bebrowserdataimportmanager.md) object and pass in a reference to your app’s window scene ([`UIWindowScene`](https://developer.apple.com/documentation/UIKit/UIWindowScene)).

```swift
let browserDataImportManager = BEBrowserDataImportManager(scene: scene)
let importMetadata = BEImportMetadata(
    supportForImportFromFiles: false
)
```

After configuring the import metadata, initiate the import process by calling [`requestImport(for:completionHandler:)`](bebrowserdataimportmanager/requestimport(for:completionhandler:).md). Pass the import metadata and your app’s import-submission completion handler.

```swift
let importOptions = try await browserDataImportManager.requestImport(for: importMetadata)
// Continue the import using the importOptions result.
```

The call triggers the system to present the sheet, which displays a list of available browsers to receive the data. The sheet passes your completion handler a [`BEImportOptions`](beimportoptions.md) instance, which indicates whether the person chooses to import data from files rather than directly from another browser:

- If [`importFromFiles`](beimportoptions/importfromfiles.md) is `true`, the person chooses to import from files. In this case, the system doesn’t establish a browser-to-browser data exchange. Prompt the person to select browsing data files from disk using a custom import process of your choosing.
- If [`importFromFiles`](beimportoptions/importfromfiles.md) is `false`, the system launches the source browser with the `BEBrowserDataExchangeExportActivity` activity to export the browser’s data. When the source browser finishes exporting the data, the system launches your app with the `BEBrowserDataExchangeImportActivity` activity to import the data.

#### Indicate Support for and Respond to Data Transfers

The data transfer sheet includes browsers that support transfer requests. To indicate support, use [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) by including the following strings in your app’s [`NSUserActivityTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserActivityTypes) target property:

```xml
<key>NSUserActivityTypes</key>
<array>
    <string>BEBrowserDataExchangeExportActivity</string>
    <string>BEBrowserDataExchangeImportActivity</string>
</array>
```

When someone chooses your app in the sheet as the browser to which they want to import data or from which to export data, the system launches your app with the relevant activity, depending on the transfer type the person chose. In a SwiftUI app, implement [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onContinueUserActivity(_:perform:)) to respond to the activity, including:

- The [`BEBrowserDataImportManager`](bebrowserdataimportmanager.md) class’s [`userActivityType`](bebrowserdataimportmanager/useractivitytype-8xgjo.md) for importing
- The [`BEBrowserDataExportManager`](bebrowserdataexportmanager.md) class’s [`userActivityType`](bebrowserdataexportmanager/useractivitytype-4ar5j.md) for exporting

For example:

```swift
struct AppView: View {
    var body: some View {
        NavigationView { /* Configure views. */ } 
        .onContinueUserActivity(BEBrowserDataExportManager.userActivityType) { userActivity in
            // Respond to the launch request to export data.
```

#### Provide a Required Token to Validate the Transfer

To ensure a one-to-one data transfer between the initiating and responding browsers, the system generates a unique token to track the request. Retrieve the token from the activity’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSUserActivity/userInfo) dictionary and provide it to the system at the time of the data exchange. Pass the  [`importTokenUserInfoKey`](bebrowserdataimportmanager/importtokenuserinfokey-3bqve.md) user info key to indicate an import, and [`exportTokenUserInfoKey`](bebrowserdataexportmanager/exporttokenuserinfokey-1y5l1.md) user info key to indicate an export, as shown below:

```swift
struct AppView: View {
    // Prepare data transfer managers.
    @State private var browserDataImportManager: BEBrowserDataImportManager
    @State private var browserDataExportManager: BEBrowserDataExportManager    
    init(scene: UIWindowScene) {
        _browserDataImportManager = State(
             initialValue: BEBrowserDataImportManager(scene: scene))
        _browserDataExportManager = State(
             initialValue: BEBrowserDataExportManager(scene: scene))
    }
    
    var body: some View {
        NavigationView { 
        .onContinueUserActivity(BEBrowserDataImportManager.userActivityType) { 
            userActivity in
            // Respond to the launch request. 
            guard let token = userActivity.userInfo?[BEBrowserDataImportManager
                .importTokenUserInfoKey] as? UUID else { return }
            Task {
                // Import browser data.
                await handleImportRequest(with: token)
            }           
        }
        .onContinueUserActivity(BEBrowserDataExportManager
            .userActivityType) { userActivity in
            // Respond to the launch request. 
            guard let token = userActivity.userInfo?[BEBrowserDataExportManager
                .exportTokenUserInfoKey] as? UUID else { return }            
            Task {
                // Export browser data.
                await handleExportRequest(with: token)
            }
        }
    }
}
```

#### Receive Imported Data in a Launch Activity

When your app is the data recipient — the destination browser — in all cases, your app receives the actual browsing data within the import launch activity. In your handler, begin receiving the data as a stream by calling [`importBrowserData(token:)`](bebrowserdataimportmanager/importbrowserdata(token:).md). Pass the retrieved token as an argument and process each imported item according to its type:

```swift
/// Called from within the import data launch activity.
func handleImportRequest(with token: UUID) async {
    do {
        for try await browserData in browserDataImportManager.importBrowserData(token: token) {
            switch browserData {
            case let bookmark as BEBrowserDataBookmark:
                await self.importBookmark(bookmark)
            case let historyVisit as BEBrowserDataHistoryVisit:
                await self.importHistoryVisit(historyVisit)
            case let readingListItem as BEBrowserDataReadingListItem:
                await self.importReadingListItem(readingListItem)
            case let extension as BEBrowserDataExtension:
                await self.importExtension(extension)
            default:
                break
            }
        }
    } catch {
        /* Handle import errors. */
    }
}
```

Preserve the folder hierarchy of bookmarks with the [`parentIdentifier`](bebrowserdatabookmark/parentidentifier.md) property. For page visits, maintain the redirects using the redirect-related properties, such as [`redirectSourceURL`](bebrowserdatahistoryvisit/redirectsourceurl.md). For extensions, consider prompting the person to install equivalent extensions from the App Store using the [`storeIdentifier`](bebrowserdataextension/storeidentifier.md) property.

```swift
/// Import a bookmark on behalf of the request.
func importBookmark(_ bookmark: BEBrowserDataBookmark) async {    
    if bookmark.isFolder {
        await bookmarkStore.createFolder(
            id: bookmark.identifier,
            title: bookmark.title,
            parentID: bookmark.parentIdentifier
        )
    } else {
        await bookmarkStore.createBookmark(
            id: bookmark.identifier,
            title: bookmark.title,
            url: bookmark.url,
            parentID: bookmark.parentIdentifier
        )
    }
}
/// Import page visit history.
func importHistoryVisit(_ visit: BEBrowserDataHistoryVisit) async {    
    await historyStore.addVisit(
        url: visit.url,
        title: visit.title,
        date: visit.dateOfLastVisit,
        visitCount: visit.visitCount,
        loadedSuccessfully: visit.loadedSuccessfully
    )
}
/// Add items to the person's reading list.
func importReadingListItem(_ item: BEBrowserDataReadingListItem) async {
    await readingListStore.addItem(
        title: item.title,
        url: item.url,
        dateAdded: item.dateOfLastVisit
    )
}
/// Prompt the person to install an imported browser extension.
func importExtension(_ extension: BEBrowserDataExtension) async {     
    if let storeID = extension.storeIdentifier {
        await extensionStore.suggestInstallation(
            name: extension.displayName,
            developer: extension.developerName,
            appStoreID: storeID
        )
    }
}
```

#### Export Data in a Launch Activity

When someone initiates an import of browsing data from a browser into your browser, the system launches your browser with the `BEBrowserDataExchangeExportActivity` activity (the [`BEBrowserDataExportManager`](bebrowserdataexportmanager.md) class’s [`userActivityType`](bebrowserdataexportmanager/useractivitytype-4ar5j.md)). In your activity handler, raise the data transfer sheet to allow the person to select the types of data to export. Then, you export the data by calling [`exportBrowserData(_:)`](bebrowserdataexportmanager/exportbrowserdata(_:).md) in the same way as when your app initiates an export.

```swift
func handleExportRequest(with token: UUID) async {
    do {
        // Raise the sheet to enable a person to configure the export.
        let exportOptions = try await browserDataExportManager.requestExport(
            for: exportMetadata,
            token: token
        )
        
        // Export the data according to the person's selected exportOptions.dataTypes.
        try await browserDataExportManager.exportBrowserData(
            AsyncStream<BEBrowserData> { continuation in
                // Export browsing data.
            }
        )
    } catch {
        /* Handle errors. */
    }
}
```

After your app streams the data, the system relaunches the browser that requested the import using the `BEBrowserDataExchangeImportActivity` (the [`BEBrowserDataImportManager`](bebrowserdataimportmanager.md) class’s [`userActivityType`](bebrowserdataimportmanager/useractivitytype-35jes.md)).

> ❗ **Important**:  The system relaunches the browser that initiates an import using the `BEBrowserDataExchangeImportActivity`, regardless of whether the inititiating browser is currently running.

## See Also

- [class BEAvailability](beavailability.md)
  A class that tests whether a device is eligible to run an alternative browser engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/transferring-browsing-data-to-another-browser)*