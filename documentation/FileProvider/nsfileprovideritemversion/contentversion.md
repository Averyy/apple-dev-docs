# contentVersion

**Framework**: File Provider  
**Kind**: property

An opaque object used to track versions of the item’s content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var contentVersion: Data { get }
```

#### Discussion

If the system stores a local copy of an item’s content, it downloads a new copy when the [`contentVersion`](nsfileprovideritemversion/contentversion.md) changes. The content version also invalidates the system’s thumbnail cache.

The system considers the file’s resource fork part of the file’s content. The version changes when either the data fork or the resource fork changes.

The version data object must be no longer than 128 bytes.

## See Also

- [class var beforeFirstSyncComponent: Data](nsfileprovideritemversion/beforefirstsynccomponent.md)
  A Boolean value indicating that this version predates the version returned by the file provider extension.
- [var metadataVersion: Data](nsfileprovideritemversion/metadataversion.md)
  An opaque object used to track versions of the item’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemversion/contentversion)*