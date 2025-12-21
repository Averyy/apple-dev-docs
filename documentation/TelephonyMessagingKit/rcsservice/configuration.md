# RCSService.Configuration

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains RCS configuration parameters, such as timing and size limits.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Configuration
```

## Topics

### Inspecting message configuration
- [var maximumTextMessageSize: Measurement<UnitInformationStorage>?](rcsservice/configuration/maximumtextmessagesize.md)
  The maximum size of a text chat message that a person can enter in a 1-to-1 chat or group chat session.
### Inspecting file transfer configuration
- [var maximumFileTransferSize: Measurement<UnitInformationStorage>?](rcsservice/configuration/maximumfiletransfersize.md)
  The maximum size of a file that the RCS file transfer service can send.
- [let fileTransferWarningSize: Measurement<UnitInformationStorage>?](rcsservice/configuration/filetransferwarningsize.md)
  The size for issuing a warning about file transfers and Rich Card media objects.
### Inspecting chat configuration
- [let chatRevokeTimeout: Duration?](rcsservice/configuration/chatrevoketimeout.md)
  The maximum duration the service provider allows for delivery notification before it revokes a chat message.
- [var maximumGroupSize: Int?](rcsservice/configuration/maximumgroupsize.md)
  The maximum number of participants allowed for a group chat.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func configuration(for: CellularServiceID) throws -> RCSService.Configuration](rcsservice/configuration(for:).md)
  Retrieves the RCS configuration for the specified cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration)*