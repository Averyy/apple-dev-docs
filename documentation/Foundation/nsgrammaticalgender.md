# NSGrammaticalGender

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
enum NSGrammaticalGender
```

```c
enum NSGrammaticalGender : NSInteger;
```

## Topics

### Determining Grammatical Gender
- [NSGrammaticalGender.feminine](./nsgrammaticalgender/feminine.md)
  The feminine grammatical gender.
- [NSGrammaticalGender.masculine](./nsgrammaticalgender/masculine.md)
  The masculine grammatical gender.
- [NSGrammaticalGender.neuter](./nsgrammaticalgender/neuter.md)
  A value to not specify gender when inflecting a string.
- [NSGrammaticalGender.notSet](./nsgrammaticalgender/notset.md)
  A value that indicates the gender is unset.
### Initializers
- [init?(rawValue: Int)](./nsgrammaticalgender/init%28rawvalue%29.md)

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
- [enum NSGrammaticalNumber](./nsgrammaticalnumber.md)
  A representation of grammatical number, used for inflecting strings.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgrammaticalgender)*