# AttributedString.WritingDirection

**Framework**: Foundation  
**Kind**: enum

The writing direction of a piece of text.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@frozen
enum WritingDirection
```

#### Overview

Writing direction defines the base direction in which bidirectional text lays out its directional runs. A directional run is a contigous sequence of characters that all have the same effective directionality, which can be determined using the Unicode BiDi algorithm. The [`AttributedString.WritingDirection.leftToRight`](attributedstring/writingdirection/lefttoright.md) writing direction puts the directional run that is placed first in the storage leftmost, and places subsequent directional runs towards the right. The [`AttributedString.WritingDirection.rightToLeft`](attributedstring/writingdirection/righttoleft.md) writing direction puts the directional run that is placed first in the storage rightmost, and places subsequent directional runs towards the left.

Note that writing direction is a property separate from a text’s alignment, its line layout direction, or its character direction. However, it is often used to determine the default alignment of a paragraph. E.g. English (a language with `Locale/LanguageDirection-swift.enum/leftToRight` [`characterDirection`](locale/language-swift.struct/characterdirection.md)) is usually aligned to the left, but may be centered or aligned to the right for special effect, or to be visually more appealing in a user interface.

For bidirectional text to be perceived as laid out correctly, make sure that the writing direction is set to the value equivalent to the [`characterDirection`](locale/language-swift.struct/characterdirection.md) of the primary language in the text. E.g. an English sentence that contains some Arabic (a language with `Locale/LanguageDirection-swift.enum/rightToLeft` [`characterDirection`](locale/language-swift.struct/characterdirection.md)) words, should use a [`AttributedString.WritingDirection.leftToRight`](attributedstring/writingdirection/lefttoright.md) writing direction. An Arabic sentence that contains some English words, should use a [`AttributedString.WritingDirection.rightToLeft`](attributedstring/writingdirection/righttoleft.md) writing direction.

Writing direction is always orthogonoal to the line layout direction chosen to display a certain text. The line layout direction is the direction in which a sequence of lines is placed in. E.g. English text is usually displayed with a line layout direction of `Locale/LanguageDirection-swift.enum/topToBottom`. While languages do have an associated line language direction (see [`lineLayoutDirection`](locale/language-swift.struct/linelayoutdirection.md)), not all displays of text follow the line layout direction of the text’s primary language.

Horizontal script is script with a line layout direction of either `Locale/LanguageDirection-swift.enum/topToBottom` or `Locale/LanguageDirection-swift.enum/bottomToTop`. Vertical script has a `Locale/LanguageDirection-swift.enum/leftToRight` or `Locale/LanguageDirection-swift.enum/rightToLeft` line layout direction. In vertical scripts, a writing direction of [`AttributedString.WritingDirection.leftToRight`](attributedstring/writingdirection/lefttoright.md) is interpreted as top-to-bottom and a writing direction of [`AttributedString.WritingDirection.rightToLeft`](attributedstring/writingdirection/righttoleft.md) is interpreted as bottom-to-top.

## Topics

### Enumeration Cases
- [AttributedString.WritingDirection.leftToRight](attributedstring/writingdirection/lefttoright.md)
  A left-to-right writing direction in horizontal script.
- [AttributedString.WritingDirection.rightToLeft](attributedstring/writingdirection/righttoleft.md)
  A right-to-left writing direction in horizontal script.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/writingdirection)*