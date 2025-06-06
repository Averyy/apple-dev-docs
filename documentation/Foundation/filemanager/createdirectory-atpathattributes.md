# createDirectory(atPath:attributes:)

**Framework**: Foundation  
**Kind**: method

Creates a directory (without contents) at a given path with given attributes.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func createDirectory(atPath path: String, attributes: [AnyHashable : Any] = [:]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation was successful, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`createDirectory(atPath:withIntermediateDirectories:attributes:)`](filemanager/createdirectory(atpath:withintermediatedirectories:attributes:).md) instead.

## Parameters

- `path`: The path at which to create the new directory. The directory to be created must not yet exist, but its parent directory must exist.
- `attributes`: The file attributes for the new directory. The attributes you can set are owner and group numbers, file permissions, and modification date. If you specify   for  , default values for these attributes are set (particularly write access for the creator and read access for others). For a list of keys you can include in this dictionary, Supporting Types. Some of the keys, such as   and  , do not apply to directories.

## See Also

- [func changeCurrentDirectoryPath(String) -> Bool](filemanager/changecurrentdirectorypath(_:).md)
  Changes the path of the current working directory to the specified path.
- [func createDirectory(atPath: String, withIntermediateDirectories: Bool, attributes: [FileAttributeKey : Any]?) throws](filemanager/createdirectory(atpath:withintermediatedirectories:attributes:).md)
  Creates a directory with given attributes at the specified path.
- [func createFile(atPath: String, contents: Data?, attributes: [FileAttributeKey : Any]?) -> Bool](filemanager/createfile(atpath:contents:attributes:).md)
  Creates a file with the specified content and attributes at the given location.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](filemanager/setattributes(_:ofitematpath:).md)
  Sets the attributes of the specified file or directory.
- [var currentDirectoryPath: String](filemanager/currentdirectorypath.md)
  The path to the program’s current directory.
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](filemanager/changefileattributes(_:atpath:).md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](filemanager/fileattributes(atpath:traverselink:).md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](filemanager/filesystemattributes(atpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func directoryContents(atPath: String) -> [Any]?](filemanager/directorycontents(atpath:).md)
  Returns the directories and files (including symbolic links) contained in a given directory.
- [func createSymbolicLink(atPath: String, pathContent: String) -> Bool](filemanager/createsymboliclink(atpath:pathcontent:).md)
  Creates a symbolic link identified by a given path that refers to a given location.
- [func pathContentOfSymbolicLink(atPath: String) -> String?](filemanager/pathcontentofsymboliclink(atpath:).md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool](../ObjectiveC/NSObject-swift.class/fileManager(_:shouldProceedAfterError:).md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(_ fm: FileManager, willProcessPath path: String)](../ObjectiveC/NSObject-swift.class/fileManager(_:willProcessPath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/createdirectory(atpath:attributes:))*