# Downloading files in a web browser with an alternative browser engine

**Framework**: BrowserEngineKit

Report download progress to the system to keep your networking extension active.

#### Overview

Maintaining a long-running network connection to download a large file requires your browser app’s networking extension to remain active in the background for a long period of time. Register your browser’s downloads with the system and report progress so that the system keeps your networking extension active. When the download completes, the system can optionally move the downloaded file to the person’s Downloads folder.

##### Create a Download Progress Access Token

In your browser app, when someone starts a download, create a URL bookmark for the URL that represents the destination for the download, and an access token for the download progress API:

```swift
let destinationURL = URL(...)
let destinationData = try destinationURL.bookmarkData()
let tokenData = DownloadMonitor.createAccessToken()
```

Pass both the bookmark data and access token to your networking extension. For information about using XPC to communicate between a browser app and its extensions, see [`Using XPC to communicate with browser extensions`](using-xpc-to-communicate-with-browser-extensions.md).

##### Register Download Progress with the System

In your networking extension, receive the bookmark data and resolve the download’s destination URL. Initialize a [`BEDownloadMonitor`](bedownloadmonitor-9bwls.md) object with the download source URL, destination URL, access token, and a [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) object that you use to report the download’s progress to the system:

```swift
let destinationURL = try! URL(resolvingBookmarkData: destinationData)
let progress = Progress()
let downloadMonitor = BEDownloadMonitor(sourceURL: sourceURL, destinationURL: destinationURL, observedProgress: progress, liveActivityAccessToken: tokenData)
```

##### Request That the System Move the File to the Persons Downloads Folder

If the system should create a placeholder file in the person’s Downloads folder that shows the state of the download, call the download monitor’s [`useDownloadsFolder(placeholderType:finalFileCreatedHandler:)`](bedownloadmonitor-9bwls/usedownloadsfolder(placeholdertype:finalfilecreatedhandler:).md) method. Use the completion handler to receive the location to which the system moves the completed downloads, as both a URL and bookmark data:

```swift
downloadMonitor.useDownloadsFolder() { finalLocation in
    // Send the final location's URL and bookmark back to the browser app.
}
```

The bookmark you get in the completion handler isn’t suitable for storing to resolve later, if you need to do this then create your own bookmark with security scope. For more information, see [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](https://developer.apple.com/documentation/Foundation/NSURL/bookmarkData(options:includingResourceValuesForKeys:relativeTo:)).

##### Download the File and Report Progress to the System

When your network extension is ready to commence the download, call [`beginMonitoring()`](bedownloadmonitor-9bwls/beginmonitoring().md). If you requested that the system use the person’s Downloads folder, this method returns the placeholder location that the system creates to host the downloaded content, as both a URL and bookmark data. Make a network connection to download the content, for example using the [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system), store data in the file at the download’s destination URL, and update the `Progress` object that you passed to the `BEDownloadMonitor`:

```swift
var downloadCompletedWithoutError = false
let placeholderURLWithBookmark = try await downloadMonitor.beginMonitoring()

// Send the placeholder URL and bookmark back to the browser app.

// Download the file using networking APIs, and
// update progress.completedUnitCount as you write content to disk.

if (downloadCompletedWithoutError) {
    // Indicate to the system that the download is complete.
    progress.completedUnitCount = progress.totalUnitCount
} else {
    // Indicate to the system that the download is canceled.
    progress.cancel()
}
```

When you indicate that the progress is complete, if you asked the system to create a placeholder file in the person’s Downloads folder, the system calls the completion handler you passed to [`useDownloadsFolder(placeholderType:finalFileCreatedHandler:)`](bedownloadmonitor-9bwls/usedownloadsfolder(placeholdertype:finalfilecreatedhandler:).md) to inform your browser of the downloaded file’s location in the Downloads folder. If you don’t tell the system to use the Downloads folder, [`beginMonitoring()`](bedownloadmonitor-9bwls/beginmonitoring().md) returns `nil`. You still download the file to a location in your app’s container using networking APIs, but the system doesn’t show a placeholder in the Downloads folder.

## See Also

- [class BEDownloadMonitor](bedownloadmonitor-9bwls.md)
  An object that reports the status of web downloads to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/downloading-files-in-a-web-browser)*