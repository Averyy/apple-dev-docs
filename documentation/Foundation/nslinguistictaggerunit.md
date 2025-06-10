# NSLinguisticTaggerUnit

**Framework**: Foundation  
**Kind**: enum

Constants representing linguistic units.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum NSLinguisticTaggerUnit
```

#### Overview

You use these constants with the [`availableTagSchemes(for:language:)`](nslinguistictagger/availabletagschemes(for:language:).md) method as well as the [`tag(for:at:unit:scheme:orthography:tokenRange:)`](nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:).md),  [`tags(in:unit:scheme:options:tokenRanges:)`](nslinguistictagger/tags(in:unit:scheme:options:tokenranges:).md), and [`enumerateTags(in:unit:scheme:options:using:)`](nslinguistictagger/enumeratetags(in:unit:scheme:options:using:).md) methods.

## Topics

### Constants
- [NSLinguisticTaggerUnit.document](nslinguistictaggerunit/document.md)
  The document in its entirety.
- [NSLinguisticTaggerUnit.paragraph](nslinguistictaggerunit/paragraph.md)
  An individual paragraph.
- [NSLinguisticTaggerUnit.sentence](nslinguistictaggerunit/sentence.md)
  An individual sentence.
- [NSLinguisticTaggerUnit.word](nslinguistictaggerunit/word.md)
  An individual word.
### Initializers
- [init?(rawValue: Int)](nslinguistictaggerunit/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NSLinguisticTagScheme](nslinguistictagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.
- [struct NSLinguisticTag](nslinguistictag.md)
  A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictaggerunit)*