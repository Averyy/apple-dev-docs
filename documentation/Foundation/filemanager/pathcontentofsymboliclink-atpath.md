# pathContentOfSymbolicLink(atPath:)

**Framework**: Foundation  
**Kind**: method

Returns the path of the directory or file that a symbolic link at a given path refers to.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func pathContentOfSymbolicLink(atPath path: String) -> String?
```

#### Return Value

The path of the directory or file to which the symbolic link `path` refers, or `nil` upon failure. If the symbolic link is specified as a relative path, that relative path is returned.

#### Discussion

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`destinationOfSymbolicLink(atPath:)`](filemanager/destinationofsymboliclink(atpath:).md) instead.

## Parameters

- `path`: The path of a symbolic link.

## See Also

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
- [func createSymbolicLink(atPath: String, pathContent: String) -> Bool](filemanager/createsymboliclink(atpath:pathcontent:).md)
  Creates a symbolic link identified by a given path that refers to a given location.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/pathcontentofsymboliclink(atpath:))*