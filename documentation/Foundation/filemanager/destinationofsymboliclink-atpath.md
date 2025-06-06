# destinationOfSymbolicLink(atPath:)

**Framework**: Foundation  
**Kind**: method

Returns the path of the item pointed to by a symbolic link.

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
func destinationOfSymbolicLink(atPath path: String) throws -> String
```

#### Return Value

An [`NSString`](nsstring.md) object containing the path of the directory or file to which the symbolic link `path` refers. When using Objective-C, returns `nil` upon failure. If the symbolic link is specified as a relative path, that relative path is returned.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: The path of a file or directory.

## See Also

- [func createSymbolicLink(at: URL, withDestinationURL: URL) throws](filemanager/createsymboliclink(at:withdestinationurl:).md)
  Creates a symbolic link at the specified URL that points to an item at the given URL.
- [func createSymbolicLink(atPath: String, withDestinationPath: String) throws](filemanager/createsymboliclink(atpath:withdestinationpath:).md)
  Creates a symbolic link that points to the specified destination.
- [func linkItem(at: URL, to: URL) throws](filemanager/linkitem(at:to:).md)
  Creates a hard link between the items at the specified URLs.
- [func linkItem(atPath: String, toPath: String) throws](filemanager/linkitem(atpath:topath:).md)
  Creates a hard link between the items at the specified paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/destinationofsymboliclink(atpath:))*