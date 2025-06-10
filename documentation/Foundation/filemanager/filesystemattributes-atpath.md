# fileSystemAttributes(atPath:)

**Framework**: Foundation  
**Kind**: method

Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fileSystemAttributes(atPath path: String) -> [AnyHashable : Any]?
```

#### Return Value

An `NSDictionary` object that describes the attributes of the mounted file system on which `path` resides. See `File-System Attribute Keys` for a description of the keys available in the dictionary.

#### Discussion

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`attributesOfFileSystem(forPath:)`](filemanager/attributesoffilesystem(forpath:).md) instead.

## Parameters

- `path`: Any pathname within the mounted file system.

## See Also

- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesofitem(atpath:).md)
  Returns the attributes of the item at a given path.
- [func attributesOfFileSystem(forPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesoffilesystem(forpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](filemanager/setattributes(_:ofitematpath:).md)
  Sets the attributes of the specified file or directory.
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](filemanager/changefileattributes(_:atpath:).md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](filemanager/fileattributes(atpath:traverselink:).md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func directoryContents(atPath: String) -> [Any]?](filemanager/directorycontents(atpath:).md)
  Returns the directories and files (including symbolic links) contained in a given directory.
- [func createDirectory(atPath: String, attributes: [AnyHashable : Any]) -> Bool](filemanager/createdirectory(atpath:attributes:).md)
  Creates a directory (without contents) at a given path with given attributes.
- [func createSymbolicLink(atPath: String, pathContent: String) -> Bool](filemanager/createsymboliclink(atpath:pathcontent:).md)
  Creates a symbolic link identified by a given path that refers to a given location.
- [func pathContentOfSymbolicLink(atPath: String) -> String?](filemanager/pathcontentofsymboliclink(atpath:).md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/filesystemattributes(atpath:))*