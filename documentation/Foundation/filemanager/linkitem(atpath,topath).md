# linkItem(atPath:toPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a hard link between the items at the specified paths.

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
func linkItem(atPath srcPath: String, toPath dstPath: String) throws
```

```objc
- (BOOL) linkItemAtPath:(NSString *) srcPath toPath:(NSString *) dstPath error:(NSError **) error;
```

#### Discussion

Use this method to create hard links between files in the current file system. If `srcPath` is a directory, this method creates a new directory at `dstPath` and then creates hard links for the items in that directory. If `srcPath` is (or contains) a symbolic link, the symbolic link is copied to the new location and not converted to a hard link.

Prior to linking each item, the file manager asks its delegate if it should actually create the link. It does this by calling the [`fileManager(_:shouldLinkItemAt:to:)`](../filemanagerdelegate/filemanager%28_,shouldlinkitemat,to%29.md) method; if that method is not implemented it calls the [`fileManager(_:shouldLinkItemAtPath:toPath:)`](../filemanagerdelegate/filemanager%28_,shouldlinkitematpath,topath%29.md) method instead. If the delegate method returns [`true`](../../Swift/true.md), or if the delegate does not implement the appropriate methods, the file manager creates the hard link. If there is an error linking one out of several items, the file manager may also call the delegate’s [`fileManager(_:shouldProceedAfterError:linkingItemAt:to:)`](../filemanagerdelegate/filemanager%28_,shouldproceedaftererror,linkingitemat,to%29.md) or [`fileManager(_:shouldProceedAfterError:linkingItemAtPath:toPath:)`](../filemanagerdelegate/filemanager%28_,shouldproceedaftererror,linkingitematpath,topath%29.md) method to determine how to proceed.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `srcPath`: The path that specifies the item you wish to link to. The value in this parameter must not be `nil`.
- `dstPath`: The path that identifies the location where the link will be created. The value in this parameter must not be `nil`.

## See Also

### Creating symbolic and hard links
- [func createSymbolicLink(at: URL, withDestinationURL: URL) throws](./createsymboliclink%28at,withdestinationurl%29.md)
  Creates a symbolic link at the specified URL that points to an item at the given URL.
- [func createSymbolicLink(atPath: String, withDestinationPath: String) throws](./createsymboliclink%28atpath,withdestinationpath%29.md)
  Creates a symbolic link that points to the specified destination.
- [func linkItem(at: URL, to: URL) throws](./linkitem%28at,to%29.md)
  Creates a hard link between the items at the specified URLs.
- [func destinationOfSymbolicLink(atPath: String) throws -> String](./destinationofsymboliclink%28atpath%29.md)
  Returns the path of the item pointed to by a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/linkitem(atpath:topath:))*