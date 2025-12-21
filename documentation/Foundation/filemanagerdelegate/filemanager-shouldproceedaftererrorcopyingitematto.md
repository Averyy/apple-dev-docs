# fileManager(_:shouldProceedAfterError:copyingItemAt:to:)

**Framework**: Foundation  
**Kind**: method

Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified URL.

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
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, copyingItemAt srcURL: URL, to dstURL: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the operation should proceed or [`false`](https://developer.apple.com/documentation/Swift/false) if it should be aborted. If you do not implement this method, the file manager assumes a response of [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The file manager calls this method when there is a problem copying the item to the specified location. If you return [`true`](https://developer.apple.com/documentation/Swift/true), the file manager continues copying any other items and ignores the error.

This method performs the same task as the [`fileManager(_:shouldProceedAfterError:copyingItemAtPath:toPath:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitematpath:topath:).md) method and is preferred over that method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that attempted to copy the item.
- `error`: The error that occurred during the attempt to copy.
- `srcURL`: The URL or a file or directory that   is attempting to copy.
- `dstURL`: The URL or a file or directory to which   is attempting to copy.

## See Also

- [func copyItem(atPath: String, toPath: String) throws](filemanager/copyitem(atpath:topath:).md)
  Copies the item at the specified path to a new location synchronously.
- [func copyItem(at: URL, to: URL) throws](filemanager/copyitem(at:to:).md)
  Copies the file at the specified URL to a new location synchronously.
- [func fileManager(FileManager, shouldCopyItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldcopyitemat:to:).md)
  Asks the delegate if the file manager should copy the specified item to the new URL.
- [func fileManager(FileManager, shouldCopyItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldcopyitematpath:topath:).md)
  Asks the delegate if the file manager should copy the specified item to the new path.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, copyingItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitematpath:topath:).md)
  Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitemat:to:))*