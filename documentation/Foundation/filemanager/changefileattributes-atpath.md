# changeFileAttributes(_:atPath:)

**Framework**: Foundation  
**Kind**: method

Changes the attributes of a given file or directory.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func changeFileAttributes(_ attributes: [AnyHashable : Any] = [:], atPath path: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if  changes succeed. If any change fails, returns [`false`](https://developer.apple.com/documentation/Swift/false), but it is undefined whether any changes actually occurred.

#### Discussion

As in the POSIX standard, the app either must own the file or directory or must be running as superuser for attribute changes to take effect. The method attempts to make all changes specified in attributes and ignores any rejection of an attempted modification.

The `NSFilePosixPermissions` value must be initialized with the code representing the POSIX file-permissions bit pattern. `NSFileHFSCreatorCode` and `NSFileHFSTypeCode` will only be heeded when `path` specifies a file.

##### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`setAttributes(_:ofItemAtPath:)`](filemanager/setattributes(_:ofitematpath:).md) instead.

## Parameters

- `attributes`: For the   value, specify a file mode from the OR’d permission bit masks defined in  . See the man page for the   function ( ) for an explanation.
- `path`: A path to a file or directory.

## See Also

- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesofitem(atpath:).md)
  Returns the attributes of the item at a given path.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](filemanager/setattributes(_:ofitematpath:).md)
  Sets the attributes of the specified file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](filemanager/fileattributes(atpath:traverselink:).md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](filemanager/filesystemattributes(atpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func directoryContents(atPath: String) -> [Any]?](filemanager/directorycontents(atpath:).md)
  Returns the directories and files (including symbolic links) contained in a given directory.
- [func createDirectory(atPath: String, attributes: [AnyHashable : Any]) -> Bool](filemanager/createdirectory(atpath:attributes:).md)
  Creates a directory (without contents) at a given path with given attributes.
- [func createSymbolicLink(atPath: String, pathContent: String) -> Bool](filemanager/createsymboliclink(atpath:pathcontent:).md)
  Creates a symbolic link identified by a given path that refers to a given location.
- [func pathContentOfSymbolicLink(atPath: String) -> String?](filemanager/pathcontentofsymboliclink(atpath:).md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](../ObjectiveC/NSObject-swift.class/fileManager(_:shouldProceedAfterError:).md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(FileManager, willProcessPath: String)](../ObjectiveC/NSObject-swift.class/fileManager(_:willProcessPath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/changefileattributes(_:atpath:))*