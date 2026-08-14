# BrowserKit

**Framework**: BrowserKit  
**Kind**: module

Transfer browser data to another browser or check a device’s eligibility to use an alternative browser engine.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

#### Overview

Use the BrowserKit framework to transfer data such as browsing history, bookmarks, and browser extensions from one browser to another, and to test whether a device is eligible to implement an alternative browser engine.

#### Test Eligibility to Use Alternative Browser Engines

To test if a device supports alternative browser engines, call [`isEligible(for:completionHandler:)`](beavailability/iseligible(for:completionhandler:).md) in a browser app that you develop with WebKit:

```swift
do {
  guard await BEAvailability.isEligible(for: .webBrowser) else { return } 
...  
```

If the device supports alternative browser engines, you can offer the person a download link to an alternative distribution of your app that uses the alternative browser engine. For more information about alternative distribution, see [`Distributing your app on an alternative app marketplace`](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-on-an-alternative-marketplace). For more information about developing or embedding alternative browser engines, see [`BrowserEngineKit`](https://developer.apple.com/documentation/browserenginekit).

## Topics

### Essentials
- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)
  Allow people to transfer browsing history, bookmarks, reading lists, and browser extensions to or from your app using a system-provided sheet.
- [class BEAvailability](beavailability.md)
  A class that tests whether a device is eligible to run an alternative browser engine.
### Data export management
- [class BEBrowserDataExportManager](bebrowserdataexportmanager.md)
  A class that handles exporting browsing data to other browsers.
- [class BEExportOptions](beexportoptions.md)
  Options that identify data to export.
- [class BEExportMetadata](beexportmetadata.md)
  Metadata that describes available browser data for export.
### Data import management
- [class BEBrowserDataImportManager](bebrowserdataimportmanager.md)
  A class that handles importing browsing data from other browsers.
- [class BEImportMetadata](beimportmetadata.md)
  Metadata that describes import capabilities for browser data transfers.
- [class BEImportOptions](beimportoptions.md)
  Options for importing browsing data.
### Browser data
- [class BEBrowserDataHistoryVisit](bebrowserdatahistoryvisit.md)
  A class that transfers page visit history between browsers.
- [class BEBrowserDataBookmark](bebrowserdatabookmark.md)
  A class that transfers bookmark information between browsers.
- [class BEBrowserDataReadingListItem](bebrowserdatareadinglistitem.md)
  A class that transfers reading list data between browsers.
- [class BEBrowserDataExtension](bebrowserdataextension.md)
  A class that transfers browser extension information between browsers.
- [class BEBrowserData](bebrowserdata.md)
  A representation of browsing data from a source browser app.
### Errors
- [struct BEBrowserDataExchangeError](bebrowserdataexchangeerror-swift.struct.md)
  An error that occurs during browser data import or export operations.
- [let BEBrowserDataExchangeErrorDomain: String](bebrowserdataexchangeerrordomain.md)
  A constant that identifies the error domain for browser data exchange errors.
### Classes
- [class BEBrowserContentFilter](bebrowsercontentfilter.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/BrowserKit)*