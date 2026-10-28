# fileManager(_:shouldProceedAfterError:removingItemAtPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.

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
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, removingItemAtPath path: String) -> Bool
```

```objc
- (BOOL) fileManager:(NSFileManager *) fileManager shouldProceedAfterError:(NSError *) error removingItemAtPath:(NSString *) path;
```

## Return Value

[`true`](../../Swift/true.md) if the operation should proceed or [`false`](../../Swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [`false`](../../Swift/false.md).

## Discussion

The file manager calls this method when there is a problem deleting the item to the specified location. If you return [`true`](../../Swift/true.md), the file manager continues deleting any remaining items and ignores the error.

This method performs the same task as the [`fileManager(_:shouldProceedAfterError:removingItemAt:)`](./filemanager%28_,shouldproceedaftererror,removingitemat%29.md) method, which is preferred over this method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that attempted to remove the item.
- `error`: The error that occurred during the attempt to copy.
- `path`: The path for the file or directory that the file manager tried to delete.

## See Also

### Related Documentation
- [func removeItem(atPath: String) throws](../filemanager/removeitem%28atpath%29.md)
  Removes the file or directory at the specified path.
- [func removeItem(at: URL) throws](../filemanager/removeitem%28at%29.md)
  Removes the file or directory at the specified URL.
### Removing an Item
- [func fileManager(FileManager, shouldRemoveItemAt: URL) -> Bool](./filemanager%28_,shouldremoveitemat%29.md)
  Asks the delegate whether the item at the specified URL should be deleted.
- [func fileManager(FileManager, shouldRemoveItemAtPath: String) -> Bool](./filemanager%28_,shouldremoveitematpath%29.md)
  Asks the delegate whether the item at the specified path should be deleted.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, removingItemAt: URL) -> Bool](./filemanager%28_,shouldproceedaftererror,removingitemat%29.md)
  Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitematpath:))*