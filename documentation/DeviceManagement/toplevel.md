# TopLevel

**Framework**: Device Management  
**Kind**: dictionary

The top-level payload properties you use to configure all profiles.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object TopLevel
```

## Mentions

- [Configuring Multiple Devices Using Profiles](configuring-multiple-devices-using-profiles.md)

#### Discussion

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS |
| Allow Manual Install | iOS, macOS, tvOS, watchOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | iOS, macOS |
| Allow Multiple Payloads | - |

## Topics

### Supporting Objects
- [object TopLevel.ConsentText](toplevel/consenttext-data.dictionary.md)
  The dictionary of consent agreements per language.
- [object TopLevel.ConsentText.ConsentTextItem](toplevel/consenttext-data.dictionary/consenttextitem-data.dictionary.md)
  A specific pairing of language code and consent text.
- [object TopLevel.PayloadContentItem](toplevel/payloadcontentitem.md)
  The payload-specific content for this profile.

## See Also

- [object CommonPayloadKeys](commonpayloadkeys.md)
  The payload properties that are common across all profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/toplevel)*