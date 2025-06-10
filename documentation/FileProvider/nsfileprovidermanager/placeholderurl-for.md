# placeholderURL(for:)

**Framework**: File Provider  
**Kind**: method

Returns a placeholder URL for a given document URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func placeholderURL(for url: URL) -> URL
```

#### Return Value

A placeholder URL for the given document.

#### Discussion

This method maps file URLs into their corresponding placeholder URLs. You typically call this method to generate the placeholder URL before calling [`writePlaceholder(at:withMetadata:)`](nsfileproviderextension/writeplaceholder(at:withmetadata:).md).

> **Note**:  While this method is available on macOS 11+, you don’t need to use it when creating a file provider extension that adopts the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) protocol.

## Parameters

- `url`: The document URL to be converted.

## See Also

- [class func writePlaceholder(at: URL, withMetadata: NSFileProviderItem) throws](nsfileprovidermanager/writeplaceholder(at:withmetadata:).md)
  Writes a document placeholder with the provided metadata.
- [func register(URLSessionTask, forItemWithIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/register(_:foritemwithidentifier:completionhandler:).md)
  Registers the URL session task responsible for the specified item.
- [func signalEnumerator(for: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/signalenumerator(for:completionhandler:).md)
  Alerts the system to changes in the specified folder’s content.
- [func waitForChanges(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/waitforchanges(below:completionhandler:).md)
  Requests a notification after the system completes all the specified changes.
- [func globalProgress(for: Progress.FileOperationKind) -> Progress](nsfileprovidermanager/globalprogress(for:).md)
  Returns a progress object that tracks either the uploading or downloading of items from the File Provider extension’s remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/placeholderurl(for:))*