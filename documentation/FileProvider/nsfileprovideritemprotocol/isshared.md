# isShared

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item is shared with other users.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var isShared: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isShared) BOOL shared;
```

## See Also

### Sharing
- [var isSharedByCurrentUser: Bool](./issharedbycurrentuser.md)
  A Boolean value that indicates whether the item was shared by the current user.
- [var mostRecentEditorNameComponents: PersonNameComponents?](./mostrecenteditornamecomponents.md)
  The most recent editor’s name.
- [var ownerNameComponents: PersonNameComponents?](./ownernamecomponents.md)
  The name of the item’s owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/isshared)*