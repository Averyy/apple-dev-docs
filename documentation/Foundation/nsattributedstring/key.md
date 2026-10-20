# NSAttributedString.Key

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * NSAttributedStringKey;
```

#### Discussion

The [`NSAttributedString.Key`](./key.md) type defines the attributes you apply to ranges of characters in an attributed string. Some attributes provide information about how to render, lay out, or interpret the text, while other attributes provide transient or collaborative information. Attributes like the [`font`](./key/font.md), [`kern`](./key/kern.md), and [`strokeColor`](./key/strokecolor.md) contain information that the rendering system uses to display the text. Attributes like the [`spellingState`](./key/spellingstate.md), [`textHighlightStyle`](./key/texthighlightstyle.md), or [`accessibilityCustomText`](./key/accessibilitycustomtext.md) contain semantic information from other parts of the system. Some of these semantic attributes also affect how the system renders the text, but they are transient attributes unlike the core rendering attributes.

## Topics

### Getting rendering attribute keys
- [static let backgroundColor: NSAttributedString.Key](./key/backgroundcolor.md)
  The color of the background behind the text.
- [static let baselineOffset: NSAttributedString.Key](./key/baselineoffset.md)
  The vertical offset for the position of the text.
- [static let font: NSAttributedString.Key](./key/font.md)
  The font of the text.
- [static let foregroundColor: NSAttributedString.Key](./key/foregroundcolor.md)
  The color of the text.
- [static let glyphInfo: NSAttributedString.Key](./key/glyphinfo.md)
  The name of a glyph info object.
- [static let kern: NSAttributedString.Key](./key/kern.md)
  The kerning of the text.
- [static let ligature: NSAttributedString.Key](./key/ligature.md)
  The ligature of the text.
- [static let paragraphStyle: NSAttributedString.Key](./key/paragraphstyle.md)
  The paragraph style of the text.
- [static let strikethroughColor: NSAttributedString.Key](./key/strikethroughcolor.md)
  The color of the strikethrough.
- [static let strikethroughStyle: NSAttributedString.Key](./key/strikethroughstyle.md)
  The strikethrough style of the text.
- [static let strokeColor: NSAttributedString.Key](./key/strokecolor.md)
  The color of the stroke.
- [static let strokeWidth: NSAttributedString.Key](./key/strokewidth.md)
  The width of the stroke.
- [static let superscript: NSAttributedString.Key](./key/superscript.md)
  The superscript of the text.
- [static let tracking: NSAttributedString.Key](./key/tracking.md)
  The amount to modify the default tracking.
- [static let underlineColor: NSAttributedString.Key](./key/underlinecolor.md)
  The color of the underline.
- [static let underlineStyle: NSAttributedString.Key](./key/underlinestyle.md)
  The underline style of the text.
- [static let writingDirection: NSAttributedString.Key](./key/writingdirection.md)
  The writing direction of the text.
### Getting text attribute keys
- [static let cursor: NSAttributedString.Key](./key/cursor.md)
  The cursor object.
- [static let link: NSAttributedString.Key](./key/link.md)
  The link for the text.
- [static let markedClauseSegment: NSAttributedString.Key](./key/markedclausesegment.md)
  The index of the marked clause segment.
- [static let replacementIndex: NSAttributedString.Key](./key/replacementindex.md)
  The replacement position associated with a format string specifier.
- [static let shadow: NSAttributedString.Key](./key/shadow.md)
  The shadow of the text.
- [static let spellingState: NSAttributedString.Key](./key/spellingstate.md)
  The spelling state of the text.
- [static let suggestionHighlight: NSAttributedString.Key](./key/suggestionhighlight.md)
  A highlight associated with a Spotlight suggestion.
- [static let textAlternatives: NSAttributedString.Key](./key/textalternatives.md)
  The alternatives for the text.
- [static let textEffect: NSAttributedString.Key](./key/texteffect.md)
  An attribute that applies a text effect to the text.
- [static let textHighlightColorScheme: NSAttributedString.Key](./key/texthighlightcolorscheme.md)
  The custom highlight color to apply to the text.
- [static let textHighlightStyle: NSAttributedString.Key](./key/texthighlightstyle.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [static let textItemTag: NSAttributedString.Key](./key/textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](./key/tooltip.md)
  The tooltip text.
### Getting attachment attribute keys
- [static let adaptiveImageGlyph: NSAttributedString.Key](./key/adaptiveimageglyph.md)
  The adaptive image glyph for the text.
- [static let attachment: NSAttributedString.Key](./key/attachment.md)
  The attachment for the text.
### Getting accessibility attribute keys
- [static let accessibilityAlignment: NSAttributedString.Key](./key/accessibilityalignment.md)
- [static let accessibilityAnnotationTextAttribute: NSAttributedString.Key](./key/accessibilityannotationtextattribute.md)
- [static let accessibilityAttachment: NSAttributedString.Key](./key/accessibilityattachment.md)
  Text attachment (`id`).
- [static let accessibilityAutocorrected: NSAttributedString.Key](./key/accessibilityautocorrected.md)
  Autocorrected text (`NSNumber` as a Boolean value).
- [static let accessibilityBackgroundColor: NSAttributedString.Key](./key/accessibilitybackgroundcolor.md)
  Text background color (`CGColorRef`).
- [static let accessibilityCustomText: NSAttributedString.Key](./key/accessibilitycustomtext.md)
- [static let accessibilityFont: NSAttributedString.Key](./key/accessibilityfont.md)
  Font keys (`NSDictionary`).
- [static let accessibilityFontBoldAttribute: NSAttributedString.Key](./key/accessibilityfontboldattribute.md)
- [static let accessibilityFontItalicAttribute: NSAttributedString.Key](./key/accessibilityfontitalicattribute.md)
- [static let accessibilityForegroundColor: NSAttributedString.Key](./key/accessibilityforegroundcolor.md)
  Text foreground color (`CGColorRef`).
- [static let accessibilityLanguage: NSAttributedString.Key](./key/accessibilitylanguage.md)
- [static let accessibilityLink: NSAttributedString.Key](./key/accessibilitylink.md)
  Text link (`id`).
- [static let accessibilityListItemIndex: NSAttributedString.Key](./key/accessibilitylistitemindex.md)
- [static let accessibilityListItemLevel: NSAttributedString.Key](./key/accessibilitylistitemlevel.md)
- [static let accessibilityListItemPrefix: NSAttributedString.Key](./key/accessibilitylistitemprefix.md)
- [static let accessibilityMarkedMisspelled: NSAttributedString.Key](./key/accessibilitymarkedmisspelled.md)
  Misspelled text that is visibly marked as misspelled (`NSNumber` as a Boolean value). If you’re implementing a custom text-editing app, use `NSAccessibilityMarkedMisspelledTextAttribute` to ensure that VoiceOver properly identifies misspelled text to users.
- [static let accessibilityMisspelled: NSAttributedString.Key](./key/accessibilitymisspelled.md)
  Misspelled text that isn’t necessarily visibly marked as misspelled ([`NSNumber`](../nsnumber.md) as a Boolean value). Beginning in macOS 10.9, VoiceOver no longer checks for this attribute; instead, VoiceOver uses [`accessibilityMarkedMisspelled`](./key/accessibilitymarkedmisspelled.md).
- [static let accessibilityShadow: NSAttributedString.Key](./key/accessibilityshadow.md)
  Text shadow (`NSNumber` as a Boolean value).
- [static let accessibilitySpeechAnnouncementPriority: NSAttributedString.Key](./key/accessibilityspeechannouncementpriority.md)
- [static let accessibilitySpeechIPANotation: NSAttributedString.Key](./key/accessibilityspeechipanotation.md)
  A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [static let accessibilitySpeechLanguage: NSAttributedString.Key](./key/accessibilityspeechlanguage.md)
  A key that indicates the language to use when speaking a string.
- [static let accessibilitySpeechPitch: NSAttributedString.Key](./key/accessibilityspeechpitch.md)
  A key that indicates the pitch to apply to spoken content.
- [static let accessibilitySpeechPunctuation: NSAttributedString.Key](./key/accessibilityspeechpunctuation.md)
  A key that indicates whether to speak punctuation.
- [static let accessibilitySpeechQueueAnnouncement: NSAttributedString.Key](./key/accessibilityspeechqueueannouncement.md)
  A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [static let accessibilitySpeechSpellOut: NSAttributedString.Key](./key/accessibilityspeechspellout.md)
- [static let accessibilityTextCustom: NSAttributedString.Key](./key/accessibilitytextcustom.md)
  A key for specifying custom attributes to apply to the text.
- [static let accessibilityTextHeadingLevel: NSAttributedString.Key](./key/accessibilitytextheadinglevel.md)
  A key for specifying the heading level of the text.
- [static let accessibilityStrikethrough: NSAttributedString.Key](./key/accessibilitystrikethrough.md)
  Text strikethrough (`NSNumber` as a Boolean value).
- [static let accessibilityStrikethroughColor: NSAttributedString.Key](./key/accessibilitystrikethroughcolor.md)
  Text strikethrough color (`CGColorRef`).
- [static let accessibilitySuperscript: NSAttributedString.Key](./key/accessibilitysuperscript.md)
  Text superscript style (`NSNumber`). Values > 0 are superscript; values < 0 are subscript.
- [static let accessibilityUnderline: NSAttributedString.Key](./key/accessibilityunderline.md)
  Text underline style (`NSNumber`).
- [static let accessibilityUnderlineColor: NSAttributedString.Key](./key/accessibilityunderlinecolor.md)
  Text underline color (`CGColorRef`).
- [static let UIAccessibilityTextAttributeContext: NSAttributedString.Key](./key/uiaccessibilitytextattributecontext.md)
### Getting Markdown attribute keys
- [static let inlinePresentationIntent: NSAttributedString.Key](./key/inlinepresentationintent.md)
  An attribute that provides details for an inline Markdown element.
- [static let presentationIntentAttributeName: NSAttributedString.Key](./key/presentationintentattributename.md)
  An attribute that provides details for a block-level Markdown element.
- [static let markdownSourcePosition: NSAttributedString.Key](./key/markdownsourceposition.md)
  The position in a Markdown source string corresponding to some attributed text.
- [static let alternateDescription: NSAttributedString.Key](./key/alternatedescription.md)
  An alternate description for a URL or image.
- [static let imageURL: NSAttributedString.Key](./key/imageurl.md)
  The URL for an image in Markdown text.
### Getting translation-related attribute keys
- [static let languageIdentifier: NSAttributedString.Key](./key/languageidentifier.md)
  The language identifier associated with the range of text.
- [static let morphology: NSAttributedString.Key](./key/morphology.md)
  An attribute that contains grammatical properties to apply to the text.
- [static let inflectionRule: NSAttributedString.Key](./key/inflectionrule.md)
  An attribute that tells the system how to apply grammar rules and other modifiers to the range of text.
- [static let inflectionAlternative: NSAttributedString.Key](./key/inflectionalternative.md)
  The alternative translation for a string when no suitable inflection exists.
- [static let agreeWithArgument: NSAttributedString.Key](./key/agreewithargument.md)
  An attribute key whose value indicates inflection agreement with a specific argument.
- [static let agreeWithConcept: NSAttributedString.Key](./key/agreewithconcept.md)
  An attribute key whose value indicates inflection agreement with a specific concept.
- [static let referentConcept: NSAttributedString.Key](./key/referentconcept.md)
  An attribute key whose value indicates the referent concept for inflection.
- [static let localizedNumberFormat: NSAttributedString.Key](./key/localizednumberformat.md)
  An attribute key whose value specifies a localized number format.
### Getting formatting attribute keys
- [static let listItemDelimiter: NSAttributedString.Key](./key/listitemdelimiter.md)
  The delimiter used when declaring the current list item.
### Getting writing tools attribute keys
- [static let writingToolsExclusionAttributeName: NSAttributedString.Key](./key/writingtoolsexclusionattributename.md)
### Deprecated Keys
- [static let expansion: NSAttributedString.Key](./key/expansion.md)
  The expansion factor of the text.
- [static let obliqueness: NSAttributedString.Key](./key/obliqueness.md)
  The obliqueness of the text.
- [static let verticalGlyphForm: NSAttributedString.Key](./key/verticalglyphform.md)
  The vertical glyph form of the text.
- [static let characterShapeAttributeName: NSAttributedString.Key](./key/charactershapeattributename.md)
  The character shape attribute.
- [static let usesScreenFontsDocumentAttribute: NSAttributedString.Key](./key/usesscreenfontsdocumentattribute.md)
  The screen fonts attribute.
### Initializers
- [init(String)](./key/init%28_%29.md)
  Creates an attributed string key.
- [init(rawValue: String)](./key/init%28rawvalue%29.md)
  Creates an attributed string key with the specified raw value.
### Type Properties
- [static let AXSpeechAttributeSSML: NSAttributedString.Key](./key/axspeechattributessml.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting text content attributes
- [NSAttributedString.TextHighlightStyle](./texthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSAttributedString.TextHighlightColorScheme](./texthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSAttributedString.TextEffectStyle](./texteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSAttributedString.SpellingState](./spellingstate.md)
  Constants for the spelling state attribute key.
- [struct NSUnderlineStyle](../../UIKit/nsunderlinestyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](../../UIKit/nswritingdirectionformattype.md)
  Constants for the writing direction attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key)*