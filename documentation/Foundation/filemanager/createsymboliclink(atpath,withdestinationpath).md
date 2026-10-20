# createSymbolicLink(atPath:withDestinationPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a symbolic link that points to the specified destination.

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
func createSymbolicLink(atPath path: String, withDestinationPath destPath: String) throws
```

```objc
- (BOOL) createSymbolicLinkAtPath:(NSString *) path withDestinationPath:(NSString *) destPath error:(NSError **) error;
```

#### Discussion

This method does not traverse symbolic links contained in `destPath`, making it possible to create symbolic links to locations that do not yet exist. Also, if the final path component in `path` is a symbolic link, that link is not followed.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: The path at which to create the new symbolic link. The last path component is used as the name of the link.
- `destPath`: The path that contains the item to be pointed to by the link. In other words, this is the destination of the link.

## See Also

### Related Documentation
- [func removeItem(atPath: String) throws](./removeitem%28atpath%29.md)
  Removes the file or directory at the specified path.
### Creating symbolic and hard links
- [func createSymbolicLink(at: URL, withDestinationURL: URL) throws](./createsymboliclink%28at,withdestinationurl%29.md)
  Creates a symbolic link at the specified URL that points to an item at the given URL.
- [func linkItem(at: URL, to: URL) throws](./linkitem%28at,to%29.md)
  Creates a hard link between the items at the specified URLs.
- [func linkItem(atPath: String, toPath: String) throws](./linkitem%28atpath,topath%29.md)
  Creates a hard link between the items at the specified paths.
- [func destinationOfSymbolicLink(atPath: String) throws -> String](./destinationofsymboliclink%28atpath%29.md)
  Returns the path of the item pointed to by a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/createsymboliclink(atpath:withdestinationpath:))*