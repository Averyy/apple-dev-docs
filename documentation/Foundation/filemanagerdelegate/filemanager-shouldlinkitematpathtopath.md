# fileManager(_:shouldLinkItemAtPath:toPath:)

**Framework**: Foundation  
**Kind**: method

Asks the delegate if a hard link should be created between the items at the two paths.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func fileManager(_ fileManager: FileManager, shouldLinkItemAtPath srcPath: String, toPath dstPath: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the operation should proceed, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the item specified by `destURL` is a directory, returning [`false`](https://developer.apple.com/documentation/Swift/false) prevents links from being created to both the directory and its children.

This method performs the same task as the [`fileManager(_:shouldLinkItemAt:to:)`](filemanagerdelegate/filemanager(_:shouldlinkitemat:to:).md) method, which is preferred over this method in macOS 10.6 and later.

## Parameters

- `fileManager`: The file manager object that is attempting to create the link.
- `srcPath`: The path or a file or directory that   is about to attempt to link.
- `dstPath`: The path or a file or directory to which   is about to attempt to link.

## See Also

- [func linkItem(at: URL, to: URL) throws](filemanager/linkitem(at:to:).md)
  Creates a hard link between the items at the specified URLs.
- [func linkItem(atPath: String, toPath: String) throws](filemanager/linkitem(atpath:topath:).md)
  Creates a hard link between the items at the specified paths.
- [func fileManager(FileManager, shouldLinkItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldlinkitemat:to:).md)
  Asks the delegate if a hard link should be created between the items at the two URLs.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, linkingItemAt: URL, to: URL) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitemat:to:).md)
  Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified URL.
- [func fileManager(FileManager, shouldProceedAfterError: any Error, linkingItemAtPath: String, toPath: String) -> Bool](filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitematpath:topath:).md)
  Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldlinkitematpath:topath:))*