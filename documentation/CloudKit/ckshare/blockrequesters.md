# blockRequesters(_:)

**Framework**: CloudKit  
**Kind**: method

Blocks the specified requesters from requesting access to this share.

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
func blockRequesters(_ requesters: [CKShare.AccessRequester])
```

#### Discussion

This method permanently prevents the listed requesters from requesting access to the share in the future. Blocked requesters appear in the [`blockedIdentities`](ckshare/blockedidentities.md) array. The share must be saved to the server after blocking to persist the changes. This method can only be used by the share owner or an admin. Attempting to use it as any other participant will result in an exception. Blocking an existing participant removes the participant from the share.

## Parameters

- `requesters`: An array of   objects to block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/blockrequesters(_:))*