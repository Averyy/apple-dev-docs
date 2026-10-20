# RCSService.RevokeMessageRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that respresents a request to revoke a previously sent message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct RevokeMessageRequest
```

## Topics

### Creating a revoke request
- [init(cellularServiceID: CellularServiceID, handle: RCSHandle, messageID: RCSMessageID)](./revokemessagerequest/init%28cellularserviceid,handle,messageid%29.md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](./revokemessagerequest/cellularserviceid.md)
  The service identifier to use for this request.
- [var handle: RCSHandle](./revokemessagerequest/handle.md)
  A handle associated with the message to revoke.
- [var messageID: RCSMessageID](./revokemessagerequest/messageid.md)
  The message identifier to revoke.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Revoking messages
- [func revokeMessage(RCSService.RevokeMessageRequest) async throws -> Bool](./revokemessage%28_%29.md)
  Requests revocation of an RCS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/revokemessagerequest)*