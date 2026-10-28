# fileSystemAttributes(atPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`attributesOfFileSystem(forPath:)`](./attributesoffilesystem%28forpath%29.md) instead.

## Declaration

```swift
func fileSystemAttributes(atPath path: String) -> [AnyHashable : Any]?
```

```objc
- (NSDictionary *) fileSystemAttributesAtPath:(NSString *) path;
```

## Return Value

An `NSDictionary` object that describes the attributes of the mounted file system on which `path` resides. See `File-System Attribute Keys` for a description of the keys available in the dictionary.

## Discussion

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`attributesOfFileSystem(forPath:)`](./attributesoffilesystem%28forpath%29.md) instead.

## Parameters

- `path`: Any pathname within the mounted file system.

## See Also

### Related Documentation
- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](./attributesofitem%28atpath%29.md)
  Returns the attributes of the item at a given path.
- [func attributesOfFileSystem(forPath: String) throws -> [FileAttributeKey : Any]](./attributesoffilesystem%28forpath%29.md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](./setattributes%28_,ofitematpath%29.md)
  Sets the attributes of the specified file or directory.
### Deprecated Methods
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](./changefileattributes%28_,atpath%29.md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](./fileattributes%28atpath,traverselink%29.md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func directoryContents(atPath: String) -> [Any]?](./directorycontents%28atpath%29.md)
  Returns the directories and files (including symbolic links) contained in a given directory.
- [func createDirectory(atPath: String, attributes: [AnyHashable : Any]) -> Bool](./createdirectory%28atpath,attributes%29.md)
  Creates a directory (without contents) at a given path with given attributes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/filesystemattributes(atpath:))*