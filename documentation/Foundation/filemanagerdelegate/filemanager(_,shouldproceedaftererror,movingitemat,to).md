# fileManager(_:shouldProceedAfterError:movingItemAt:to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) fileManager:(NSFileManager *) fileManager shouldProceedAfterError:(NSError *) error movingItemAtURL:(NSURL *) srcURL toURL:(NSURL *) dstURL;
```

## Return Value

[`true`](../../Swift/true.md) if the operation should proceed or [`false`](../../Swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [`false`](../../Swift/false.md).

## Discussion

The file manager calls this method when there is a problem moving the item to the specified location. If you return [`true`](../../Swift/true.md), the file manager proceeds to remove the item from its current location as if the move operation had completed successfully.

This method performs the same task as the [`fileManager(_:shouldProceedAfterError:movingItemAtPath:toPath:)`](./filemanager%28_,shouldproceedaftererror,movingitematpath,topath%29.md) method and is preferred over that method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that attempted to move the item.
- `error`: The error that occurred while trying to move the item in `srcURL`.
- `srcURL`: The URL of the file or directory that the file manager tried to move.
- `dstURL`: The URL of the intended destination for the item in `srcURL`.

## See Also

### Related Documentation
- [func moveItem(atPath: String, toPath: String) throws](../filemanager/moveitem%28atpath,topath%29.md)
  Moves the file or directory at the specified path to a new location synchronously.
- [func moveItem(at: URL, to: URL) throws](../filemanager/moveitem%28at,to%29.md)
  Moves the file or directory at the specified URL to a new location synchronously.
### Moving  an Item
- [func fileManager(FileManager, shouldMoveItemAt: URL, to: URL) -> Bool](./filemanager%28_,shouldmoveitemat,to%29.md)
  Asks the delegate if the file manager should move the specified item to the new URL.
- [func fileManager(FileManager, shouldMoveItemAtPath: String, toPath: String) -> Bool](./filemanager%28_,shouldmoveitematpath,topath%29.md)
  Asks the delegate if the file manager should move the specified item to the new path.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, movingItemAtPath: String, toPath: String) -> Bool](./filemanager%28_,shouldproceedaftererror,movingitematpath,topath%29.md)
  Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitemat:to:))*