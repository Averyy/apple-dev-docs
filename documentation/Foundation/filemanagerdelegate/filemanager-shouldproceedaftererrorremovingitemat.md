# fileManager(_:shouldProceedAfterError:removingItemAt:)

**Framework**: Foundation  
**Kind**: method

Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.

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
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, removingItemAt URL: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation should proceed or [`false`](https://developer.apple.com/documentation/swift/false) if it should be aborted. If you do not implement this method, the file manager assumes a response of [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The file manager calls this method when there is a problem deleting the item to the specified location. If you return [`true`](https://developer.apple.com/documentation/swift/true), the file manager continues deleting any remaining items and ignores the error.

This method performs the same task as the [`fileManager(_:shouldProceedAfterError:removingItemAtPath:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitematpath:).md) method and is preferred over that method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that attempted to remove the item.
- `error`: The error that occurred while attempting to remove the item at  .
- `URL`: The URL for the file or directory that the file manager tried to delete.

## See Also

- [func removeItem(atPath: String) throws](filemanager/removeitem(atpath:).md)
  Removes the file or directory at the specified path.
- [func removeItem(at: URL) throws](filemanager/removeitem(at:).md)
  Removes the file or directory at the specified URL.
- [func fileManager(FileManager, shouldRemoveItemAt: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldremoveitemat:).md)
  Asks the delegate whether the item at the specified URL should be deleted.
- [func fileManager(FileManager, shouldRemoveItemAtPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldremoveitematpath:).md)
  Asks the delegate whether the item at the specified path should be deleted.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, removingItemAtPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitematpath:).md)
  Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitemat:))*