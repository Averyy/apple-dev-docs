# NSFilePromiseReceiver

**Framework**: AppKit  
**Kind**: class

An object that receives a file promise from the pasteboard.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class NSFilePromiseReceiver
```

#### Overview

Because [`NSFilePromiseReceiver`](nsfilepromisereceiver.md) implements the [`NSPasteboardReading`](nspasteboardreading.md) protocol, you receive all file promises on the drag pasteboard as follows:

Likewise, you can enumerate dragged items by calling the following:

> **Note**:  A non-item-based drag source may promise multiple files on the same pasteboard item. To be compatible with these drag sources, many [`NSFilePromiseReceiver`](nsfilepromisereceiver.md) methods return an array of values. Multiple-file item-based promises result in one [`NSFilePromiseReceiver`](nsfilepromisereceiver.md) per promised file.

 A non-item-based drag source may promise multiple files on the same pasteboard item. To be compatible with these drag sources, many [`NSFilePromiseReceiver`](nsfilepromisereceiver.md) methods return an array of values. Multiple-file item-based promises result in one [`NSFilePromiseReceiver`](nsfilepromisereceiver.md) per promised file.

## Topics

### Instance Properties
- [var fileNames: [String]](nsfilepromisereceiver/filenames.md)
  An array containing names of the promised files being written to the destination location.
- [var fileTypes: [String]](nsfilepromisereceiver/filetypes.md)
  An array containing types of the promised files being written to the destination location.
### Instance Methods
- [func receivePromisedFiles(atDestination: URL, options: [AnyHashable : Any], operationQueue: OperationQueue, reader: (URL, (any Error)?) -> Void)](nsfilepromisereceiver/receivepromisedfiles(atdestination:options:operationqueue:reader:).md)
  Fulfills the promises at the specified destination.
### Type Properties
- [class var readableDraggedTypes: [String]](nsfilepromisereceiver/readabledraggedtypes.md)
  An array containing dragged file types that are readable.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSPasteboardReading](nspasteboardreading.md)

## See Also

- [Supporting Drag and Drop Through File Promises](supporting-drag-and-drop-through-file-promises.md)
  Receive and provide file promises to support dragged app files and pasteboard operations.
- [Supporting Table View Drag and Drop Through File Promises](supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [Supporting Collection View Drag and Drop Through File Promises](supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [class NSFilePromiseProvider](nsfilepromiseprovider.md)
  An object that provides a promise for the pasteboard.
- [protocol NSFilePromiseProviderDelegate](nsfilepromiseproviderdelegate.md)
  A set of methods that provides the name of the promised file and writes the file to the destination directory when the file promise is fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver)*