# attributesOfItem(atPath:)

**Framework**: Foundation  
**Kind**: method

Returns the attributes of the item at a given path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func attributesOfItem(atPath path: String) throws -> [FileAttributeKey : Any]
```

#### Return Value

A dictionary object that describes the attributes (file, directory, symlink, and so on) of the file specified by `path` (or `nil` if an error occurred in Objective-C). The keys in the dictionary are described in `File Attribute Keys`.

#### Discussion

If the item at the path is a symbolic link—that is, the value of the [`type`](fileattributekey/type.md) key in the attributes dictionary is [`typeSymbolicLink`](fileattributetype/typesymboliclink.md)—you can use the [`destinationOfSymbolicLink(atPath:)`](filemanager/destinationofsymboliclink(atpath:).md) method to retrieve the path of the item pointed to by the link. You can also use the [`resolvingSymlinksInPath`](nsstring/resolvingsymlinksinpath.md) method of [`NSString`](nsstring.md) to resolve links in the path before retrieving the item’s attributes.

As a convenience, [`NSDictionary`](nsdictionary.md) provides a set of methods (declared as a category on [`NSDictionary`](nsdictionary.md)) for quickly and efficiently obtaining attribute information from the returned dictionary: [`fileGroupOwnerAccountName()`](nsdictionary/filegroupowneraccountname().md), [`fileModificationDate()`](nsdictionary/filemodificationdate().md), [`fileOwnerAccountName()`](nsdictionary/fileowneraccountname().md), [`filePosixPermissions()`](nsdictionary/fileposixpermissions().md), [`fileSize()`](nsdictionary/filesize().md), [`fileSystemFileNumber()`](nsdictionary/filesystemfilenumber().md), [`fileSystemNumber()`](nsdictionary/filesystemnumber().md), and [`fileType()`](nsdictionary/filetype().md).

##### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: The path of a file or directory.

## See Also

- [func componentsToDisplay(forPath: String) -> [String]?](filemanager/componentstodisplay(forpath:).md)
  Returns an array of strings representing the user-visible components of a given path.
- [func displayName(atPath: String) -> String](filemanager/displayname(atpath:).md)
  Returns the display name of the file or directory at a specified path.
- [func attributesOfFileSystem(forPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesoffilesystem(forpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](filemanager/setattributes(_:ofitematpath:).md)
  Sets the attributes of the specified file or directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/attributesofitem(atpath:))*