# NSLocale.LanguageDirection

**Framework**: Foundation  
**Kind**: enum

The directions that a language may take across a page of text.

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
enum LanguageDirection
```

#### Overview

Use these constants with the methods [`lineDirection(forLanguage:)`](nslocale/linedirection(forlanguage:).md) and [`characterDirection(forLanguage:)`](nslocale/characterdirection(forlanguage:).md).

## Topics

### Constants
- [NSLocale.LanguageDirection.unknown](nslocale/languagedirection/unknown.md)
  The direction of the language is unknown.
- [NSLocale.LanguageDirection.leftToRight](nslocale/languagedirection/lefttoright.md)
  The language direction is from left to right.
- [NSLocale.LanguageDirection.rightToLeft](nslocale/languagedirection/righttoleft.md)
  The language direction is from right to left.
- [NSLocale.LanguageDirection.topToBottom](nslocale/languagedirection/toptobottom.md)
  The language direction is from top to bottom.
- [NSLocale.LanguageDirection.bottomToTop](nslocale/languagedirection/bottomtotop.md)
  The language direction is from bottom to top.
- [NSLocale.LanguageDirection.unknown](nslocale/languagedirection/unknown.md)
  The direction of the language is unknown.
- [NSLocale.LanguageDirection.leftToRight](nslocale/languagedirection/lefttoright.md)
  The language direction is from left to right.
- [NSLocale.LanguageDirection.rightToLeft](nslocale/languagedirection/righttoleft.md)
  The language direction is from right to left.
- [NSLocale.LanguageDirection.topToBottom](nslocale/languagedirection/toptobottom.md)
  The language direction is from top to bottom.
- [NSLocale.LanguageDirection.bottomToTop](nslocale/languagedirection/bottomtotop.md)
  The language direction is from bottom to top.
### Initializers
- [init?(rawValue: UInt)](nslocale/languagedirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func characterDirection(forLanguage: String) -> Locale.LanguageDirection](locale/characterdirection(forlanguage:).md)
  Returns the character direction for a specified language code.
- [static func lineDirection(forLanguage: String) -> Locale.LanguageDirection](locale/linedirection(forlanguage:).md)
  Returns the line direction for a specified language code.
- [typealias LanguageDirection](locale/languagedirection.md)
  An alias for the standard set of language directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/languagedirection)*