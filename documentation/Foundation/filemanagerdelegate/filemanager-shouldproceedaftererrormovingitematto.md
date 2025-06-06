# fileManager(_:shouldProceedAfterError:movingItemAt:to:)

**Framework**: Foundation  
**Kind**: method

Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified URL.

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
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, movingItemAt srcURL: URL, to dstURL: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation should proceed or [`false`](https://developer.apple.com/documentation/swift/false) if it should be aborted. If you do not implement this method, the file manager assumes a response of [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The file manager calls this method when there is a problem moving the item to the specified location. If you return [`true`](https://developer.apple.com/documentation/swift/true), the file manager proceeds to remove the item from its current location as if the move operation had completed successfully.

This method performs the same task as the [`fileManager(_:shouldProceedAfterError:movingItemAtPath:toPath:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitematpath:topath:).md) method and is preferred over that method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that attempted to move the item.
- `error`: The error that occurred while trying to move the item in  .
- `srcURL`: The URL of the file or directory that the file manager tried to move.
- `dstURL`: The URL of the intended destination for the item in  .

## See Also

- [func moveItem(atPath: String, toPath: String) throws](filemanager/moveitem(atpath:topath:).md)
  Moves the file or directory at the specified path to a new location synchronously.
- [func moveItem(at: URL, to: URL) throws](filemanager/moveitem(at:to:).md)
  Moves the file or directory at the specified URL to a new location synchronously.
- [func fileManager(FileManager, shouldMoveItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldmoveitemat:to:).md)
  Asks the delegate if the file manager should move the specified item to the new URL.
- [func fileManager(FileManager, shouldMoveItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldmoveitematpath:topath:).md)
  Asks the delegate if the file manager should move the specified item to the new path.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, movingItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitematpath:topath:).md)
  Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitemat:to:))*