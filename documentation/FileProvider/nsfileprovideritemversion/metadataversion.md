# metadataVersion

**Framework**: File Provider  
**Kind**: property

An opaque object used to track versions of the item’s metadata.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var metadataVersion: Data { get }
```

#### Discussion

When the [`metadataVersion`](nsfileprovideritemversion/metadataversion.md) changes, system updates the dataless representation of the item on disk, but it doesn’t attempt to download the content.

The version data object must be no longer than 128 bytes.

## See Also

- [class var beforeFirstSyncComponent: Data](nsfileprovideritemversion/beforefirstsynccomponent.md)
  A Boolean value indicating that this version predates the version returned by the file provider extension.
- [var contentVersion: Data](nsfileprovideritemversion/contentversion.md)
  An opaque object used to track versions of the item’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemversion/metadataversion)*