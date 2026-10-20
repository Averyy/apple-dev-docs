# parentItemIdentifier

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The persistent identifier of the item’s parent folder.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var parentItemIdentifier: NSFileProviderItemIdentifier { get }
```

```objc
@property (nonatomic, copy, readonly) NSFileProviderItemIdentifier parentItemIdentifier;
```

## Mentions

- [Synchronizing the File Provider Extension](../synchronizing-the-file-provider-extension.md)

## See Also

### Specifying Content Location
- [var isTrashed: Bool](./istrashed.md)
  A Boolean value that indicates whether an item is in the trash.
- [var symlinkTargetPath: String?](./symlinktargetpath.md)
  The target of the symlink.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/parentitemidentifier)*