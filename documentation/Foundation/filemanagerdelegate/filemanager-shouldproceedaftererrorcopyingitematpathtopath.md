# fileManager(_:shouldProceedAfterError:copyingItemAtPath:toPath:)

**Framework**: Foundation  
**Kind**: method

Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified path.

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
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, copyingItemAtPath srcPath: String, toPath dstPath: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation should proceed or [`false`](https://developer.apple.com/documentation/swift/false) if it should be aborted. If you do not implement this method, the file manager assumes a response of [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The file manager calls this method when there is a problem copying the item to the specified location. If you return [`true`](https://developer.apple.com/documentation/swift/true), the file manager continues copying any other items and ignores the error.

This method performs the same task as the [`fileManager(_:shouldProceedAfterError:copyingItemAt:to:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitemat:to:).md) method, which is preferred over this method in macOS 10.6 and later.

## Parameters

- `fileManager`: The   object that sent this message.
- `error`: The error that occurred during the attempt to copy.
- `srcPath`: The path or a file or directory that   is attempting to copy.
- `dstPath`: The path or a file or directory to which   is attempting to copy.

## See Also

- [func copyItem(atPath: String, toPath: String) throws](filemanager/copyitem(atpath:topath:).md)
  Copies the item at the specified path to a new location synchronously.
- [func copyItem(at: URL, to: URL) throws](filemanager/copyitem(at:to:).md)
  Copies the file at the specified URL to a new location synchronously.
- [func fileManager(FileManager, shouldCopyItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldcopyitemat:to:).md)
  Asks the delegate if the file manager should copy the specified item to the new URL.
- [func fileManager(FileManager, shouldCopyItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldcopyitematpath:topath:).md)
  Asks the delegate if the file manager should copy the specified item to the new path.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, copyingItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitemat:to:).md)
  Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitematpath:topath:))*