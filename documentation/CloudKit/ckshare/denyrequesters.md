# denyRequesters(_:)

**Framework**: CloudKit  
**Kind**: method

Denies share access to the specified requesters.

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
func denyRequesters(_ requesters: [CKShare.AccessRequester])
```

#### Discussion

Use this method to reject pending requests from one or more uninvited users. Denied requesters are removed from the [`requesters`](ckshare/requesters.md) array. You must save the share to the server after denying to persist the changes. Once saved, these requesters are not given access to the share, but they may attempt to request access again unless you block them. This method can only be used by the share owner or an admin. Attempting to use it as any other participant will result in an exception.

## Parameters

- `requesters`: An array of   objects to deny.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/denyrequesters(_:))*