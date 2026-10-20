# fileManager(_:shouldRemoveItemAt:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) fileManager:(NSFileManager *) fileManager shouldRemoveItemAtURL:(NSURL *) URL;
```

#### Return Value

[`true`](../../Swift/true.md) if the specified item should be removed or [`false`](../../Swift/false.md) if it should not be removed.

#### Discussion

Removed items are deleted immediately and not placed in the Trash. If the specified item is a directory, returning [`false`](../../Swift/false.md) prevents both the directory and its children from being deleted.

This method performs the same task as the [`fileManager(_:shouldRemoveItemAtPath:)`](./filemanager%28_,shouldremoveitematpath%29.md) method and is preferred over that method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that is attempting to remove the file or directory.
- `URL`: The URL indicating the file or directory that the file manager is attempting to delete.

## See Also

### Related Documentation
- [func removeItem(atPath: String) throws](../filemanager/removeitem%28atpath%29.md)
  Removes the file or directory at the specified path.
- [func removeItem(at: URL) throws](../filemanager/removeitem%28at%29.md)
  Removes the file or directory at the specified URL.
### Removing an Item
- [func fileManager(FileManager, shouldRemoveItemAtPath: String) -> Bool](./filemanager%28_,shouldremoveitematpath%29.md)
  Asks the delegate whether the item at the specified path should be deleted.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, removingItemAt: URL) -> Bool](./filemanager%28_,shouldproceedaftererror,removingitemat%29.md)
  Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, removingItemAtPath: String) -> Bool](./filemanager%28_,shouldproceedaftererror,removingitematpath%29.md)
  Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldremoveitemat:))*