# directoryEntryCount

**Framework**: Foundation  
**Kind**: property

The count of file system objects in the directory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var directoryEntryCount: Int? { get }
```

#### Discussion

This value is a count of objects that are actually in the file system, so it excludes virtual items like “`.`” and “`..`”. This property is useful for quickly identifying an empty directory for backup and syncing. If the URL isn’t a directory, or the file system can’t cheaply compute the value, the value is `nil`.

Not all file systems can provide this information.

## See Also

- [var isDirectory: Bool?](urlresourcevalues/isdirectory.md)
  A Boolean value that indicates whether the resource is a directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/directoryentrycount)*