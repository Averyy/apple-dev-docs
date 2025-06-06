# createSymbolicLink(at:withDestinationURL:)

**Framework**: Foundation  
**Kind**: method

Creates a symbolic link at the specified URL that points to an item at the given URL.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func createSymbolicLink(at url: URL, withDestinationURL destURL: URL) throws
```

#### Discussion

This method does not traverse symbolic links contained in `destURL`, making it possible to create symbolic links to locations that do not yet exist. Also, if the final path component in `url` is a symbolic link, that link is not followed.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The file URL at which to create the new symbolic link. The last path component of the URL issued as the name of the link.
- `destURL`: The file URL that contains the item to be pointed to by the link. In other words, this is the destination of the link.

## See Also

- [func createSymbolicLink(atPath: String, withDestinationPath: String) throws](filemanager/createsymboliclink(atpath:withdestinationpath:).md)
  Creates a symbolic link that points to the specified destination.
- [func linkItem(at: URL, to: URL) throws](filemanager/linkitem(at:to:).md)
  Creates a hard link between the items at the specified URLs.
- [func linkItem(atPath: String, toPath: String) throws](filemanager/linkitem(atpath:topath:).md)
  Creates a hard link between the items at the specified paths.
- [func destinationOfSymbolicLink(atPath: String) throws -> String](filemanager/destinationofsymboliclink(atpath:).md)
  Returns the path of the item pointed to by a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/createsymboliclink(at:withdestinationurl:))*