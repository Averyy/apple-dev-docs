# revokeMessage(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Requests revocation of an RCS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func revokeMessage(_ request: RCSService.RevokeMessageRequest) async throws -> Bool
```

#### Return Value

A Boolean value that indicates whether sending the request to the carrier network succeeded.

#### Discussion

The RCS specification requires that you revoke a message when delivery fails or times out, and fall back to sending the message with SMS or MMS.

> **Note**:  If the session is no longer valid, this method throws [`TelephonyMessagingSession.Error.invalidSession`](telephonymessagingsession/error/invalidsession.md). If the method can’t resolve the handle in the request, it throws [`RCSService.Error.invalidArgument`](rcsservice/error/invalidargument.md). If the method can’t process the revoke request for other reasons it throws [`RCSService.Error.internalError`](rcsservice/error/internalerror.md).

## Parameters

- `request`: The request that contains the message to be revoked.

## See Also

- [RCSService.RevokeMessageRequest](rcsservice/revokemessagerequest.md)
  A structure that respresents a request to revoke a previously sent message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/revokemessage(_:))*