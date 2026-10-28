# NLTokenUnit

**Framework**: Natural Language  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NLTokenUnit : NSInteger;
```

## Overview

You use these constants with these methods:

- [`availableTagSchemes(for:language:)`](./nltagger/availabletagschemes%28for,language%29.md)
- [`tagsInRange:unit:scheme:options:tokenRanges:`](./nltagger/tagsinrange_unit_scheme_options_tokenranges_.md)
- [`enumerateTagsInRange:unit:scheme:options:usingBlock:`](./nltagger/enumeratetagsinrange_unit_scheme_options_usingblock_.md)

## Topics

### Constants
- [NLTokenUnit.word](./nltokenunit/word.md)
  An individual word.
- [NLTokenUnit.sentence](./nltokenunit/sentence.md)
  An individual sentence.
- [NLTokenUnit.paragraph](./nltokenunit/paragraph.md)
  An individual paragraph.
- [NLTokenUnit.document](./nltokenunit/document.md)
  The document in its entirety.
### Initializers
- [init?(rawValue: Int)](./nltokenunit/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining the range of a unit token
- [func tokenRange(at: String.Index, unit: NLTokenUnit) -> Range<String.Index>](./nltagger/tokenrange%28at,unit%29.md)
  Returns the range of the linguistic unit containing the specified character index.
- [func tokenRange(for: Range<String.Index>, unit: NLTokenUnit) -> Range<String.Index>](./nltagger/tokenrange%28for,unit%29.md)
  Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.
- [- tokenRangeAtIndex:unit:](./nltagger/tokenrangeatindex_unit_.md)
  Returns the range of the linguistic unit containing the specified character index.
- [- tokenRangeForRange:unit:](./nltagger/tokenrangeforrange_unit_.md)
  Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenunit)*