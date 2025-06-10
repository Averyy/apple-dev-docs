# NLTokenUnit

**Framework**: Natural Language  
**Kind**: enum

Constants representing linguistic units.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum NLTokenUnit
```

#### Overview

You use these constants with these methods:

- [`availableTagSchemes(for:language:)`](nltagger/availabletagschemes(for:language:).md)
- [`tagsInRange:unit:scheme:options:tokenRanges:`](nltagger/tagsinrange:unit:scheme:options:tokenranges:.md)
- [`enumerateTagsInRange:unit:scheme:options:usingBlock:`](nltagger/enumeratetagsinrange:unit:scheme:options:usingblock:.md)

## Topics

### Constants
- [NLTokenUnit.word](nltokenunit/word.md)
  An individual word.
- [NLTokenUnit.sentence](nltokenunit/sentence.md)
  An individual sentence.
- [NLTokenUnit.paragraph](nltokenunit/paragraph.md)
  An individual paragraph.
- [NLTokenUnit.document](nltokenunit/document.md)
  The document in its entirety.
### Initializers
- [init?(rawValue: Int)](nltokenunit/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func tokenRange(at: String.Index, unit: NLTokenUnit) -> Range<String.Index>](nltagger/tokenrange(at:unit:).md)
  Returns the range of the linguistic unit containing the specified character index.
- [func tokenRange(for: Range<String.Index>, unit: NLTokenUnit) -> Range<String.Index>](nltagger/tokenrange(for:unit:).md)
  Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenunit)*