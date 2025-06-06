# NSFilePromiseProviderDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that provides the name of the promised file and writes the file to the destination directory when the file promise is fulfilled.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSFilePromiseProviderDelegate : NSObjectProtocol
```

## Topics

### Handling File Promises
- [func filePromiseProvider(NSFilePromiseProvider, fileNameForType: String) -> String](nsfilepromiseproviderdelegate/filepromiseprovider(_:filenamefortype:).md)
  Provides the drag destination file’s name.
- [func filePromiseProvider(NSFilePromiseProvider, writePromiseTo: URL, completionHandler: ((any Error)?) -> Void)](nsfilepromiseproviderdelegate/filepromiseprovider(_:writepromiseto:completionhandler:).md)
  Writes the contents of a promise to the specified URL.
- [func operationQueue(for: NSFilePromiseProvider) -> OperationQueue](nsfilepromiseproviderdelegate/operationqueue(for:).md)
  Returns the operation queue from which to issue the write request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Supporting Drag and Drop Through File Promises](supporting-drag-and-drop-through-file-promises.md)
  Receive and provide file promises to support dragged app files and pasteboard operations.
- [Supporting Table View Drag and Drop Through File Promises](supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [Supporting Collection View Drag and Drop Through File Promises](supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [class NSFilePromiseProvider](nsfilepromiseprovider.md)
  An object that provides a promise for the pasteboard.
- [class NSFilePromiseReceiver](nsfilepromisereceiver.md)
  An object that receives a file promise from the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate)*