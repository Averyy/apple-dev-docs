# totalSize

**Framework**: TelephonyMessagingKit  
**Kind**: property

The total size of the message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var totalSize: Measurement<UnitInformationStorage> { get }
```

#### Discussion

If this value exceeds `MMSConfiguration/maximumMessageSize`, sending the message with [`sendMessage(_:)`](mmsservice/sendmessage(_:).md) fails with [`MMSService.Error.maximumSizeExceeded`](mmsservice/error/maximumsizeexceeded.md).

## See Also

- [var cellularServiceID: CellularServiceID](mmsmessage/cellularserviceid.md)
  The cellular service identifier associated with the message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [var messageID: MMSMessageID](mmsmessage/messageid.md)
  A message identifier for the message.
- [struct MMSMessageID](mmsmessageid.md)
  A structure that represents an MMS message identifier.
- [var description: String](mmsmessage/description.md)
  A textual representation of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsmessage/totalsize)*