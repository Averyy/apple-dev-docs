# MMSService.Configuration

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that provides information about MMS messages sent and received using the current carrier.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Instance Properties
- [var maximumImageSize: Measurement<UnitInformationStorage>?](./configuration/maximumimagesize.md)
  The maximum size of an image, in bytes, allowed for a sent group message.
- [var maximumMessageSize: Measurement<UnitInformationStorage>?](./configuration/maximummessagesize.md)
  The maximum MMS size for a sent text message.
- [var maximumRecipients: Int?](./configuration/maximumrecipients.md)
  The maximum number of recipients allowed for a sent group message.
- [var maximumSubjectSize: Measurement<UnitInformationStorage>?](./configuration/maximumsubjectsize.md)
  The maximum length of the subject allowed for a sent group message.
- [var smsSizeToBeSentAsMMSInstead: Measurement<UnitInformationStorage>?](./configuration/smssizetobesentasmmsinstead.md)
  The maximum size of an SMS message, beyond which the client needs to use MMS instead.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing MMS configuration
- [func configuration(for: CellularServiceID) async throws -> MMSService.Configuration](./configuration%28for%29.md)
  Retrieves the MMS configuration for the carrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/configuration)*