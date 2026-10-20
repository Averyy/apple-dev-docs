# RCSService.Configuration

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that contains RCS configuration parameters, such as timing and size limits.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Inspecting message configuration
- [var maximumTextMessageSize: Measurement<UnitInformationStorage>?](./configuration/maximumtextmessagesize.md)
  The maximum size of a text chat message that a person can enter in a 1-to-1 chat or group chat session.
### Inspecting file transfer configuration
- [var maximumFileTransferSize: Measurement<UnitInformationStorage>?](./configuration/maximumfiletransfersize.md)
  The maximum size of a file that the RCS file transfer service can send.
- [let fileTransferWarningSize: Measurement<UnitInformationStorage>?](./configuration/filetransferwarningsize.md)
  The size for issuing a warning about file transfers and Rich Card media objects.
### Inspecting chat configuration
- [let chatRevokeTimeout: Duration?](./configuration/chatrevoketimeout.md)
  The maximum duration the service provider allows for delivery notification before it revokes a chat message.
- [var maximumGroupSize: Int?](./configuration/maximumgroupsize.md)
  The maximum number of participants allowed for a group chat.
### Supporting RCS encryption
- [let supportsEndToEndEncryption: Bool](./configuration/supportsendtoendencryption.md)
  A Boolean value indicating whether the RCS service supports end-to-end encryption.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing RCS configuration
- [func configuration(for: CellularServiceID) throws -> RCSService.Configuration](./configuration%28for%29.md)
  Retrieves the RCS configuration for the specified cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration)*