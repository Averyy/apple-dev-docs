# Morphology.GrammaticalGender

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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
- [Morphology.GrammaticalGender.feminine](./grammaticalgender-swift.enum/feminine.md)
  The feminine grammatical gender.
- [Morphology.GrammaticalGender.masculine](./grammaticalgender-swift.enum/masculine.md)
  The masculine grammatical gender.
- [Morphology.GrammaticalGender.neuter](./grammaticalgender-swift.enum/neuter.md)
  A value to not specify gender when inflecting a string.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Grammatical Properties
- [var isUnspecified: Bool](./isunspecified.md)
  A Boolean value that indicates whether this instance specifies no particular grammar.
- [var grammaticalGender: Morphology.GrammaticalGender?](./grammaticalgender-swift.property.md)
  The grammatical gender used for inflecting strings with this morphology.
- [var number: Morphology.GrammaticalNumber?](./number.md)
  The grammatical number used for inflecting strings with this morphology.
- [Morphology.GrammaticalNumber](./grammaticalnumber.md)
  A representation of grammatical number, used for inflecting strings.
- [var partOfSpeech: Morphology.PartOfSpeech?](./partofspeech-swift.property.md)
  The grammatical part of speech used for inflecting strings with this morphology.
- [Morphology.PartOfSpeech](./partofspeech-swift.enum.md)
  A representation of grammatical parts of speech, used for inflecting strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/grammaticalgender-swift.enum)*