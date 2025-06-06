# waitForChanges(below:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Requests a notification after the system completes all the specified changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func waitForChanges(below itemIdentifier: NSFileProviderItemIdentifier) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func waitForChanges(below itemIdentifier: NSFileProviderItemIdentifier) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func waitForChanges(below itemIdentifier: NSFileProviderItemIdentifier) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method waits for all the changes to the item’s descendants to complete before calling the completion handler. If an error occurs during this process, the system immediately passes the error to the completion handler, and you can’t assume all the changes have completed.

> **Note**:  The system doesn’t wait for changes to the item specified by the `itemIdentifier` parameter. It only waits for changes to the item’s children. As a result, you can use this method inside a call to [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:).md).

 The system doesn’t wait for changes to the item specified by the `itemIdentifier` parameter. It only waits for changes to the item’s children. As a result, you can use this method inside a call to [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:).md).

If the `itemIdentifier` property doesn’t refer to a directory, this method immediately calls the completion handler.

## Parameters

- `itemIdentifier`: The item’s identifier.
- `completionHandler`: A block that the system calls after all the changes are complete. The block takes the following parameters:

## See Also

- [class func placeholderURL(for: URL) -> URL](nsfileprovidermanager/placeholderurl(for:).md)
  Returns a placeholder URL for a given document URL.
- [class func writePlaceholder(at: URL, withMetadata: NSFileProviderItem) throws](nsfileprovidermanager/writeplaceholder(at:withmetadata:).md)
  Writes a document placeholder with the provided metadata.
- [func register(URLSessionTask, forItemWithIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/register(_:foritemwithidentifier:completionhandler:).md)
  Registers the URL session task responsible for the specified item.
- [func signalEnumerator(for: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/signalenumerator(for:completionhandler:).md)
  Alerts the system to changes in the specified folder’s content.
- [func globalProgress(for: Progress.FileOperationKind) -> Progress](nsfileprovidermanager/globalprogress(for:).md)
  Returns a progress object that tracks either the uploading or downloading of items from the File Provider extension’s remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/waitforchanges(below:completionhandler:))*