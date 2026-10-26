# movePath:toPath:handler:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Moves the directory or file specified by a given path to a different location in the file system identified by another path.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`moveItem(at:to:)`](../filemanager/moveitem%28at,to%29.md) instead.

## Declaration

```objc
- (BOOL) movePath:(NSString *) src toPath:(NSString *) dest handler:(id) handler;
```

#### Return Value

[`true`](../../Swift/true.md) if the move operation is successful. If the operation is not successful, but the handler method [`fileManager(_:shouldProceedAfterError:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md) returns [`true`](../../Swift/true.md), [`movePath:toPath:handler:`](./movepath_topath_handler_.md) also returns [`true`](../../Swift/true.md); otherwise returns [`false`](../../Swift/false.md).

#### Discussion

If `source` is a file, the method creates a file at `destination` that holds the exact contents of the original file and then deletes the original file. If `source` is a directory, [`movePath:toPath:handler:`](./movepath_topath_handler_.md) creates a new directory at `destination` and recursively populates it with duplicates of the files and directories contained in `source`. It then deletes the old directory and its contents.  Symbolic links are not traversed, however links are preserved. File or directory attributes—that is, metadata such as owner and group numbers, file permissions, and modification date—are also moved.

The handler callback mechanism is similar to delegation. `NSFileManager` sends [`fileManager(_:willProcessPath:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,willprocesspath%29.md) when it begins a copy, move, remove, or link operation. It sends [`fileManager(_:shouldProceedAfterError:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md) when it encounters any error in processing.

If a failure in a move operation occurs, either the preexisting path or the new path remains intact, but not both.

##### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`moveItem(at:to:)`](../filemanager/moveitem%28at,to%29.md) instead.

## Parameters

- `src`: The path of a file or directory to move. `source` must exist.
- `dest`: The path to which `source` is moved. `destination` must not yet exist. The destination path must end in a filename; there is no implicit adoption of the source filename.
- `handler`: An object that responds to the callback messages [`fileManager(_:willProcessPath:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,willprocesspath%29.md) and [`fileManager(_:shouldProceedAfterError:)`](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md). You can specify `nil` for `handler`; if you do so and an error occurs, the method automatically returns [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [func linkItem(at: URL, to: URL) throws](../filemanager/linkitem%28at,to%29.md)
  Creates a hard link between the items at the specified URLs.
- [func moveItem(atPath: String, toPath: String) throws](../filemanager/moveitem%28atpath,topath%29.md)
  Moves the file or directory at the specified path to a new location synchronously.
- [func copyItem(atPath: String, toPath: String) throws](../filemanager/copyitem%28atpath,topath%29.md)
  Copies the item at the specified path to a new location synchronously.
- [func removeItem(atPath: String) throws](../filemanager/removeitem%28atpath%29.md)
  Removes the file or directory at the specified path.
### Deprecated Methods
- [- copyPath:toPath:handler:](./copypath_topath_handler_.md)
  Copies the directory or file specified in a given path to a different location in the file system identified by another path.
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
- [- linkPath:toPath:handler:](./linkpath_topath_handler_.md)
  Creates a link from a source to a destination.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(FileManager, willProcessPath: String)](../../ObjectiveC/nsobject-swift.class/filemanager%28_,willprocesspath%29.md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanager/movepath:topath:handler:)*