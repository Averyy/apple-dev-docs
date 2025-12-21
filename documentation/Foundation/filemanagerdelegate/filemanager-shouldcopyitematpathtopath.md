# fileManager(_:shouldCopyItemAtPath:toPath:)

**Framework**: Foundation  
**Kind**: method

Asks the delegate if the file manager should copy the specified item to the new path.

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
optional func fileManager(_ fileManager: FileManager, shouldCopyItemAtPath srcPath: String, toPath dstPath: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the item should be copied or [`false`](https://developer.apple.com/documentation/Swift/false) if the file manager should stop copying items associated with the current operation. If you do not implement this method, the file manager assumes a response of [`true`](https://developer.apple.com/documentation/Swift/true).

#### Discussion

This method is called once for each item that needs to be copied. Thus, for a directory, this method is called once for the directory and once for each item in the directory.

This method performs the same task as the [`fileManager(_:shouldCopyItemAt:to:)`](filemanagerdelegate/filemanager(_:shouldcopyitemat:to:).md) method, which is preferred over this method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that is attempting to copy the file or directory.
- `srcPath`: The path to the file or directory that the file manager wants to copy.
- `dstPath`: The new path for the copied file or directory.

## See Also

- [func copyItem(atPath: String, toPath: String) throws](filemanager/copyitem(atpath:topath:).md)
  Copies the item at the specified path to a new location synchronously.
- [func copyItem(at: URL, to: URL) throws](filemanager/copyitem(at:to:).md)
  Copies the file at the specified URL to a new location synchronously.
- [func fileManager(FileManager, shouldCopyItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldcopyitemat:to:).md)
  Asks the delegate if the file manager should copy the specified item to the new URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, copyingItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitemat:to:).md)
  Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, copyingItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitematpath:topath:).md)
  Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldcopyitematpath:topath:))*