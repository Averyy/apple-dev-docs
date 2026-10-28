# destinationOfSymbolicLink(atPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) destinationOfSymbolicLinkAtPath:(NSString *) path error:(NSError **) error;
```

## Return Value

An [`NSString`](../nsstring.md) object containing the path of the directory or file to which the symbolic link `path` refers. When using Objective-C, returns `nil` upon failure. If the symbolic link is specified as a relative path, that relative path is returned.

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: The path of a file or directory.

## See Also

### Creating symbolic and hard links
- [func createSymbolicLink(at: URL, withDestinationURL: URL) throws](./createsymboliclink%28at,withdestinationurl%29.md)
  Creates a symbolic link at the specified URL that points to an item at the given URL.
- [func createSymbolicLink(atPath: String, withDestinationPath: String) throws](./createsymboliclink%28atpath,withdestinationpath%29.md)
  Creates a symbolic link that points to the specified destination.
- [func linkItem(at: URL, to: URL) throws](./linkitem%28at,to%29.md)
  Creates a hard link between the items at the specified URLs.
- [func linkItem(atPath: String, toPath: String) throws](./linkitem%28atpath,topath%29.md)
  Creates a hard link between the items at the specified paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/destinationofsymboliclink(atpath:))*