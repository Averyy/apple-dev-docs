# Morphology.GrammaticalNumber

**Framework**: Foundation  
**Kind**: enum

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
- [Morphology.GrammaticalNumber.zero](morphology/grammaticalnumber/zero.md)
  Zero persons or things, as used for a gramnatical number.
- [Morphology.GrammaticalNumber.singular](morphology/grammaticalnumber/singular.md)
  A single person or thing, as used for a grammatical number.
- [Morphology.GrammaticalNumber.plural](morphology/grammaticalnumber/plural.md)
  Multiple persons or things, as used for a grammatical number.
- [Morphology.GrammaticalNumber.pluralTwo](morphology/grammaticalnumber/pluraltwo.md)
  Two persons or things, as used for a grammatical number.
- [Morphology.GrammaticalNumber.pluralFew](morphology/grammaticalnumber/pluralfew.md)
  A small number of persons or things, as used for a grammatical number.
- [Morphology.GrammaticalNumber.pluralMany](morphology/grammaticalnumber/pluralmany.md)
  A large number of persons or things, as used for a grammatical number.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isUnspecified: Bool](morphology/isunspecified.md)
  A Boolean value that indicates whether this instance specifies no particular grammar.
- [var grammaticalGender: Morphology.GrammaticalGender?](morphology/grammaticalgender-swift.property.md)
  The grammatical gender used for inflecting strings with this morphology.
- [Morphology.GrammaticalGender](morphology/grammaticalgender-swift.enum.md)
  A representation of grammatical gender, used for inflecting strings.
- [var number: Morphology.GrammaticalNumber?](morphology/number.md)
  The grammatical number used for inflecting strings with this morphology.
- [var partOfSpeech: Morphology.PartOfSpeech?](morphology/partofspeech-swift.property.md)
  The grammatical part of speech used for inflecting strings with this morphology.
- [Morphology.PartOfSpeech](morphology/partofspeech-swift.enum.md)
  A representation of grammatical parts of speech, used for inflecting strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/grammaticalnumber)*