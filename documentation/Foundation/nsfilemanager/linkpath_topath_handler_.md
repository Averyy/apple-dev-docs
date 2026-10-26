# linkPath:toPath:handler:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a link from a source to a destination.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`linkItem(at:to:)`](../filemanager/linkitem%28at,to%29.md) instead.

## Declaration

```objc
- (BOOL) linkPath:(NSString *) src toPath:(NSString *) dest handler:(id) handler;
```

#### Return Value

[`true`](../../Swift/true.md) if the link operation is successful. If the operation is not successful, but the handler method [`fileManager(_:shouldProceedAfterError:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md) returns [`true`](../../Swift/true.md), also returns [`true`](../../Swift/true.md). Otherwise returns [`false`](../../Swift/false.md).

#### Discussion

The handler callback mechanism is similar to delegation. `NSFileManager` sends [`fileManager(_:willProcessPath:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,willprocesspath%29.md) when it begins a copy, move, remove, or link operation. It sends [`fileManager(_:shouldProceedAfterError:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md) when it encounters any error in processing

##### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`removeItem(atPath:)`](../filemanager/removeitem%28atpath%29.md) instead.

## Parameters

- `src`: A path that identifies a source file or directory.

  The file, link, or directory specified by `source` must exist.
- `dest`: A path that identifies a destination file or directory.

  The destination should not yet exist. The destination path must end in a filename; there is no implicit adoption of the source filename.
- `handler`: An object that responds to the callback messages [`fileManager(_:willProcessPath:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,willprocesspath%29.md) and [`fileManager(_:shouldProceedAfterError:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md). You can specify `nil` for `handler`; if you do so and an error occurs, the method automatically returns [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [func linkItem(at: URL, to: URL) throws](../filemanager/linkitem%28at,to%29.md)
  Creates a hard link between the items at the specified URLs.
- [func moveItem(atPath: String, toPath: String) throws](../filemanager/moveitem%28atpath,topath%29.md)
  Moves the file or directory at the specified path to a new location synchronously.
- [func createSymbolicLink(atPath: String, withDestinationPath: String) throws](../filemanager/createsymboliclink%28atpath,withdestinationpath%29.md)
  Creates a symbolic link that points to the specified destination.
- [func copyItem(atPath: String, toPath: String) throws](../filemanager/copyitem%28atpath,topath%29.md)
  Copies the item at the specified path to a new location synchronously.
- [func removeItem(atPath: String) throws](../filemanager/removeitem%28atpath%29.md)
  Removes the file or directory at the specified path.
### Deprecated Methods
- [- copyPath:toPath:handler:](./copypath_topath_handler_.md)
  Copies the directory or file specified in a given path to a different location in the file system identified by another path.
- [- movePath:toPath:handler:](./movepath_topath_handler_.md)
  Moves the directory or file specified by a given path to a different location in the file system identified by another path.
- [- removeFileAtPath:handler:](./removefileatpath_handler_.md)
  Deletes the file, link, or directory (including, recursively, all subdirectories, files, and links in the directory) identified by a given path.
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](../filemanager/changefileattributes%28_,atpath%29.md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](../filemanager/fileattributes%28atpath,traverselink%29.md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](../filemanager/filesystemattributes%28atpath%29.md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func directoryContents(atPath: String) -> [Any]?](../filemanager/directorycontents%28atpath%29.md)
  Returns the directories and files (including symbolic links) contained in a given directory.
- [func createDirectory(atPath: String, attributes: [AnyHashable : Any]) -> Bool](../filemanager/createdirectory%28atpath,attributes%29.md)
  Creates a directory (without contents) at a given path with given attributes.
- [func createSymbolicLink(atPath: String, pathContent: String) -> Bool](../filemanager/createsymboliclink%28atpath,pathcontent%29.md)
  Creates a symbolic link identified by a given path that refers to a given location.
- [func pathContentOfSymbolicLink(atPath: String) -> String?](../filemanager/pathcontentofsymboliclink%28atpath%29.md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(FileManager, willProcessPath: String)](../../ObjectiveC/nsobject-swift.class/filemanager%28_,willprocesspath%29.md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanager/linkpath:topath:handler:)*