# fileManager(_:shouldRemoveItemAt:)

**Framework**: Foundation  
**Kind**: method

Asks the delegate whether the item at the specified URL should be deleted.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func fileManager(_ fileManager: FileManager, shouldRemoveItemAt URL: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified item should be removed or [`false`](https://developer.apple.com/documentation/swift/false) if it should not be removed.

#### Discussion

Removed items are deleted immediately and not placed in the Trash. If the specified item is a directory, returning [`false`](https://developer.apple.com/documentation/swift/false) prevents both the directory and its children from being deleted.

This method performs the same task as the [`fileManager(_:shouldRemoveItemAtPath:)`](filemanagerdelegate/filemanager(_:shouldremoveitematpath:).md) method and is preferred over that method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that is attempting to remove the file or directory.
- `URL`: The URL indicating the file or directory that the file manager is attempting to delete.

## See Also

- [func removeItem(atPath: String) throws](filemanager/removeitem(atpath:).md)
  Removes the file or directory at the specified path.
- [func removeItem(at: URL) throws](filemanager/removeitem(at:).md)
  Removes the file or directory at the specified URL.
- [func fileManager(FileManager, shouldRemoveItemAtPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldremoveitematpath:).md)
  Asks the delegate whether the item at the specified path should be deleted.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, removingItemAt: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitemat:).md)
  Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, removingItemAtPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitematpath:).md)
  Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldremoveitemat:))*