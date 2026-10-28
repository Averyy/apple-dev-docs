# NSLocale.LanguageDirection

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSLocaleLanguageDirection : NSUInteger;
```

## Overview

Use these constants with the methods [`lineDirection(forLanguage:)`](./linedirection%28forlanguage%29.md) and [`characterDirection(forLanguage:)`](./characterdirection%28forlanguage%29.md).

## Topics

### Constants
- [NSLocale.LanguageDirection.unknown](./languagedirection/unknown.md)
  The direction of the language is unknown.
- [NSLocale.LanguageDirection.leftToRight](./languagedirection/lefttoright.md)
  The language direction is from left to right.
- [NSLocale.LanguageDirection.rightToLeft](./languagedirection/righttoleft.md)
  The language direction is from right to left.
- [NSLocale.LanguageDirection.topToBottom](./languagedirection/toptobottom.md)
  The language direction is from top to bottom.
- [NSLocale.LanguageDirection.bottomToTop](./languagedirection/bottomtotop.md)
  The language direction is from bottom to top.
### Initializers
- [init?(rawValue: UInt)](./languagedirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting line and character direction for a language
- [static func characterDirection(forLanguage: String) -> Locale.LanguageDirection](../locale/characterdirection%28forlanguage%29.md)
  Returns the character direction for a specified language code.
- [static func lineDirection(forLanguage: String) -> Locale.LanguageDirection](../locale/linedirection%28forlanguage%29.md)
  Returns the line direction for a specified language code.
- [typealias LanguageDirection](../locale/languagedirection.md)
  An alias for the standard set of language directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/languagedirection)*