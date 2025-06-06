# setAttributes(_:ofItemAtPath:)

**Framework**: Foundation  
**Kind**: method

Sets the attributes of the specified file or directory.

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
func setAttributes(_ attributes: [FileAttributeKey : Any], ofItemAtPath path: String) throws
```

#### Discussion

As in the POSIX standard, the app either must own the file or directory or must be running as superuser for attribute changes to take effect. The method attempts to make all changes specified in attributes and ignores any rejection of an attempted modification. If the last component of the path is a symbolic link, the system traverses it.

You must initialize the [`posixPermissions`](fileattributekey/posixpermissions.md) value with the code representing the POSIX file-permissions bit pattern. The system sets [`hfsCreatorCode`](fileattributekey/hfscreatorcode.md) and [`hfsTypeCode`](fileattributekey/hfstypecode.md) only when `path` specifies a file.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `attributes`: A dictionary containing as keys the attributes to set for   and as values the corresponding value for the attribute. You can set the following attributes:  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  . You can change single attributes or any combination of attributes; you need not specify keys for all attributes.
- `path`: The path of a file or directory.

## See Also

- [func componentsToDisplay(forPath: String) -> [String]?](filemanager/componentstodisplay(forpath:).md)
  Returns an array of strings representing the user-visible components of a given path.
- [func displayName(atPath: String) -> String](filemanager/displayname(atpath:).md)
  Returns the display name of the file or directory at a specified path.
- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesofitem(atpath:).md)
  Returns the attributes of the item at a given path.
- [func attributesOfFileSystem(forPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesoffilesystem(forpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/setattributes(_:ofitematpath:))*