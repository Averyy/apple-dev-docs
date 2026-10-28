# fileManager(_:shouldMoveItemAt:to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the file manager should move the specified item to the new URL.

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
optional func fileManager(_ fileManager: FileManager, shouldMoveItemAt srcURL: URL, to dstURL: URL) -> Bool
```

```objc
- (BOOL) fileManager:(NSFileManager *) fileManager shouldMoveItemAtURL:(NSURL *) srcURL toURL:(NSURL *) dstURL;
```

## Return Value

[`true`](../../Swift/true.md) if the item should be moved or [`false`](../../Swift/false.md) if it should not be moved. If you do not implement this method, the file manager assumes a response of [`true`](../../Swift/true.md).

## Discussion

This method is called only once for the item being moved, regardless of whether the item is a file, directory, or symbolic link.

This method performs the same task as the [`fileManager(_:shouldMoveItemAtPath:toPath:)`](./filemanager%28_,shouldmoveitematpath,topath%29.md) method and is preferred over that method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that is attempting to move the file or directory.
- `srcURL`: The URL of the file or directory that the file manager wants to move.
- `dstURL`: The URL specifying the new location for the file or directory.

## See Also

### Related Documentation
- [func moveItem(atPath: String, toPath: String) throws](../filemanager/moveitem%28atpath,topath%29.md)
  Moves the file or directory at the specified path to a new location synchronously.
- [func moveItem(at: URL, to: URL) throws](../filemanager/moveitem%28at,to%29.md)
  Moves the file or directory at the specified URL to a new location synchronously.
### Moving  an Item
- [func fileManager(FileManager, shouldMoveItemAtPath: String, toPath: String) -> Bool](./filemanager%28_,shouldmoveitematpath,topath%29.md)
  Asks the delegate if the file manager should move the specified item to the new path.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, movingItemAt: URL, to: URL) -> Bool](./filemanager%28_,shouldproceedaftererror,movingitemat,to%29.md)
  Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, movingItemAtPath: String, toPath: String) -> Bool](./filemanager%28_,shouldproceedaftererror,movingitematpath,topath%29.md)
  Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldmoveitemat:to:))*