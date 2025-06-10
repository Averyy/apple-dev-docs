# unblockIdentities(_:)

**Framework**: CloudKit  
**Kind**: method

Unblocks previously blocked identities, allowing them to request access again.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func unblockIdentities(_ blockedIdentities: [CKShare.BlockedIdentity])
```

#### Discussion

Call this method to remove the specified identities from the [`blockedIdentities`](ckshare/blockedidentities.md) array. Once unblocked, those identities are free to request access to the share unless access requests are disabled. You must save the share to commit this change to the server. This method can only be used by the share owner or an admin. Attempting to use it as any other participant will result in an exception.

## Parameters

- `blockedIdentities`: An array of   objects to unblock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/unblockidentities(_:))*