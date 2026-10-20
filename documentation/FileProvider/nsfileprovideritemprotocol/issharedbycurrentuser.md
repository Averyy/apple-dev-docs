# isSharedByCurrentUser

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item was shared by the current user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var isSharedByCurrentUser: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSharedByCurrentUser) BOOL sharedByCurrentUser;
```

## See Also

### Sharing
- [var isShared: Bool](./isshared.md)
  A Boolean value that indicates whether the item is shared with other users.
- [var mostRecentEditorNameComponents: PersonNameComponents?](./mostrecenteditornamecomponents.md)
  The most recent editor’s name.
- [var ownerNameComponents: PersonNameComponents?](./ownernamecomponents.md)
  The name of the item’s owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/issharedbycurrentuser)*