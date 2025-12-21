# MMSService.Configuration

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that provides information about MMS messages sent and received using the current carrier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Configuration
```

## Topics

### Instance Properties
- [var maximumImageSize: Measurement<UnitInformationStorage>?](mmsservice/configuration/maximumimagesize.md)
  The maximum size of an image, in bytes, allowed for a sent group message.
- [var maximumMessageSize: Measurement<UnitInformationStorage>?](mmsservice/configuration/maximummessagesize.md)
  The maximum MMS size for a sent text message.
- [var maximumRecipients: Int?](mmsservice/configuration/maximumrecipients.md)
  The maximum number of recipients allowed for a sent group message.
- [var maximumSubjectSize: Measurement<UnitInformationStorage>?](mmsservice/configuration/maximumsubjectsize.md)
  The maximum length of the subject allowed for a sent group message.
- [var smsSizeToBeSentAsMMSInstead: Measurement<UnitInformationStorage>?](mmsservice/configuration/smssizetobesentasmmsinstead.md)
  The maximum size of an SMS message, beyond which the client needs to use MMS instead.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func configuration(for: CellularServiceID) async throws -> MMSService.Configuration](mmsservice/configuration(for:).md)
  Retrieves the MMS configuration for the carrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/configuration)*