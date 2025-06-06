# createSymbolicLink(atPath:pathContent:)

**Framework**: Foundation  
**Kind**: method

Creates a symbolic link identified by a given path that refers to a given location.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func createSymbolicLink(atPath path: String, pathContent otherpath: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation is successful, otherwise [`false`](https://developer.apple.com/documentation/swift/false). Returns [`false`](https://developer.apple.com/documentation/swift/false) if a file, directory, or symbolic link identical to `path` already exists.

#### Discussion

Creates a symbolic link identified by `path` that refers to the location `otherPath` in the file system.

##### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`createSymbolicLink(atPath:withDestinationPath:)`](filemanager/createsymboliclink(atpath:withdestinationpath:).md) instead.

## Parameters

- `path`: The path for a symbolic link.
- `otherpath`: The path to which   should refer.

## See Also

- [func removeItem(atPath: String) throws](filemanager/removeitem(atpath:).md)
  Removes the file or directory at the specified path.
- [func destinationOfSymbolicLink(atPath: String) throws -> String](filemanager/destinationofsymboliclink(atpath:).md)
  Returns the path of the item pointed to by a symbolic link.
- [func createSymbolicLink(atPath: String, withDestinationPath: String) throws](filemanager/createsymboliclink(atpath:withdestinationpath:).md)
  Creates a symbolic link that points to the specified destination.
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](filemanager/changefileattributes(_:atpath:).md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](filemanager/fileattributes(atpath:traverselink:).md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](filemanager/filesystemattributes(atpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func directoryContents(atPath: String) -> [Any]?](filemanager/directorycontents(atpath:).md)
  Returns the directories and files (including symbolic links) contained in a given directory.
- [func createDirectory(atPath: String, attributes: [AnyHashable : Any]) -> Bool](filemanager/createdirectory(atpath:attributes:).md)
  Creates a directory (without contents) at a given path with given attributes.
- [func pathContentOfSymbolicLink(atPath: String) -> String?](filemanager/pathcontentofsymboliclink(atpath:).md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool](../ObjectiveC/NSObject-swift.class/fileManager(_:shouldProceedAfterError:).md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(_ fm: FileManager, willProcessPath path: String)](../ObjectiveC/NSObject-swift.class/fileManager(_:willProcessPath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/createsymboliclink(atpath:pathcontent:))*