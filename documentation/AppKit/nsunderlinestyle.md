# NSUnderlineStyle

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants for the underline style and strikethrough style attribute keys.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct NSUnderlineStyle
```

```c
enum NSUnderlineStyle : NSInteger;
```

#### Overview

Use these constants to specify the [`NSUnderlineStyleAttributeName`](./nsunderlinestyleattributename.md) and [`NSStrikethroughStyleAttributeName`](./nsstrikethroughstyleattributename.md) attributes of an attributed string.

## Topics

### Getting the line style
- [static var single: NSUnderlineStyle](./nsunderlinestyle/single.md)
  Draw a single line.
- [static var thick: NSUnderlineStyle](./nsunderlinestyle/thick.md)
  Draw a thick line.
- [static var double: NSUnderlineStyle](./nsunderlinestyle/double.md)
  Draw a double line.
- [static var patternDot: NSUnderlineStyle](./nsunderlinestyle/patterndot.md)
  Draw a line of dots.
- [static var patternDash: NSUnderlineStyle](./nsunderlinestyle/patterndash.md)
  Draw a line of dashes.
- [static var patternDashDot: NSUnderlineStyle](./nsunderlinestyle/patterndashdot.md)
  Draw a line of alternating dashes and dots.
- [static var patternDashDotDot: NSUnderlineStyle](./nsunderlinestyle/patterndashdotdot.md)
  Draw a line of alternating dashes and two dots.
- [static var byWord: NSUnderlineStyle](./nsunderlinestyle/byword.md)
  Draw the line only beneath or through words, not whitespace.
- [NSUnderlineStyleNone](./nsunderlinestyle/nsunderlinestylenone.md)
  Don’t draw a line.
- [NSUnderlineStylePatternSolid](./nsunderlinestyle/nsunderlinestylepatternsolid.md)
  Draw a solid line.
### Deprecated
- [init(rawValue: Int)](./nsunderlinestyle/init%28rawvalue%29.md)
- [init(Text.LineStyle)](./nsunderlinestyle/init%28_%29.md)
  Creates a [`NSUnderlineStyle`](./nsunderlinestyle.md) from `Text.LineStyle`.
- [Deprecated symbols](./nsunderlinestyle-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Hashable](../Swift/hashable.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Getting text content attributes
- [enum NSWritingDirectionFormatType](./nswritingdirectionformattype.md)
  Constants for the writing direction attribute key.
- [TextKit string attribute keys](./textkit-string-attribute-keys.md)
  AppKit-specific keys you use to apply attributes to ranges of characters in an attributed string.
- [NSTextHighlightStyle](./nstexthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSTextHighlightColorScheme](./nstexthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSTextEffectStyle](./nstexteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSSpellingState](./nsspellingstate.md)
  Constants for the spelling state attribute key.
- [NSUnderlineByWordMask](./nsunderlinebywordmask.md)
  Draw the underline only underneath words, not underneath whitespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsunderlinestyle)*