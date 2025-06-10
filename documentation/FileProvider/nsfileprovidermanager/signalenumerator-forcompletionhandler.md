# signalEnumerator(for:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Alerts the system to changes in the specified folder’s content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func signalEnumerator(for containerItemIdentifier: NSFileProviderItemIdentifier) async throws
```

## Mentions

- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)
- [Signaling Changes for User-Driven Actions](signaling-changes-for-user-driven-actions.md)
- [Using push notifications to signal changes](using-push-notifications-to-signal-changes.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func signalEnumerator(for containerItemIdentifier: NSFileProviderItemIdentifier) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [class func placeholderURL(for: URL) -> URL](nsfileprovidermanager/placeholderurl(for:).md)
  Returns a placeholder URL for a given document URL.
- [class func writePlaceholder(at: URL, withMetadata: NSFileProviderItem) throws](nsfileprovidermanager/writeplaceholder(at:withmetadata:).md)
  Writes a document placeholder with the provided metadata.
- [func register(URLSessionTask, forItemWithIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/register(_:foritemwithidentifier:completionhandler:).md)
  Registers the URL session task responsible for the specified item.
- [func waitForChanges(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/waitforchanges(below:completionhandler:).md)
  Requests a notification after the system completes all the specified changes.
- [func globalProgress(for: Progress.FileOperationKind) -> Progress](nsfileprovidermanager/globalprogress(for:).md)
  Returns a progress object that tracks either the uploading or downloading of items from the File Provider extension’s remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/signalenumerator(for:completionhandler:))*