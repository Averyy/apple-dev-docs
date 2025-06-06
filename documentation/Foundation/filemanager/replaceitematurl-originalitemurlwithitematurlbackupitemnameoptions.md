# replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)

**Framework**: Foundation  
**Kind**: method

Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+
- Unknown ?+ - Deprecated
- visionOS 1.0+

## Declaration

```swift
func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL newItemURL: NSURL, backupItemName: String? = nil, options: FileManager.ItemReplacementOptions = []) throws -> NSURL?
```

#### Return Value

The URL of the new item. If no new file system object is required, the URL object in this parameter may be the same passed to the originalItemURL parameter. However, if a new file system object is required, the URL object may be different. For example, replacing an RTF document with an RTFD document requires the creation of a new file.

#### Discussion

By default, the creation date, permissions, Finder label and color, and Spotlight comments of the original item are preserved on the new item. You can configure which metadata is preserved using the options parameter.

This method works only when the originalItemURL and newItemURL parameters are located on the same volume. Attempting to call this method by passing originalItemURL and newItemURL parameters that have locations on different volumes results in an error. Instead, you can call the [`url(for:in:appropriateFor:create:)`](filemanager/url(for:in:appropriatefor:create:).md) method, passing [`FileManager.SearchPathDirectory.itemReplacementDirectory`](filemanager/searchpathdirectory/itemreplacementdirectory.md) as the search path directory, to get a temporary URL on the destination’s volume that is suitable for use with this method.

If an error occurs and the original item is not in the original location or a temporary location, the resulting error object contains a user info dictionary with the key `"NSFileOriginalItemLocationKey"`. The value assigned to that key is an [`NSURL`](nsurl.md) object with the location of the item. The error code is one of the file-related errors described in [`NSError Codes`](1448136-nserror-codes.md).

## Parameters

- `originalItemURL`: The item containing the content you want to replace.
- `newItemURL`: The item containing the new content for  . It is recommended that you put this item in a temporary directory as provided by the OS. If a temporary directory is not available, put this item in a uniquely named directory that is in the same directory as the original item.
- `backupItemName`: The backup item will be removed in the event of success unless the   option is provided in options.
- `options`: The options to use during the replacement. Typically, you pass   for this parameter, which uses only the metadata from the new item. You can also combine the options described in   using the C-bitwise OR operator.

## See Also

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
- [func pathContentOfSymbolicLink(atPath: String) -> String?](filemanager/pathcontentofsymboliclink(atpath:).md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool](../ObjectiveC/NSObject-swift.class/fileManager(_:shouldProceedAfterError:).md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(_ fm: FileManager, willProcessPath path: String)](../ObjectiveC/NSObject-swift.class/fileManager(_:willProcessPath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:))*