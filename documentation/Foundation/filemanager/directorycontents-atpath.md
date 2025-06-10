# directoryContents(atPath:)

**Framework**: Foundation  
**Kind**: method

Returns the directories and files (including symbolic links) contained in a given directory.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func directoryContents(atPath path: String) -> [Any]?
```

#### Return Value

An array of [`NSString`](nsstring.md) objects identifying the directories and files (including symbolic links) contained in `path`. Returns an empty array if the directory exists but has no contents. Returns `nil` if the directory specified at `path` does not exist or there is some other error accessing it.

#### Discussion

The search is shallow, and therefore does not return the contents of any subdirectories and does not traverse symbolic links in the specified directory. This returned array does not contain strings for the current directory (”`.`”), parent directory (”`..`”), or resource forks (begin with “._”).

##### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`contentsOfDirectory(atPath:)`](filemanager/contentsofdirectory(atpath:).md) instead.

## Parameters

- `path`: A path to a directory.

## See Also

- [var currentDirectoryPath: String](filemanager/currentdirectorypath.md)
  The path to the program’s current directory.
- [func fileExists(atPath: String, isDirectory: UnsafeMutablePointer<ObjCBool>?) -> Bool](filemanager/fileexists(atpath:isdirectory:).md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func subpaths(atPath: String) -> [String]?](filemanager/subpaths(atpath:).md)
  Returns an array of strings identifying the paths for all items in the specified directory.
- [func contentsOfDirectory(atPath: String) throws -> [String]](filemanager/contentsofdirectory(atpath:).md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(atPath: String) -> FileManager.DirectoryEnumerator?](filemanager/enumerator(atpath:).md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](filemanager/changefileattributes(_:atpath:).md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](filemanager/fileattributes(atpath:traverselink:).md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](filemanager/filesystemattributes(atpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func createDirectory(atPath: String, attributes: [AnyHashable : Any]) -> Bool](filemanager/createdirectory(atpath:attributes:).md)
  Creates a directory (without contents) at a given path with given attributes.
- [func createSymbolicLink(atPath: String, pathContent: String) -> Bool](filemanager/createsymboliclink(atpath:pathcontent:).md)
  Creates a symbolic link identified by a given path that refers to a given location.
- [func pathContentOfSymbolicLink(atPath: String) -> String?](filemanager/pathcontentofsymboliclink(atpath:).md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directorycontents(atpath:))*