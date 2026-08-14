# fileManager(_:shouldLinkItemAt:to:)

**Framework**: Foundation  
**Kind**: method

Asks the delegate if a hard link should be created between the items at the two URLs.

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
optional func fileManager(_ fileManager: FileManager, shouldLinkItemAt srcURL: URL, to dstURL: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the link should be created or [`false`](https://developer.apple.com/documentation/swift/false) if it should not be created.

#### Discussion

If the item specified by `destURL` is a directory, returning [`false`](https://developer.apple.com/documentation/swift/false) prevents links from being created to both the directory and its children.

This method performs the same task as the [`fileManager(_:shouldLinkItemAtPath:toPath:)`](filemanagerdelegate/filemanager(_:shouldlinkitematpath:topath:).md) method and is preferred over that method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that is attempting to create the link.
- `srcURL`: The URL identifying the new hard link to be created.
- `dstURL`: The URL identifying the destination of the link.

## See Also

- [func linkItem(at: URL, to: URL) throws](filemanager/linkitem(at:to:).md)
  Creates a hard link between the items at the specified URLs.
- [func linkItem(atPath: String, toPath: String) throws](filemanager/linkitem(atpath:topath:).md)
  Creates a hard link between the items at the specified paths.
- [func fileManager(FileManager, shouldLinkItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldlinkitematpath:topath:).md)
  Asks the delegate if a hard link should be created between the items at the two paths.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, linkingItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitemat:to:).md)
  Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, linkingItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitematpath:topath:).md)
  Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldlinkitemat:to:))*