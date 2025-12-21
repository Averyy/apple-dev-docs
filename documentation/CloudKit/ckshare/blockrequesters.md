# blockRequesters(_:)

**Framework**: CloudKit  
**Kind**: method

Blocks specified users from requesting access to this share.

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
func blockRequesters(_ requesters: [CKShare.AccessRequester])
```

#### Discussion

Blocking prevents users from submitting future access requests and removes existing participants from the share. Blocked requesters appear in the [`blockedIdentities`](ckshare/blockedidentities.md) array.

To persist this change, save the share to the server after calling this method.

Only the share owner or an administrator can invoke this method. Attempts by other participants result in an exception.

## Parameters

- `requesters`: An array of   objects to block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/blockrequesters(_:))*