# TextKit string attribute keys

**Framework**: AppKit  
**Role**: API Collection

AppKit-specific keys you use to apply attributes to ranges of characters in an attributed string.

## Overview

AppKit defines these attribute keys you use to specify attribute values in [`NSAttributedString`](../Foundation/nsattributedstring.md) and [`NSMutableAttributedString`](../Foundation/nsmutableattributedstring.md).

## Topics

### Getting rendering attribute keys
- [NSBackgroundColorAttributeName](./nsbackgroundcolorattributename.md)
  The color of the background behind the text.
- [NSBaselineOffsetAttributeName](./nsbaselineoffsetattributename.md)
  The vertical offset for the position of the text.
- [NSFontAttributeName](./nsfontattributename.md)
  The font of the text.
- [NSForegroundColorAttributeName](./nsforegroundcolorattributename.md)
  The color of the text.
- [NSGlyphInfoAttributeName](./nsglyphinfoattributename.md)
  The name of a glyph info object.
- [NSKernAttributeName](./nskernattributename.md)
  The kerning of the text.
- [NSLigatureAttributeName](./nsligatureattributename.md)
  The ligature of the text.
- [NSParagraphStyleAttributeName](./nsparagraphstyleattributename.md)
  The paragraph style of the text.
- [NSStrikethroughColorAttributeName](./nsstrikethroughcolorattributename.md)
  The color of the strikethrough.
- [NSStrikethroughStyleAttributeName](./nsstrikethroughstyleattributename.md)
  The strikethrough style of the text.
- [NSStrokeColorAttributeName](./nsstrokecolorattributename.md)
  The color of the stroke.
- [NSStrokeWidthAttributeName](./nsstrokewidthattributename.md)
  The width of the stroke.
- [NSSuperscriptAttributeName](./nssuperscriptattributename.md)
  The superscript of the text.
- [NSTrackingAttributeName](./nstrackingattributename.md)
  The amount to modify the default tracking.
- [NSUnderlineColorAttributeName](./nsunderlinecolorattributename.md)
  The color of the underline.
- [NSUnderlineStyleAttributeName](./nsunderlinestyleattributename.md)
  The underline style of the text.
- [NSWritingDirectionAttributeName](./nswritingdirectionattributename.md)
  The writing direction of the text.
### Getting text attribute keys
- [NSCursorAttributeName](./nscursorattributename.md)
  The cursor object.
- [NSLinkAttributeName](./nslinkattributename.md)
  The link for the text.
- [NSMarkedClauseSegmentAttributeName](./nsmarkedclausesegmentattributename.md)
  The index of the marked clause segment.
- [NSShadowAttributeName](./nsshadowattributename.md)
  The shadow of the text.
- [NSSpellingStateAttributeName](./nsspellingstateattributename.md)
  The spelling state of the text.
- [NSTextAlternativesAttributeName](./nstextalternativesattributename.md)
  The alternatives for the text.
- [NSTextEffectAttributeName](./nstexteffectattributename.md)
  An attribute that applies a text effect to the text.
- [NSTextHighlightColorSchemeAttributeName](./nstexthighlightcolorschemeattributename.md)
  The custom highlight color to apply to the text.
