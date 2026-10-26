# createDirectory(atPath:attributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a directory (without contents) at a given path with given attributes.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`createDirectory(at:withIntermediateDirectories:attributes:)`](./createdirectory%28at,withintermediatedirectories,attributes%29.md) instead.

## Declaration

```swift
func createDirectory(atPath path: String, attributes: [AnyHashable : Any] = [:]) -> Bool
```

```objc
- (BOOL) createDirectoryAtPath:(NSString *) path attributes:(NSDictionary *) attributes;
```

#### Return Value

[`true`](../../Swift/true.md) if the operation was successful, otherwise [`false`](../../Swift/false.md).

#### Discussion

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`createDirectory(atPath:withIntermediateDirectories:attributes:)`](./createdirectory%28atpath,withintermediatedirectories,attributes%29.md) instead.

## Parameters

- `path`: The path at which to create the new directory. The directory to be created must not yet exist, but its parent directory must exist.
- `attributes`: The file attributes for the new directory. The attributes you can set are owner and group numbers, file permissions, and modification date. If you specify `nil` for `attributes`, default values for these attributes are set (particularly write access for the creator and read access for others). For a list of keys you can include in this dictionary, Supporting Types. Some of the keys, such as `NSFileHFSCreatorCode` and `NSFileHFSTypeCode`, do not apply to directories.

## See Also

### Related Documentation
- [func changeCurrentDirectoryPath(String) -> Bool](./changecurrentdirectorypath%28_%29.md)
  Changes the path of the current working directory to the specified path.
- [func createDirectory(atPath: String, withIntermediateDirectories: Bool, attributes: [FileAttributeKey : Any]?) throws](./createdirectory%28atpath,withintermediatedirectories,attributes%29.md)
  Creates a directory with given attributes at the specified path.
- [func createFile(atPath: String, contents: Data?, attributes: [FileAttributeKey : Any]?) -> Bool](./createfile%28atpath,contents,attributes%29.md)
  Creates a file with the specified content and attributes at the given location.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](./setattributes%28_,ofitematpath%29.md)
  Sets the attributes of the specified file or directory.
- [var currentDirectoryPath: String](./currentdirectorypath.md)
  The path to the program’s current directory.
### Deprecated Methods
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](./changefileattributes%28_,atpath%29.md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](./fileattributes%28atpath,traverselink%29.md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](./filesystemattributes%28atpath%29.md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func directoryContents(atPath: String) -> [Any]?](./directorycontents%28atpath%29.md)
  Returns the directories and files (including symbolic links) contained in a given directory.
- [func createSymbolicLink(atPath: String, pathContent: String) -> Bool](./createsymboliclink%28atpath,pathcontent%29.md)
  Creates a symbolic link identified by a given path that refers to a given location.
- [func pathContentOfSymbolicLink(atPath: String) -> String?](./pathcontentofsymboliclink%28atpath%29.md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](../../ObjectiveC/nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(FileManager, willProcessPath: String)](../../ObjectiveC/nsobject-swift.class/filemanager%28_,willprocesspath%29.md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](./replaceitematurl%28originalitemurl,withitematurl,backupitemname,options%29.md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [- copyPath:toPath:handler:](../nsfilemanager/copypath_topath_handler_.md)
  Copies the directory or file specified in a given path to a different location in the file system identified by another path.
- [- movePath:toPath:handler:](../nsfilemanager/movepath_topath_handler_.md)
  Moves the directory or file specified by a given path to a different location in the file system identified by another path.
- [- removeFileAtPath:handler:](../nsfilemanager/removefileatpath_handler_.md)
  Deletes the file, link, or directory (including, recursively, all subdirectories, files, and links in the directory) identified by a given path.
- [- linkPath:toPath:handler:](../nsfilemanager/linkpath_topath_handler_.md)
  Creates a link from a source to a destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/createdirectory(atpath:attributes:))*