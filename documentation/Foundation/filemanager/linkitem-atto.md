# linkItem(at:to:)

**Framework**: Foundation  
**Kind**: method

Creates a hard link between the items at the specified URLs.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func linkItem(at srcURL: URL, to dstURL: URL) throws
```

#### Discussion

Use this method to create hard links between files in the current file system. If `srcURL` is a directory, this method creates a new directory at `dstURL` and then creates hard links for the items in that directory. If `srcURL` is (or contains) a symbolic link, the symbolic link is copied and not converted to a hard link at `dstURL`.

Prior to linking each item, the file manager asks its delegate if it should actually create the link. It does this by calling the [`fileManager(_:shouldLinkItemAt:to:)`](filemanagerdelegate/filemanager(_:shouldlinkitemat:to:).md) method; if that method is not implemented it calls the [`fileManager(_:shouldLinkItemAtPath:toPath:)`](filemanagerdelegate/filemanager(_:shouldlinkitematpath:topath:).md) method instead. If the delegate method returns [`true`](https://developer.apple.com/documentation/swift/true), or if the delegate does not implement the appropriate methods, the file manager creates the hard link. If there is an error linking one out of several items, the file manager may also call the delegate’s [`fileManager(_:shouldProceedAfterError:linkingItemAt:to:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitemat:to:).md) or [`fileManager(_:shouldProceedAfterError:linkingItemAtPath:toPath:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitematpath:topath:).md) method to determine how to proceed.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `srcURL`: The file URL that identifies the source of the link. The URL in this parameter must not be a file reference URL; it must specify the actual path to the item. The value in this parameter must not be  .
- `dstURL`: The file URL that specifies where you want to create the hard link. The URL in this parameter must not be a file reference URL; it must specify the actual path to the item. The value in this parameter must not be  .

## See Also

- [func createSymbolicLink(at: URL, withDestinationURL: URL) throws](filemanager/createsymboliclink(at:withdestinationurl:).md)
  Creates a symbolic link at the specified URL that points to an item at the given URL.
- [func createSymbolicLink(atPath: String, withDestinationPath: String) throws](filemanager/createsymboliclink(atpath:withdestinationpath:).md)
  Creates a symbolic link that points to the specified destination.
- [func linkItem(atPath: String, toPath: String) throws](filemanager/linkitem(atpath:topath:).md)
  Creates a hard link between the items at the specified paths.
- [func destinationOfSymbolicLink(atPath: String) throws -> String](filemanager/destinationofsymboliclink(atpath:).md)
  Returns the path of the item pointed to by a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/linkitem(at:to:))*