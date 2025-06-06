# NSAttributedString.Key

**Framework**: Foundation  
**Kind**: struct

The attributes you apply to ranges of characters in an attributed string.

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
struct Key
```

#### Discussion

The [`NSAttributedString.Key`](nsattributedstring/key.md) type defines the attributes you apply to ranges of characters in an attributed string. Some attributes provide information about how to render, lay out, or interpret the text, while other attributes provide transient or collaborative information. Attributes like the [`font`](nsattributedstring/key/font.md), [`kern`](nsattributedstring/key/kern.md), and [`strokeColor`](nsattributedstring/key/strokecolor.md) contain information that the rendering system uses to display the text. Attributes like the [`spellingState`](nsattributedstring/key/spellingstate.md), [`textHighlightStyle`](nsattributedstring/key/texthighlightstyle.md), or [`accessibilityCustomText`](nsattributedstring/key/accessibilitycustomtext.md) contain semantic information from other parts of the system. Some of these semantic attributes also affect how the system renders the text, but they are transient attributes unlike the core rendering attributes.

## Topics

### Getting rendering attribute keys
- [static let backgroundColor: NSAttributedString.Key](nsattributedstring/key/backgroundcolor.md)
  The color of the background behind the text.
- [static let baselineOffset: NSAttributedString.Key](nsattributedstring/key/baselineoffset.md)
  The vertical offset for the position of the text.
- [static let font: NSAttributedString.Key](nsattributedstring/key/font.md)
  The font of the text.
- [static let foregroundColor: NSAttributedString.Key](nsattributedstring/key/foregroundcolor.md)
  The color of the text.
- [static let glyphInfo: NSAttributedString.Key](nsattributedstring/key/glyphinfo.md)
  The name of a glyph info object.
- [static let kern: NSAttributedString.Key](nsattributedstring/key/kern.md)
  The kerning of the text.
- [static let ligature: NSAttributedString.Key](nsattributedstring/key/ligature.md)
  The ligature of the text.
- [static let paragraphStyle: NSAttributedString.Key](nsattributedstring/key/paragraphstyle.md)
  The paragraph style of the text.
- [static let strikethroughColor: NSAttributedString.Key](nsattributedstring/key/strikethroughcolor.md)
  The color of the strikethrough.
- [static let strikethroughStyle: NSAttributedString.Key](nsattributedstring/key/strikethroughstyle.md)
  The strikethrough style of the text.
- [static let strokeColor: NSAttributedString.Key](nsattributedstring/key/strokecolor.md)
  The color of the stroke.
- [static let strokeWidth: NSAttributedString.Key](nsattributedstring/key/strokewidth.md)
  The width of the stroke.
- [static let superscript: NSAttributedString.Key](nsattributedstring/key/superscript.md)
  The superscript of the text.
- [static let tracking: NSAttributedString.Key](nsattributedstring/key/tracking.md)
  The amount to modify the default tracking.
- [static let underlineColor: NSAttributedString.Key](nsattributedstring/key/underlinecolor.md)
  The color of the underline.
- [static let underlineStyle: NSAttributedString.Key](nsattributedstring/key/underlinestyle.md)
  The underline style of the text.
- [static let writingDirection: NSAttributedString.Key](nsattributedstring/key/writingdirection.md)
  The writing direction of the text.
### Getting text attribute keys
- [static let cursor: NSAttributedString.Key](nsattributedstring/key/cursor.md)
  The cursor object.
- [static let link: NSAttributedString.Key](nsattributedstring/key/link.md)
  The link for the text.
- [static let markedClauseSegment: NSAttributedString.Key](nsattributedstring/key/markedclausesegment.md)
  The index of the marked clause segment.
- [static let replacementIndex: NSAttributedString.Key](nsattributedstring/key/replacementindex.md)
  The replacement position associated with a format string specifier.
- [static let shadow: NSAttributedString.Key](nsattributedstring/key/shadow.md)
  The shadow of the text.
- [static let spellingState: NSAttributedString.Key](nsattributedstring/key/spellingstate.md)
  The spelling state of the text.
- [static let suggestionHighlight: NSAttributedString.Key](nsattributedstring/key/suggestionhighlight.md)
  A highlight associated with a Spotlight suggestion.
- [static let textAlternatives: NSAttributedString.Key](nsattributedstring/key/textalternatives.md)
  The alternatives for the text.
- [static let textEffect: NSAttributedString.Key](nsattributedstring/key/texteffect.md)
  An attribute that applies a text effect to the text.
- [static let textHighlightColorScheme: NSAttributedString.Key](nsattributedstring/key/texthighlightcolorscheme.md)
  The custom highlight color to apply to the text.
- [static let textHighlightStyle: NSAttributedString.Key](nsattributedstring/key/texthighlightstyle.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [static let textItemTag: NSAttributedString.Key](nsattributedstring/key/textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](nsattributedstring/key/tooltip.md)
  The tooltip text.
### Getting attachment attribute keys
- [static let adaptiveImageGlyph: NSAttributedString.Key](nsattributedstring/key/adaptiveimageglyph.md)
  The adaptive image glyph for the text.
- [static let attachment: NSAttributedString.Key](nsattributedstring/key/attachment.md)
  The attachment for the text.
### Getting accessibility attribute keys
- [static let accessibilityAlignment: NSAttributedString.Key](nsattributedstring/key/accessibilityalignment.md)
- [static let accessibilityAnnotationTextAttribute: NSAttributedString.Key](nsattributedstring/key/accessibilityannotationtextattribute.md)
- [static let accessibilityAttachment: NSAttributedString.Key](nsattributedstring/key/accessibilityattachment.md)
  Text attachment (`id`).
- [static let accessibilityAutocorrected: NSAttributedString.Key](nsattributedstring/key/accessibilityautocorrected.md)
  Autocorrected text (`NSNumber` as a Boolean value).
- [static let accessibilityBackgroundColor: NSAttributedString.Key](nsattributedstring/key/accessibilitybackgroundcolor.md)
  Text background color (`CGColorRef`).
- [static let accessibilityCustomText: NSAttributedString.Key](nsattributedstring/key/accessibilitycustomtext.md)
- [static let accessibilityFont: NSAttributedString.Key](nsattributedstring/key/accessibilityfont.md)
  Font keys (`NSDictionary`).
- [static let accessibilityForegroundColor: NSAttributedString.Key](nsattributedstring/key/accessibilityforegroundcolor.md)
  Text foreground color (`CGColorRef`).
- [static let accessibilityLanguage: NSAttributedString.Key](nsattributedstring/key/accessibilitylanguage.md)
- [static let accessibilityLink: NSAttributedString.Key](nsattributedstring/key/accessibilitylink.md)
  Text link (`id`).
- [static let accessibilityListItemIndex: NSAttributedString.Key](nsattributedstring/key/accessibilitylistitemindex.md)
- [static let accessibilityListItemLevel: NSAttributedString.Key](nsattributedstring/key/accessibilitylistitemlevel.md)
- [static let accessibilityListItemPrefix: NSAttributedString.Key](nsattributedstring/key/accessibilitylistitemprefix.md)
- [static let accessibilityMarkedMisspelled: NSAttributedString.Key](nsattributedstring/key/accessibilitymarkedmisspelled.md)
  Misspelled text that is visibly marked as misspelled (`NSNumber` as a Boolean value). If you’re implementing a custom text-editing app, use `NSAccessibilityMarkedMisspelledTextAttribute` to ensure that VoiceOver properly identifies misspelled text to users.
- [static let accessibilityMisspelled: NSAttributedString.Key](nsattributedstring/key/accessibilitymisspelled.md)
  Misspelled text that isn’t necessarily visibly marked as misspelled ([`NSNumber`](nsnumber.md) as a Boolean value). Beginning in macOS 10.9, VoiceOver no longer checks for this attribute; instead, VoiceOver uses [`accessibilityMarkedMisspelled`](nsattributedstring/key/accessibilitymarkedmisspelled.md).
- [static let accessibilityShadow: NSAttributedString.Key](nsattributedstring/key/accessibilityshadow.md)
  Text shadow (`NSNumber` as a Boolean value).
- [static let accessibilitySpeechAnnouncementPriority: NSAttributedString.Key](nsattributedstring/key/accessibilityspeechannouncementpriority.md)
- [static let accessibilitySpeechIPANotation: NSAttributedString.Key](nsattributedstring/key/accessibilityspeechipanotation.md)
  A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [static let accessibilitySpeechLanguage: NSAttributedString.Key](nsattributedstring/key/accessibilityspeechlanguage.md)
  A key that indicates the language to use when speaking a string.
- [static let accessibilitySpeechPitch: NSAttributedString.Key](nsattributedstring/key/accessibilityspeechpitch.md)
  A key that indicates the pitch to apply to spoken content.
- [static let accessibilitySpeechPunctuation: NSAttributedString.Key](nsattributedstring/key/accessibilityspeechpunctuation.md)
  A key that indicates whether to speak punctuation.
- [static let accessibilitySpeechQueueAnnouncement: NSAttributedString.Key](nsattributedstring/key/accessibilityspeechqueueannouncement.md)
  A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [static let accessibilitySpeechSpellOut: NSAttributedString.Key](nsattributedstring/key/accessibilityspeechspellout.md)
- [static let accessibilityTextCustom: NSAttributedString.Key](nsattributedstring/key/accessibilitytextcustom.md)
  A key for specifying custom attributes to apply to the text.
- [static let accessibilityTextHeadingLevel: NSAttributedString.Key](nsattributedstring/key/accessibilitytextheadinglevel.md)
  A key for specifying the heading level of the text.
- [static let accessibilityStrikethrough: NSAttributedString.Key](nsattributedstring/key/accessibilitystrikethrough.md)
  Text strikethrough (`NSNumber` as a Boolean value).
- [static let accessibilityStrikethroughColor: NSAttributedString.Key](nsattributedstring/key/accessibilitystrikethroughcolor.md)
  Text strikethrough color (`CGColorRef`).
- [static let accessibilitySuperscript: NSAttributedString.Key](nsattributedstring/key/accessibilitysuperscript.md)
  Text superscript style (`NSNumber`). Values > 0 are superscript; values < 0 are subscript.
- [static let accessibilityUnderline: NSAttributedString.Key](nsattributedstring/key/accessibilityunderline.md)
  Text underline style (`NSNumber`).
- [static let accessibilityUnderlineColor: NSAttributedString.Key](nsattributedstring/key/accessibilityunderlinecolor.md)
  Text underline color (`CGColorRef`).
- [static let UIAccessibilityTextAttributeContext: NSAttributedString.Key](nsattributedstring/key/uiaccessibilitytextattributecontext.md)
### Getting Markdown attribute keys
- [static let inlinePresentationIntent: NSAttributedString.Key](nsattributedstring/key/inlinepresentationintent.md)
  An attribute that provides details for an inline Markdown element.
- [static let presentationIntentAttributeName: NSAttributedString.Key](nsattributedstring/key/presentationintentattributename.md)
  An attribute that provides details for a block-level Markdown element.
- [static let markdownSourcePosition: NSAttributedString.Key](nsattributedstring/key/markdownsourceposition.md)
  The position in a Markdown source string corresponding to some attributed text.
- [static let alternateDescription: NSAttributedString.Key](nsattributedstring/key/alternatedescription.md)
  An alternate description for a URL or image.
- [static let imageURL: NSAttributedString.Key](nsattributedstring/key/imageurl.md)
  The URL for an image in Markdown text.
### Getting translation-related attribute keys
- [static let languageIdentifier: NSAttributedString.Key](nsattributedstring/key/languageidentifier.md)
  The language identifier associated with the range of text.
- [static let morphology: NSAttributedString.Key](nsattributedstring/key/morphology.md)
  An attribute that contains grammatical properties to apply to the text.
- [static let inflectionRule: NSAttributedString.Key](nsattributedstring/key/inflectionrule.md)
  An attribute that tells the system how to apply grammar rules and other modifiers to the range of text.
- [static let inflectionAlternative: NSAttributedString.Key](nsattributedstring/key/inflectionalternative.md)
  The alternative translation for a string when no suitable inflection exists.
- [static let agreeWithArgument: NSAttributedString.Key](nsattributedstring/key/agreewithargument.md)
- [static let agreeWithConcept: NSAttributedString.Key](nsattributedstring/key/agreewithconcept.md)
- [static let referentConcept: NSAttributedString.Key](nsattributedstring/key/referentconcept.md)
- [static let localizedNumberFormat: NSAttributedString.Key](nsattributedstring/key/localizednumberformat.md)
### Deprecated Keys
- [static let expansion: NSAttributedString.Key](nsattributedstring/key/expansion.md)
  The expansion factor of the text.
- [static let obliqueness: NSAttributedString.Key](nsattributedstring/key/obliqueness.md)
  The obliqueness of the text.
- [static let verticalGlyphForm: NSAttributedString.Key](nsattributedstring/key/verticalglyphform.md)
  The vertical glyph form of the text.
- [static let characterShapeAttributeName: NSAttributedString.Key](nsattributedstring/key/charactershapeattributename.md)
  The character shape attribute.
- [static let usesScreenFontsDocumentAttribute: NSAttributedString.Key](nsattributedstring/key/usesscreenfontsdocumentattribute.md)
  The screen fonts attribute.
### Initializers
- [init(String)](nsattributedstring/key/init(_:).md)
  Creates an attributed string key.
- [init(rawValue: String)](nsattributedstring/key/init(rawvalue:).md)
  Creates an attributed string key with the specified raw value.
### Type Properties
- [static let writingToolsExclusionAttributeName: NSAttributedString.Key](nsattributedstring/key/writingtoolsexclusionattributename.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSAttributedString.TextHighlightStyle](nsattributedstring/texthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSAttributedString.TextEffectStyle](nsattributedstring/texteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSAttributedString.SpellingState](nsattributedstring/spellingstate.md)
  Constants for the spelling state attribute key.
- [struct NSUnderlineStyle](../UIKit/NSUnderlineStyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](../UIKit/NSWritingDirectionFormatType.md)
  Constants for the writing direction attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key)*