- [NSTextHighlightStyleAttributeName](./nstexthighlightstyleattributename.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [NSToolTipAttributeName](./nstooltipattributename.md)
  The tooltip text.
### Getting attachment attribute keys
- [NSAdaptiveImageGlyphAttributeName](./nsadaptiveimageglyphattributename.md)
  The adaptive image glyph for the text.
- [NSAttachmentAttributeName](./nsattachmentattributename.md)
  The attachment for the text.
### Getting accessibility attribute keys
- [NSAccessibilityAnnotationTextAttribute](./nsaccessibilityannotationtextattribute.md)
- [NSAccessibilityAutocorrectedTextAttribute](./nsaccessibilityautocorrectedtextattribute.md)
  Autocorrected text (`NSNumber` as a Boolean value).
- [NSAccessibilityBackgroundColorTextAttribute](./nsaccessibilitybackgroundcolortextattribute.md)
  Text background color (`CGColorRef`).
- [NSAccessibilityCustomTextAttribute](./nsaccessibilitycustomtextattribute.md)
- [NSAccessibilityFontBoldAttribute](./nsaccessibilityfontboldattribute.md)
- [NSAccessibilityFontItalicAttribute](./nsaccessibilityfontitalicattribute.md)
- [NSAccessibilityFontTextAttribute](./nsaccessibilityfonttextattribute.md)
  Font keys (`NSDictionary`).
- [NSAccessibilityForegroundColorTextAttribute](./nsaccessibilityforegroundcolortextattribute.md)
  Text foreground color (`CGColorRef`).
- [NSAccessibilityLanguageTextAttribute](./nsaccessibilitylanguagetextattribute.md)
- [NSAccessibilityLinkTextAttribute](./nsaccessibilitylinktextattribute.md)
  Text link (`id`).
- [NSAccessibilityListItemIndexTextAttribute](./nsaccessibilitylistitemindextextattribute.md)
- [NSAccessibilityListItemLevelTextAttribute](./nsaccessibilitylistitemleveltextattribute.md)
- [NSAccessibilityListItemPrefixTextAttribute](./nsaccessibilitylistitemprefixtextattribute.md)
- [NSAccessibilityMarkedMisspelledTextAttribute](./nsaccessibilitymarkedmisspelledtextattribute.md)
  Misspelled text that is visibly marked as misspelled (`NSNumber` as a Boolean value). If you’re implementing a custom text-editing app, use `NSAccessibilityMarkedMisspelledTextAttribute` to ensure that VoiceOver properly identifies misspelled text to users.
- [NSAccessibilityMisspelledTextAttribute](./nsaccessibilitymisspelledtextattribute.md)
  Misspelled text that isn’t necessarily visibly marked as misspelled (`NSNumber` as a Boolean value).
- [NSAccessibilityShadowTextAttribute](./nsaccessibilityshadowtextattribute.md)
  Text shadow (`NSNumber` as a Boolean value).
- [NSAccessibilityStrikethroughTextAttribute](./nsaccessibilitystrikethroughtextattribute.md)
  Text strikethrough (`NSNumber` as a Boolean value).
- [NSAccessibilityStrikethroughColorTextAttribute](./nsaccessibilitystrikethroughcolortextattribute.md)
  Text strikethrough color (`CGColorRef`).
- [NSAccessibilitySuperscriptTextAttribute](./nsaccessibilitysuperscripttextattribute.md)
  Text superscript style (`NSNumber`). Values > 0 are superscript; values < 0 are subscript.
- [NSAccessibilityTextAlignmentAttribute](./nsaccessibilitytextalignmentattribute.md)
- [let NSAccessibilityTextCompletionAttribute: String](./nsaccessibilitytextcompletionattribute.md)
- [NSAccessibilityUnderlineTextAttribute](./nsaccessibilityunderlinetextattribute.md)
  Text underline style (`NSNumber`).
- [NSAccessibilityUnderlineColorTextAttribute](./nsaccessibilityunderlinecolortextattribute.md)
  Text underline color (`CGColorRef`).
### Writing Tools keys
- [NSWritingToolsExclusionAttributeName](./nswritingtoolsexclusionattributename.md)
### Deprecated
- [NSAccessibilityAttachmentTextAttribute](./nsaccessibilityattachmenttextattribute.md)
  Text attachment (`id`).
- [NSExpansionAttributeName](./nsexpansionattributename.md)
  The expansion factor of the text.
- [NSObliquenessAttributeName](./nsobliquenessattributename.md)
  The obliqueness of the text.
- [NSVerticalGlyphFormAttributeName](./nsverticalglyphformattributename.md)
  The vertical glyph form of the text.
- [NSCharacterShapeAttributeName](./nscharactershapeattributename.md)
  The character shape attribute.
- [NSUsesScreenFontsDocumentAttribute](./nsusesscreenfontsdocumentattribute.md)
  The screen fonts attribute.

## See Also

### Getting text content attributes
- [NSTextHighlightStyle](./nstexthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSTextHighlightColorScheme](./nstexthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSTextEffectStyle](./nstexteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSSpellingState](./nsspellingstate.md)
  Constants for the spelling state attribute key.
- [struct NSUnderlineStyle](./nsunderlinestyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](./nswritingdirectionformattype.md)
  Constants for the writing direction attribute key.
- [NSUnderlineByWordMask](./nsunderlinebywordmask.md)
  Draw the underline only underneath words, not underneath whitespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/textkit-string-attribute-keys)*