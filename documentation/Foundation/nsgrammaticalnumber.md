# NSGrammaticalNumber

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
enum NSGrammaticalNumber
```

```c
enum NSGrammaticalNumber : NSInteger;
```

## Topics

### Determining Grammatical Number
- [NSGrammaticalNumber.zero](./nsgrammaticalnumber/zero.md)
  Zero persons or things, as used for a grammatical number.
- [NSGrammaticalNumber.singular](./nsgrammaticalnumber/singular.md)
  A single person or thing, as used for a grammatical number.
- [NSGrammaticalNumber.plural](./nsgrammaticalnumber/plural.md)
  Multiple persons or things, as used for a grammatical number.
- [NSGrammaticalNumber.pluralTwo](./nsgrammaticalnumber/pluraltwo.md)
  Two persons or things, as used for a grammatical number.
- [NSGrammaticalNumber.pluralFew](./nsgrammaticalnumber/pluralfew.md)
  A small number of persons or things, as used for a grammatical number.
- [NSGrammaticalNumber.pluralMany](./nsgrammaticalnumber/pluralmany.md)
  A large number of persons or things, as used for a grammatical number.
- [NSGrammaticalNumber.notSet](./nsgrammaticalnumber/notset.md)
  A value that indicates the number is unset.
### Initializers
- [init?(rawValue: Int)](./nsgrammaticalnumber/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Grammatical Properties
- [enum NSGrammaticalGender](./nsgrammaticalgender.md)
  A representation of grammatical gender, used for inflecting strings.
- [enum NSGrammaticalPartOfSpeech](./nsgrammaticalpartofspeech.md)
  A representation of grammatical parts of speech, used for inflecting strings.
- [unspecified](./nsmorphology/unspecified.md)
  A Boolean value that indicates whether this instance specifies no particular grammar.
- [grammaticalGender](./nsmorphology/grammaticalgender.md)
  The grammatical gender used for inflecting strings with this morphology.
- [number](./nsmorphology/number.md)
  The grammatical number used for inflecting strings with this morphology.
- [partOfSpeech](./nsmorphology/partofspeech.md)
  The grammatical part of speech used for inflecting strings with this morphology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgrammaticalnumber)*