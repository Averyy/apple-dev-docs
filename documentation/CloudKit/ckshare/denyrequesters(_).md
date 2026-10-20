# denyRequesters(_:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) denyRequesters:(NSArray<CKShareAccessRequester *> *) requesters;
```

#### Discussion

Use this method to deny pending access requests from uninvited users. CloudKit removes denied requesters from the [`requesters`](./requesters.md) array. To persist the changes, save the share to the server after calling this method.

After denial, requesters can still submit new access requests unless explicitly blocked using [`blockRequesters(_:)`](./blockrequesters%28_%29.md).

Only the share owner or an administrator can invoke this method. Attempts by other participants result in an exception.

## Parameters

- `requesters`: An array of [`CKShare.AccessRequester`](./accessrequester.md) objects to deny.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/denyrequesters(_:))*