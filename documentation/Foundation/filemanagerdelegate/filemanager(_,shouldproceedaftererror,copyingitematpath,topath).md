# fileManager(_:shouldProceedAfterError:copyingItemAtPath:toPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) fileManager:(NSFileManager *) fileManager shouldProceedAfterError:(NSError *) error copyingItemAtPath:(NSString *) srcPath toPath:(NSString *) dstPath;
```

#### Return Value

[`true`](../../Swift/true.md) if the operation should proceed or [`false`](../../Swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [`false`](../../Swift/false.md).

#### Discussion

The file manager calls this method when there is a problem copying the item to the specified location. If you return [`true`](../../Swift/true.md), the file manager continues copying any other items and ignores the error.

This method performs the same task as the [`fileManager(_:shouldProceedAfterError:copyingItemAt:to:)`](./filemanager%28_,shouldproceedaftererror,copyingitemat,to%29.md) method, which is preferred over this method in macOS 10.6 and later.

## Parameters

- `fileManager`: The `NSFileManager` object that sent this message.
- `error`: The error that occurred during the attempt to copy.
- `srcPath`: The path or a file or directory that `fileManager` is attempting to copy.
- `dstPath`: The path or a file or directory to which `fileManager` is attempting to copy.

## See Also

### Related Documentation
- [func copyItem(atPath: String, toPath: String) throws](../filemanager/copyitem%28atpath,topath%29.md)
  Copies the item at the specified path to a new location synchronously.
- [func copyItem(at: URL, to: URL) throws](../filemanager/copyitem%28at,to%29.md)
  Copies the file at the specified URL to a new location synchronously.
### Copying  an Item
- [func fileManager(FileManager, shouldCopyItemAt: URL, to: URL) -> Bool](./filemanager%28_,shouldcopyitemat,to%29.md)
  Asks the delegate if the file manager should copy the specified item to the new URL.
- [func fileManager(FileManager, shouldCopyItemAtPath: String, toPath: String) -> Bool](./filemanager%28_,shouldcopyitematpath,topath%29.md)
  Asks the delegate if the file manager should copy the specified item to the new path.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, copyingItemAt: URL, to: URL) -> Bool](./filemanager%28_,shouldproceedaftererror,copyingitemat,to%29.md)
  Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitematpath:topath:))*