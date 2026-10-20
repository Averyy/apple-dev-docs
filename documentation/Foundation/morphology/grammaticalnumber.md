# Morphology.GrammaticalNumber

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A representation of grammatical number, used for inflecting strings.

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
enum GrammaticalNumber
```

## Topics

### Determining Grammatical Number
- [Morphology.GrammaticalNumber.zero](./grammaticalnumber/zero.md)
  Zero persons or things, as used for a gramnatical number.
- [Morphology.GrammaticalNumber.singular](./grammaticalnumber/singular.md)
  A single person or thing, as used for a grammatical number.
- [Morphology.GrammaticalNumber.plural](./grammaticalnumber/plural.md)
  Multiple persons or things, as used for a grammatical number.
- [Morphology.GrammaticalNumber.pluralTwo](./grammaticalnumber/pluraltwo.md)
  Two persons or things, as used for a grammatical number.
- [Morphology.GrammaticalNumber.pluralFew](./grammaticalnumber/pluralfew.md)
  A small number of persons or things, as used for a grammatical number.
- [Morphology.GrammaticalNumber.pluralMany](./grammaticalnumber/pluralmany.md)
  A large number of persons or things, as used for a grammatical number.

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
- [Morphology.GrammaticalGender](./grammaticalgender-swift.enum.md)
  A representation of grammatical gender, used for inflecting strings.
- [var number: Morphology.GrammaticalNumber?](./number.md)
  The grammatical number used for inflecting strings with this morphology.
- [var partOfSpeech: Morphology.PartOfSpeech?](./partofspeech-swift.property.md)
  The grammatical part of speech used for inflecting strings with this morphology.
- [Morphology.PartOfSpeech](./partofspeech-swift.enum.md)
  A representation of grammatical parts of speech, used for inflecting strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/grammaticalnumber)*