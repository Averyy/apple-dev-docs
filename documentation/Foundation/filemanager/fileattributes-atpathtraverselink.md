# fileAttributes(atPath:traverseLink:)

**Framework**: Foundation  
**Kind**: method

Returns a dictionary that describes the POSIX attributes of the file specified at a given.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fileAttributes(atPath path: String, traverseLink yorn: Bool) -> [AnyHashable : Any]?
```

#### Return Value

An `NSDictionary` object that describes the POSIX attributes of the file specified at `path`. The keys in the dictionary are described in `File Attribute Keys`. If there is no item at `path`, returns `nil`.

#### Discussion

This code example gets several attributes of a file and logs them.

```objc
NSFileManager *fileManager = [[NSFileManager alloc] init];
NSString *path = @"/tmp/List";
NSDictionary *fileAttributes = [fileManager fileAttributesAtPath:path traverseLink:YES];
 
if (fileAttributes != nil) {
    NSNumber *fileSize;
    NSString *fileOwner;
    NSDate *fileModDate;
    if (fileSize = [fileAttributes objectForKey:NSFileSize]) {
        NSLog(@"File size: %qi\n", [fileSize unsignedLongLongValue]);
    }
    if (fileOwner = [fileAttributes objectForKey:NSFileOwnerAccountName]) {
        NSLog(@"Owner: %@\n", fileOwner);
    }
    if (fileModDate = [fileAttributes objectForKey:NSFileModificationDate]) {
        NSLog(@"Modification date: %@\n", fileModDate);
    }
}
else {
    NSLog(@"Path (%@) is invalid.", path);
}
```

As a convenience, `NSDictionary` provides a set of methods (declared as a category in `NSFileManager.h`) for quickly and efficiently obtaining attribute information from the returned dictionary: [`fileGroupOwnerAccountName()`](nsdictionary/filegroupowneraccountname().md), [`fileModificationDate()`](nsdictionary/filemodificationdate().md), [`fileOwnerAccountName()`](nsdictionary/fileowneraccountname().md), [`filePosixPermissions()`](nsdictionary/fileposixpermissions().md), [`fileSize()`](nsdictionary/filesize().md), [`fileSystemFileNumber()`](nsdictionary/filesystemfilenumber().md), [`fileSystemNumber()`](nsdictionary/filesystemnumber().md), and [`fileType()`](nsdictionary/filetype().md). For example, you could rewrite the file modification statement in the code example above as:

```objc
if (fileModDate = [fileAttributes fileModificationDate])
    NSLog(@"Modification date: %@\n", fileModDate);
```

##### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`attributesOfItem(atPath:)`](filemanager/attributesofitem(atpath:).md) instead.

## Parameters

- `path`: A file path.
- `yorn`: If   is not a symbolic link, this parameter has no effect. If   is a symbolic link, then:

## See Also

- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesofitem(atpath:).md)
  Returns the attributes of the item at a given path.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](filemanager/setattributes(_:ofitematpath:).md)
  Sets the attributes of the specified file or directory.
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](filemanager/changefileattributes(_:atpath:).md)
  Changes the attributes of a given file or directory.
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
- [func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool](../ObjectiveC/NSObject-swift.class/fileManager(_:shouldProceedAfterError:).md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(_ fm: FileManager, willProcessPath path: String)](../ObjectiveC/NSObject-swift.class/fileManager(_:willProcessPath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/fileattributes(atpath:traverselink:))*