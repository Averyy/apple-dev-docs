# MMSService.Configuration

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that provides information about MMS messages sent and received using the current carrier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(from: any Decoder) throws](mmsservice/configuration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
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
### Instance Methods
- [func encode(to: any Encoder) throws](mmsservice/configuration/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/configuration)*