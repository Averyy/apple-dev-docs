# directoryContents(atPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the directories and files (including symbolic links) contained in a given directory.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`contentsOfDirectory(atPath:)`](./contentsofdirectory%28atpath%29.md) instead.

## Declaration

```swift
func directoryContents(atPath path: String) -> [Any]?
```

```objc
- (NSArray *) directoryContentsAtPath:(NSString *) path;
```

#### Return Value

An array of [`NSString`](../nsstring.md) objects identifying the directories and files (including symbolic links) contained in `path`. Returns an empty array if the directory exists but has no contents. Returns `nil` if the directory specified at `path` does not exist or there is some other error accessing it.

#### Discussion

The search is shallow, and therefore does not return the contents of any subdirectories and does not traverse symbolic links in the specified directory. This returned array does not contain strings for the current directory (”`.`”), parent directory (”`..`”), or resource forks (begin with “._”).

##### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`contentsOfDirectory(atPath:)`](./contentsofdirectory%28atpath%29.md) instead.

## Parameters

- `path`: A path to a directory.

## See Also

### Related Documentation
- [var currentDirectoryPath: String](./currentdirectorypath.md)
  The path to the program’s current directory.
- [func fileExists(atPath: String, isDirectory: UnsafeMutablePointer<ObjCBool>?) -> Bool](./fileexists%28atpath,isdirectory%29.md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func subpaths(atPath: String) -> [String]?](./subpaths%28atpath%29.md)
  Returns an array of strings identifying the paths for all items in the specified directory.
- [func contentsOfDirectory(atPath: String) throws -> [String]](./contentsofdirectory%28atpath%29.md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(atPath: String) -> FileManager.DirectoryEnumerator?](./enumerator%28atpath%29.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
### Deprecated Methods
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](./changefileattributes%28_,atpath%29.md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](./fileattributes%28atpath,traverselink%29.md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](./filesystemattributes%28atpath%29.md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directorycontents(atpath:))*