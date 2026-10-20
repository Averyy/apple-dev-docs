# globalProgress(for:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Returns a progress object that tracks either the uploading or downloading of items from the File Provider extension’s remote storage.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func globalProgress(for kind: Progress.FileOperationKind) -> Progress
```

```objc
- (NSProgress *) globalProgressForKind:(NSProgressFileOperationKind) kind;
```

#### Discussion

The returned progress instance tracks ongoing operations. This method supports two kinds of operations:

- **[`uploading`](../../Foundation/progress/fileoperationkind-swift.struct/uploading.md)**: Uploading items from the local storage to the remote storage.
- **[`downloading`](../../Foundation/progress/fileoperationkind-swift.struct/downloading.md)**: Downloading items from the remote storage to the local storage.

The progress instance has its [`fileOperationKind`](../../Foundation/progress/fileoperationkind-swift.property.md) property set. It also provides the number of items to upload or download, the number of bytes already transferred, and the total number of bytes to transfer. The grand total is reset to `0` when there are no operations left.

If new matching operations begin while the progress instance is running, it adds the new operations to the existing data. By default, when there are no matching operations, the progress has its values set to `1` and its state set to finished.

The system updates the progress instance on the main queue. You must retain the progress item, and observe its changes through key-value observing. For more information, see `Using Key-Value Observing in Swift`.

## Parameters

- `kind`: The kind of operation. This method only accepts two values: [`uploading`](../../Foundation/progress/fileoperationkind-swift.struct/uploading.md) and [`downloading`](../../Foundation/progress/fileoperationkind-swift.struct/downloading.md).

## See Also

### Performing actions
- [class func placeholderURL(for: URL) -> URL](./placeholderurl%28for%29.md)
  Returns a placeholder URL for a given document URL.
- [class func writePlaceholder(at: URL, withMetadata: NSFileProviderItem) throws](./writeplaceholder%28at,withmetadata%29.md)
  Writes a document placeholder with the provided metadata.
- [func register(URLSessionTask, forItemWithIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./register%28_,foritemwithidentifier,completionhandler%29.md)
  Registers the URL session task responsible for the specified item.
- [func signalEnumerator(for: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./signalenumerator%28for,completionhandler%29.md)
  Alerts the system to changes in the specified folder’s content.
- [func waitForChanges(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./waitforchanges%28below,completionhandler%29.md)
  Requests a notification after the system completes all the specified changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/globalprogress(for:))*