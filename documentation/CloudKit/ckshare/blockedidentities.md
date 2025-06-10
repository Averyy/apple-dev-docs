# blockedIdentities

**Framework**: CloudKit  
**Kind**: property

A list of users blocked from requesting access to this share.

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
var blockedIdentities: [CKShare.BlockedIdentity] { get }
```

#### Discussion

Identities remain in this list until a user calls [`unblockIdentities(_:)`](ckshare/unblockidentities(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/blockedidentities)*