# symlinkTargetPath

**Framework**: File Provider  
**Kind**: property

The target of the symlink.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var symlinkTargetPath: String? { get }
```

#### Discussion

If the extension contains an item with a [`typeIdentifier`](nsfileprovideritemprotocol/typeidentifier.md) of `public.symlink` (`kUTTypeSymLink`), this property contains the symlink’s target. Otherwise, it’s `nil`.

## See Also

- [var parentItemIdentifier: NSFileProviderItemIdentifier](nsfileprovideritemprotocol/parentitemidentifier.md)
  The persistent identifier of the item’s parent folder.
- [var isTrashed: Bool](nsfileprovideritemprotocol/istrashed.md)
  A Boolean value that indicates whether an item is in the trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/symlinktargetpath)*