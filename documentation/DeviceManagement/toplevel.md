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
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | NA |

## Topics

### Objects
- [object TopLevel.ConsentText](toplevel/consenttext-data.dictionary.md)
  The dictionary of consent agreements per language.
- [object TopLevel.PayloadContentItem](toplevel/payloadcontentitem.md)
  The payload-specific content for this profile.

## See Also

- [object CommonPayloadKeys](commonpayloadkeys.md)
  The payload properties that are common across all profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/toplevel)*