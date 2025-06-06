# NSFilePromiseProvider

**Framework**: AppKit  
**Kind**: class

An object that provides a promise for the pasteboard.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class NSFilePromiseProvider
```

#### Overview

A file promise is a possible future file of a specified type.  When you’re working with drag and drop, use promises to indicate intent for future action.  Avoid loading or performing any actions on the file until the promise completes.

Use the [`NSFilePromiseProvider`](nsfilepromiseprovider.md) class when creating file promises. Instantiate one [`NSFilePromiseProvider`](nsfilepromiseprovider.md) for each file promised. Set the [`fileType`](nsfilepromiseprovider/filetype.md) and [`delegate`](nsfilepromiseprovider/delegate.md) properties before writing any [`NSFilePromiseProvider`](nsfilepromiseprovider.md) to the pasteboard. The file type must be a Uniform Type Identifier (UTI) that ultimately conforms to `kUTTypeData` or `kUTTypeDirectory`. The [`NSFilePromiseProviderDelegate`](nsfilepromiseproviderdelegate.md) will write the promised file to the destination directory.

Optionally, you may attach a `userInfo` object of your choosing to the [`NSFilePromiseProvider`](nsfilepromiseprovider.md) to determine which promise is being referenced when promising multiple files under the same [`NSFilePromiseProviderDelegate`](nsfilepromiseproviderdelegate.md) instance.

## Topics

### Initializers
- [init()](nsfilepromiseprovider/init.md)
  Initializes a file promise provider.
- [convenience init(fileType: String, delegate: any NSFilePromiseProviderDelegate)](nsfilepromiseprovider/init(filetype:delegate:).md)
  Initializes a file promise provider for a certain file type.
### Instance Properties
- [var delegate: (any NSFilePromiseProviderDelegate)?](nsfilepromiseprovider/delegate.md)
- [var fileType: String](nsfilepromiseprovider/filetype.md)
  The file type of the file promise provider.
- [var userInfo: Any?](nsfilepromiseprovider/userinfo.md)
  Optional user information to pass to the file promise provider.

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
- [NSPasteboardWriting](nspasteboardwriting.md)

## See Also

- [Supporting Drag and Drop Through File Promises](supporting-drag-and-drop-through-file-promises.md)
  Receive and provide file promises to support dragged app files and pasteboard operations.
- [Supporting Table View Drag and Drop Through File Promises](supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [Supporting Collection View Drag and Drop Through File Promises](supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [protocol NSFilePromiseProviderDelegate](nsfilepromiseproviderdelegate.md)
  A set of methods that provides the name of the promised file and writes the file to the destination directory when the file promise is fulfilled.
- [class NSFilePromiseReceiver](nsfilepromisereceiver.md)
  An object that receives a file promise from the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider)*