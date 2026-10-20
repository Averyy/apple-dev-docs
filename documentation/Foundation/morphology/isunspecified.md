# isUnspecified

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this instance specifies no particular grammar.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var isUnspecified: Bool { get }
```

#### Discussion

This value is equivalent to having set none of the properties in this [`Morphology`](../morphology.md). This occurs when the user hasn’t specified preferences, or chose not to share them with this app. When the morphology is unspecified, inflecting a string with this morphology does nothing.

## See Also

### Accessing Grammatical Properties
- [var grammaticalGender: Morphology.GrammaticalGender?](./grammaticalgender-swift.property.md)
  The grammatical gender used for inflecting strings with this morphology.
- [Morphology.GrammaticalGender](./grammaticalgender-swift.enum.md)
  A representation of grammatical gender, used for inflecting strings.
- [var number: Morphology.GrammaticalNumber?](./number.md)
  The grammatical number used for inflecting strings with this morphology.
- [Morphology.GrammaticalNumber](./grammaticalnumber.md)
  A representation of grammatical number, used for inflecting strings.
- [var partOfSpeech: Morphology.PartOfSpeech?](./partofspeech-swift.property.md)
  The grammatical part of speech used for inflecting strings with this morphology.
- [Morphology.PartOfSpeech](./partofspeech-swift.enum.md)
  A representation of grammatical parts of speech, used for inflecting strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/isunspecified)*