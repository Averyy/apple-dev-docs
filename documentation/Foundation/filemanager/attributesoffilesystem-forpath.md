# attributesOfFileSystem(forPath:)

**Framework**: Foundation  
**Kind**: method

Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.

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
func attributesOfFileSystem(forPath path: String) throws -> [FileAttributeKey : Any]
```

## Mentions

- [About Apple File System](about-apple-file-system.md)

#### Return Value

A dictionary object that describes the attributes of the mounted file system on which `path` resides. See `File-System Attribute Keys` for a description of the keys available in the dictionary.

#### Discussion

This method does not traverse a terminal symbolic link.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: Any pathname within the mounted file system.

## See Also

- [func componentsToDisplay(forPath: String) -> [String]?](filemanager/componentstodisplay(forpath:).md)
  Returns an array of strings representing the user-visible components of a given path.
- [func displayName(atPath: String) -> String](filemanager/displayname(atpath:).md)
  Returns the display name of the file or directory at a specified path.
- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesofitem(atpath:).md)
  Returns the attributes of the item at a given path.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](filemanager/setattributes(_:ofitematpath:).md)
  Sets the attributes of the specified file or directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/attributesoffilesystem(forpath:))*