# TopLevel.ConsentText

**Framework**: Device Management  
**Kind**: dictionary

The dictionary of consent agreements per language.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
object TopLevel.ConsentText
```

## Topics

### Objects
- [object TopLevel.ConsentText.ConsentTextItem](toplevel/consenttext-data.dictionary/consenttextitem-data.dictionary.md)
  A specific pairing of language code and consent text.

## Properties

- `ConsentTextItem` (TopLevel.ConsentText.ConsentTextItem) *(required)*: The dictionary containing a key that consists of the IETF BCP 47 identifier for a language (for example, en or jp) and a value that consists of the agreement localized to that language.

## See Also

- [object TopLevel.PayloadContentItem](toplevel/payloadcontentitem.md)
  The payload-specific content for this profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/toplevel/consenttext-data.dictionary)*