# fileAttributes(atPath:traverseLink:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary that describes the POSIX attributes of the file specified at a given.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`attributesOfItem(atPath:)`](./attributesofitem%28atpath%29.md) instead.

## Declaration

```swift
func fileAttributes(atPath path: String, traverseLink yorn: Bool) -> [AnyHashable : Any]?
```

```objc
- (NSDictionary *) fileAttributesAtPath:(NSString *) path traverseLink:(BOOL) yorn;
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

As a convenience, `NSDictionary` provides a set of methods (declared as a category in `NSFileManager.h`) for quickly and efficiently obtaining attribute information from the returned dictionary: [`fileGroupOwnerAccountName()`](../nsdictionary/filegroupowneraccountname%28%29.md), [`fileModificationDate()`](../nsdictionary/filemodificationdate%28%29.md), [`fileOwnerAccountName()`](../nsdictionary/fileowneraccountname%28%29.md), [`filePosixPermissions()`](../nsdictionary/fileposixpermissions%28%29.md), [`fileSize()`](../nsdictionary/filesize%28%29.md), [`fileSystemFileNumber()`](../nsdictionary/filesystemfilenumber%28%29.md), [`fileSystemNumber()`](../nsdictionary/filesystemnumber%28%29.md), and [`fileType()`](../nsdictionary/filetype%28%29.md). For example, you could rewrite the file modification statement in the code example above as:

```objc
if (fileModDate = [fileAttributes fileModificationDate])
    NSLog(@"Modification date: %@\n", fileModDate);
```

##### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [`attributesOfItem(atPath:)`](./attributesofitem%28atpath%29.md) instead.

## Parameters

- `path`: A file path.
- `yorn`: If `path` is not a symbolic link, this parameter has no effect. If `path` is a symbolic link, then:

  - If [`true`](../../Swift/true.md) the attributes of the linked-to file are returned, or if the link points to a nonexistent file the method returns `nil`.
  - If [`false`](../../Swift/false.md), the attributes of the symbolic link are returned.

## See Also

### Related Documentation
- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](./attributesofitem%28atpath%29.md)
  Returns the attributes of the item at a given path.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](./setattributes%28_,ofitematpath%29.md)
  Sets the attributes of the specified file or directory.
### Deprecated Methods
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](./changefileattributes%28_,atpath%29.md)
  Changes the attributes of a given file or directory.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](./filesystemattributes%28atpath%29.md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/fileattributes(atpath:traverselink:))*