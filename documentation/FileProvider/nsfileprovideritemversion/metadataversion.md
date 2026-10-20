# metadataVersion

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

An opaque object used to track versions of the item’s metadata.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var metadataVersion: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * metadataVersion;
```

#### Discussion

When the [`metadataVersion`](./metadataversion.md) changes, system updates the dataless representation of the item on disk, but it doesn’t attempt to download the content.

The version data object must be no longer than 128 bytes.

## See Also

### Accessing Version Data
- [class var beforeFirstSyncComponent: Data](./beforefirstsynccomponent.md)
  A Boolean value indicating that this version predates the version returned by the file provider extension.
- [var contentVersion: Data](./contentversion.md)
  An opaque object used to track versions of the item’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemversion/metadataversion)*