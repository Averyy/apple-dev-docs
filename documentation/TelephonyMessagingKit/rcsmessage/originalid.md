# originalID

**Framework**: TelephonyMessagingKit  
**Kind**: property

The original message ID of this message.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
let originalID: RCSMessageID?
```

#### Discussion

A non-nil value indicates that this message was re-sent.

## See Also

- [let cellularServiceID: CellularServiceID](rcsmessage/cellularserviceid.md)
  The cellular service identifier associated with the message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let handle: RCSHandle](rcsmessage/handle.md)
  The handle associated with the sender or receiver of the message.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [let id: RCSMessageID](rcsmessage/id.md)
  A message identifier for the message.
- [struct RCSMessageID](rcsmessageid.md)
  A structure that represents an RCS message identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/originalid)*