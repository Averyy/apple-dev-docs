# denyRequesters(_:)

**Framework**: CloudKit  
**Kind**: method

Denies access requests from specified users.

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
func denyRequesters(_ requesters: [CKShare.AccessRequester])
```

#### Discussion

Use this method to deny pending access requests from uninvited users. Denied requesters are removed from the [`requesters`](ckshare/requesters.md) array. To persist the changes, save the share to the server after calling this method.

After denial, requesters can still submit new access requests unless explicitly blocked using [`blockRequesters(_:)`](ckshare/blockrequesters(_:).md).

Only the share owner or an administrator can invoke this method. Attempts by other participants result in an exception.

## Parameters

- `requesters`: An array of   objects to deny.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/denyrequesters(_:))*