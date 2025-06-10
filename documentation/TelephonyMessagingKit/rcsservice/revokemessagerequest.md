# RCSService.RevokeMessageRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that respresents a request to revoke a previously sent message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct RevokeMessageRequest
```

## Topics

### Creating a revoke request
- [init(cellularServiceID: CellularServiceID, handle: RCSHandle, messageID: RCSMessageID)](rcsservice/revokemessagerequest/init(cellularserviceid:handle:messageid:).md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](rcsservice/revokemessagerequest/cellularserviceid.md)
  The service identifier to use for this request.
- [var handle: RCSHandle](rcsservice/revokemessagerequest/handle.md)
  A handle associated with the message to revoke.
- [var messageID: RCSMessageID](rcsservice/revokemessagerequest/messageid.md)
  The message identifier to revoke.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func revokeMessage(RCSService.RevokeMessageRequest) async throws -> Bool](rcsservice/revokemessage(_:).md)
  Requests revocation of an RCS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/revokemessagerequest)*