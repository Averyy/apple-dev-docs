# Morphology.GrammaticalGender

**Framework**: Foundation  
**Kind**: enum

A representation of grammatical gender, used for inflecting strings.

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
enum GrammaticalGender
```

## Topics

### Determining Grammatical Gender
- [Morphology.GrammaticalGender.feminine](morphology/grammaticalgender-swift.enum/feminine.md)
  The feminine grammatical gender.
- [Morphology.GrammaticalGender.masculine](morphology/grammaticalgender-swift.enum/masculine.md)
  The masculine grammatical gender.
- [Morphology.GrammaticalGender.neuter](morphology/grammaticalgender-swift.enum/neuter.md)
  A value to not specify gender when inflecting a string.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isUnspecified: Bool](morphology/isunspecified.md)
  A Boolean value that indicates whether this instance specifies no particular grammar.
- [var grammaticalGender: Morphology.GrammaticalGender?](morphology/grammaticalgender-swift.property.md)
  The grammatical gender used for inflecting strings with this morphology.
- [var number: Morphology.GrammaticalNumber?](morphology/number.md)
  The grammatical number used for inflecting strings with this morphology.
- [Morphology.GrammaticalNumber](morphology/grammaticalnumber.md)
  A representation of grammatical number, used for inflecting strings.
- [var partOfSpeech: Morphology.PartOfSpeech?](morphology/partofspeech-swift.property.md)
  The grammatical part of speech used for inflecting strings with this morphology.
- [Morphology.PartOfSpeech](morphology/partofspeech-swift.enum.md)
  A representation of grammatical parts of speech, used for inflecting strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/grammaticalgender-swift.enum)*