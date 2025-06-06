# FileManagerDelegate

**Framework**: Foundation  
**Kind**: protocol

The interface a file manager’s delegate uses to intervene during operations or if an error occurs.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol FileManagerDelegate : NSObjectProtocol
```

#### Overview

The [`FileManagerDelegate`](filemanagerdelegate.md) protocol defines optional methods for managing operations involving the copying, moving, linking, or removal of files and directories. When you use an [`FileManager`](filemanager.md) object to initiate a copy, move, link, or remove operation, the file manager asks its delegate whether the operation should begin at all and whether it should proceed when an error occurs.

The methods of this protocol accept either [`NSURL`](nsurl.md) or [`NSString`](nsstring.md) objects. The file manager always prefers methods that take an [`NSURL`](nsurl.md) object over those that take an [`NSString`](nsstring.md) object.

You should associate your delegate with a unique instance of the [`FileManager`](filemanager.md) class, as opposed to the shared instance.

## Topics

### Moving  an Item
- [func fileManager(FileManager, shouldMoveItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldmoveitemat:to:).md)
  Asks the delegate if the file manager should move the specified item to the new URL.
- [func fileManager(FileManager, shouldMoveItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldmoveitematpath:topath:).md)
  Asks the delegate if the file manager should move the specified item to the new path.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, movingItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitemat:to:).md)
  Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, movingItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitematpath:topath:).md)
  Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.
### Copying  an Item
- [func fileManager(FileManager, shouldCopyItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldcopyitemat:to:).md)
  Asks the delegate if the file manager should copy the specified item to the new URL.
- [func fileManager(FileManager, shouldCopyItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldcopyitematpath:topath:).md)
  Asks the delegate if the file manager should copy the specified item to the new path.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, copyingItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitemat:to:).md)
  Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, copyingItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitematpath:topath:).md)
  Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified path.
### Removing an Item
- [func fileManager(FileManager, shouldRemoveItemAt: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldremoveitemat:).md)
  Asks the delegate whether the item at the specified URL should be deleted.
- [func fileManager(FileManager, shouldRemoveItemAtPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldremoveitematpath:).md)
  Asks the delegate whether the item at the specified path should be deleted.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, removingItemAt: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitemat:).md)
  Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, removingItemAtPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitematpath:).md)
  Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.
### Linking an Item
- [func fileManager(FileManager, shouldLinkItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldlinkitemat:to:).md)
  Asks the delegate if a hard link should be created between the items at the two URLs.
- [func fileManager(FileManager, shouldLinkItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldlinkitematpath:topath:).md)
  Asks the delegate if a hard link should be created between the items at the two paths.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, linkingItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitemat:to:).md)
  Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, linkingItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitematpath:topath:).md)
  Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified path.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md)
  Prevent data loss and app crashes by interacting with the file system in a coordinated, asynchronous manner and by avoiding unnecessary disk I/O.
- [class FileManager](filemanager.md)
  A convenient interface to the contents of the file system, and the primary means of interacting with it.
- [About Apple File System](about-apple-file-system.md)
  Use high-level APIs to get the most out of Apple File System.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate)*