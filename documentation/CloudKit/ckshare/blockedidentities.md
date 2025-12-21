# blockedIdentities

**Framework**: CloudKit  
**Kind**: property

A list of users blocked from requesting access to this share.

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
var blockedIdentities: [CKShare.BlockedIdentity] { get }
```

#### Discussion

Identities remain in this list until an owner or administrator calls [`unblockIdentities(_:)`](ckshare/unblockidentities(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/blockedidentities)*