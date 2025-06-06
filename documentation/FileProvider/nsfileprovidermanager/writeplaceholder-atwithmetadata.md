# writePlaceholder(at:withMetadata:)

**Framework**: Fileprovider  
**Kind**: method

Writes a document placeholder with the provided metadata.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func writePlaceholder(at placeholderURL: URL, withMetadata metadata: NSFileProviderItem) throws
```

#### Discussion

Call this method whenever you need to create a placeholder for a document. The metadata that you provide sets the data provided to the user in the browser interface.

> **Note**:  While this method is available on macOS 11+, you don’t need to use it when creating a file provider extension that adopts the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) protocol.

## Parameters

- `placeholderURL`: The placeholder URL for the document. You can generate a placeholder URL from a document URL by calling  .
- `metadata`: The metadata for this document.

## See Also

- [class func placeholderURL(for: URL) -> URL](nsfileprovidermanager/placeholderurl(for:).md)
  Returns a placeholder URL for a given document URL.
- [func register(URLSessionTask, forItemWithIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/register(_:foritemwithidentifier:completionhandler:).md)
  Registers the URL session task responsible for the specified item.
- [func signalEnumerator(for: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/signalenumerator(for:completionhandler:).md)
  Alerts the system to changes in the specified folder’s content.
- [func waitForChanges(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/waitforchanges(below:completionhandler:).md)
  Requests a notification after the system completes all the specified changes.
- [func globalProgress(for: Progress.FileOperationKind) -> Progress](nsfileprovidermanager/globalprogress(for:).md)
  Returns a progress object that tracks either the uploading or downloading of items from the File Provider extension’s remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/writeplaceholder(at:withmetadata:))*