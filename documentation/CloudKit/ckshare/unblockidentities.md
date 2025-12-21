# unblockIdentities(_:)

**Framework**: CloudKit  
**Kind**: method

Unblocks previously blocked users, allowing them to request access again.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func unblockIdentities(_ blockedIdentities: [CKShare.BlockedIdentity])
```

#### Discussion

Use this method to remove specified identities from the [`blockedIdentities`](ckshare/blockedidentities.md) array. Unblocked identities can request access again if access requests are enabled.

To persist this change, save the share to the server after calling this method.

Only the share owner or an administrator can invoke this method. Attempts by other participants result in an exception.

## Parameters

- `blockedIdentities`: An array of   objects to unblock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/unblockidentities(_:))*