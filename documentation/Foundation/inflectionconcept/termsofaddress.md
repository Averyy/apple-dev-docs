# InflectionConcept.termsOfAddress(_:)

**Framework**: Foundation  
**Kind**: case

Indicates that the system uses the associated terms of address for grammatical agreement when localizing text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case termsOfAddress([TermOfAddress])
```

#### Discussion

When inflecting text the first term of address which can be used in the target language is the one used for pronoun substitution and grammar agreement.

## Parameters

- `[TermOfAddress]`: A list of preferred terms of address for localizing text.

## See Also

- [InflectionConcept.localizedPhrase(_:)](inflectionconcept/localizedphrase(_:).md)
  Indicates that the system uses the associated string for grammatical agreement when localizing text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inflectionconcept/termsofaddress(_:))*