# isTrashed

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether an item is in the trash.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var isTrashed: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isTrashed) BOOL trashed;
```

## See Also

### Specifying Content Location
- [var parentItemIdentifier: NSFileProviderItemIdentifier](./parentitemidentifier.md)
  The persistent identifier of the item’s parent folder.
- [var symlinkTargetPath: String?](./symlinktargetpath.md)
  The target of the symlink.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/istrashed)*