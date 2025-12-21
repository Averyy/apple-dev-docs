# removeItem(at:)

**Framework**: Foundation  
**Kind**: method

Removes the file or directory at the specified URL.

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
func removeItem(at URL: URL) throws
```

#### Discussion

Prior to removing each item, the file manager asks its delegate if it should actually do so. It does this by calling the [`fileManager(_:shouldRemoveItemAt:)`](filemanagerdelegate/filemanager(_:shouldremoveitemat:).md) method; if that method is not implemented (or the process is running in OS X 10.5 or earlier) it calls the [`fileManager(_:shouldRemoveItemAtPath:)`](filemanagerdelegate/filemanager(_:shouldremoveitematpath:).md) method instead. If the delegate method returns [`true`](https://developer.apple.com/documentation/Swift/true), or if the delegate does not implement the appropriate methods, the file manager proceeds to remove the file or directory. If there is an error removing an item, the file manager may also call the delegate’s [`fileManager(_:shouldProceedAfterError:removingItemAt:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitemat:).md) or [`fileManager(_:shouldProceedAfterError:removingItemAtPath:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitematpath:).md) method to determine how to proceed.

Removing an item also removes all old versions of that item, invalidating any URLs returned by the [`url(forPublishingUbiquitousItemAt:expiration:)`](filemanager/url(forpublishingubiquitousitemat:expiration:).md) method to old versions.

## Parameters

- `URL`: A file URL specifying the file or directory to remove. If the URL specifies a directory, the contents of that directory are recursively removed. You may specify   for this parameter in Objective-C.

## See Also

- [func createDirectory(at: URL, withIntermediateDirectories: Bool, attributes: [FileAttributeKey : Any]?) throws](filemanager/createdirectory(at:withintermediatedirectories:attributes:).md)
  Creates a directory with the given attributes at the specified URL.
- [func createDirectory(atPath: String, withIntermediateDirectories: Bool, attributes: [FileAttributeKey : Any]?) throws](filemanager/createdirectory(atpath:withintermediatedirectories:attributes:).md)
  Creates a directory with given attributes at the specified path.
- [func createFile(atPath: String, contents: Data?, attributes: [FileAttributeKey : Any]?) -> Bool](filemanager/createfile(atpath:contents:attributes:).md)
  Creates a file with the specified content and attributes at the given location.
- [func removeItem(atPath: String) throws](filemanager/removeitem(atpath:).md)
  Removes the file or directory at the specified path.
- [func trashItem(at: URL, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws](filemanager/trashitem(at:resultingitemurl:).md)
  Moves an item to the trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/removeitem(at:))*