# EncodableAttributedStringKey

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines how an attribute key encodes its value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol EncodableAttributedStringKey : AttributedStringKey
```

#### Overview

Implement this protocol to make an attribute encodable. Encoding an [`AttributedString`](attributedstring.md) or [`AttributeContainer`](attributecontainer.md) drops any attributes whose types don’t conform to this protocol.

## Topics

### Encoding Values
- [static func encode(Self.Value, to: any Encoder) throws](encodableattributedstringkey/encode(_:to:).md)
  Encodes a value to the provided encoder.

## Relationships

### Inherits From
- [AttributedStringKey](attributedstringkey.md)
### Conforming Types
- [AttributeScopes.AccessibilityAttributes.AdjustedPitchAttribute](attributescopes/accessibilityattributes/adjustedpitchattribute.md)
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute](attributescopes/accessibilityattributes/announcementpriorityattribute.md)
- [AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute](attributescopes/accessibilityattributes/headinglevelattribute.md)
- [AttributeScopes.AccessibilityAttributes.IPANotationAttribute](attributescopes/accessibilityattributes/ipanotationattribute.md)
- [AttributeScopes.AccessibilityAttributes.IncludesPunctuationAttribute](attributescopes/accessibilityattributes/includespunctuationattribute.md)
- [AttributeScopes.AccessibilityAttributes.QueueAnnouncementAttribute](attributescopes/accessibilityattributes/queueannouncementattribute.md)
- [AttributeScopes.AccessibilityAttributes.SpellOutAttribute](attributescopes/accessibilityattributes/spelloutattribute.md)
- [AttributeScopes.AccessibilityAttributes.TextCustomAttribute](attributescopes/accessibilityattributes/textcustomattribute.md)
- [AttributeScopes.AccessibilityAttributes.TextualContextAttribute](attributescopes/accessibilityattributes/textualcontextattribute.md)
- [AttributeScopes.AppKitAttributes.AdaptiveImageGlyphAttribute](attributescopes/appkitattributes/adaptiveimageglyphattribute.md)
- [AttributeScopes.AppKitAttributes.AttachmentAttribute](attributescopes/appkitattributes/attachmentattribute.md)
- [AttributeScopes.AppKitAttributes.BackgroundColorAttribute](attributescopes/appkitattributes/backgroundcolorattribute.md)
- [AttributeScopes.AppKitAttributes.BaselineOffsetAttribute](attributescopes/appkitattributes/baselineoffsetattribute.md)
- [AttributeScopes.AppKitAttributes.ExpansionAttribute](attributescopes/appkitattributes/expansionattribute.md)
- [AttributeScopes.AppKitAttributes.FontAttribute](attributescopes/appkitattributes/fontattribute.md)
- [AttributeScopes.AppKitAttributes.ForegroundColorAttribute](attributescopes/appkitattributes/foregroundcolorattribute.md)
- [AttributeScopes.AppKitAttributes.GlyphInfoAttribute](attributescopes/appkitattributes/glyphinfoattribute.md)
- [AttributeScopes.AppKitAttributes.KernAttribute](attributescopes/appkitattributes/kernattribute.md)
- [AttributeScopes.AppKitAttributes.LigatureAttribute](attributescopes/appkitattributes/ligatureattribute.md)
- [AttributeScopes.AppKitAttributes.MarkedClauseSegmentAttribute](attributescopes/appkitattributes/markedclausesegmentattribute.md)
- [AttributeScopes.AppKitAttributes.ObliquenessAttribute](attributescopes/appkitattributes/obliquenessattribute.md)
- [AttributeScopes.AppKitAttributes.ParagraphStyleAttribute](attributescopes/appkitattributes/paragraphstyleattribute.md)
- [AttributeScopes.AppKitAttributes.ShadowAttribute](attributescopes/appkitattributes/shadowattribute.md)
- [AttributeScopes.AppKitAttributes.StrikethroughColorAttribute](attributescopes/appkitattributes/strikethroughcolorattribute.md)
- [AttributeScopes.AppKitAttributes.StrikethroughStyleAttribute](attributescopes/appkitattributes/strikethroughstyleattribute.md)
- [AttributeScopes.AppKitAttributes.StrokeColorAttribute](attributescopes/appkitattributes/strokecolorattribute.md)
- [AttributeScopes.AppKitAttributes.StrokeWidthAttribute](attributescopes/appkitattributes/strokewidthattribute.md)
- [AttributeScopes.AppKitAttributes.SuperscriptAttribute](attributescopes/appkitattributes/superscriptattribute.md)
- [AttributeScopes.AppKitAttributes.TextAlternativesAttribute](attributescopes/appkitattributes/textalternativesattribute.md)
- [AttributeScopes.AppKitAttributes.TextEffectAttribute](attributescopes/appkitattributes/texteffectattribute.md)
- [AttributeScopes.AppKitAttributes.ToolTipAttribute](attributescopes/appkitattributes/tooltipattribute.md)
- [AttributeScopes.AppKitAttributes.TrackingAttribute](attributescopes/appkitattributes/trackingattribute.md)
- [AttributeScopes.AppKitAttributes.UnderlineColorAttribute](attributescopes/appkitattributes/underlinecolorattribute.md)
- [AttributeScopes.AppKitAttributes.UnderlineStyleAttribute](attributescopes/appkitattributes/underlinestyleattribute.md)
- [AttributeScopes.CoreTextAttributes.TextAlignmentAttribute](attributescopes/coretextattributes/textalignmentattribute.md)
- [AttributeScopes.FoundationAttributes.AgreementArgumentAttribute](attributescopes/foundationattributes/agreementargumentattribute.md)
- [AttributeScopes.FoundationAttributes.AgreementConceptAttribute](attributescopes/foundationattributes/agreementconceptattribute.md)
- [AttributeScopes.FoundationAttributes.AlternateDescriptionAttribute](attributescopes/foundationattributes/alternatedescriptionattribute.md)
- [AttributeScopes.FoundationAttributes.ByteCountAttribute](attributescopes/foundationattributes/bytecountattribute.md)
- [AttributeScopes.FoundationAttributes.DateFieldAttribute](attributescopes/foundationattributes/datefieldattribute.md)
- [AttributeScopes.FoundationAttributes.DurationFieldAttribute](attributescopes/foundationattributes/durationfieldattribute.md)
- [AttributeScopes.FoundationAttributes.ImageURLAttribute](attributescopes/foundationattributes/imageurlattribute.md)
- [AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternativeattribute.md)
- [AttributeScopes.FoundationAttributes.InflectionRuleAttribute](attributescopes/foundationattributes/inflectionruleattribute.md)
- [AttributeScopes.FoundationAttributes.InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintentattribute.md)
- [AttributeScopes.FoundationAttributes.LanguageIdentifierAttribute](attributescopes/foundationattributes/languageidentifierattribute.md)
- [AttributeScopes.FoundationAttributes.LinkAttribute](attributescopes/foundationattributes/linkattribute.md)
- [AttributeScopes.FoundationAttributes.ListItemDelimiterAttribute](attributescopes/foundationattributes/listitemdelimiterattribute.md)
- [AttributeScopes.FoundationAttributes.LocalizedNumberFormatAttribute](attributescopes/foundationattributes/localizednumberformatattribute.md)
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedDateArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateargumentattribute.md)
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedDateIntervalArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateintervalargumentattribute.md)
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedNumericArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizednumericargumentattribute.md)
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes.LocalizedURLArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizedurlargumentattribute.md)
- [AttributeScopes.FoundationAttributes.MarkdownSourcePositionAttribute](attributescopes/foundationattributes/markdownsourcepositionattribute.md)
- [AttributeScopes.FoundationAttributes.MeasurementAttribute](attributescopes/foundationattributes/measurementattribute.md)
- [AttributeScopes.FoundationAttributes.MorphologyAttribute](attributescopes/foundationattributes/morphologyattribute.md)
- [AttributeScopes.FoundationAttributes.NumberFormatAttributes.NumberPartAttribute](attributescopes/foundationattributes/numberformatattributes/numberpartattribute.md)
- [AttributeScopes.FoundationAttributes.NumberFormatAttributes.SymbolAttribute](attributescopes/foundationattributes/numberformatattributes/symbolattribute.md)
- [AttributeScopes.FoundationAttributes.PersonNameComponentAttribute](attributescopes/foundationattributes/personnamecomponentattribute.md)
- [AttributeScopes.FoundationAttributes.PresentationIntentAttribute](attributescopes/foundationattributes/presentationintentattribute.md)
- [AttributeScopes.FoundationAttributes.ReferentConceptAttribute](attributescopes/foundationattributes/referentconceptattribute.md)
- [AttributeScopes.FoundationAttributes.ReplacementIndexAttribute](attributescopes/foundationattributes/replacementindexattribute.md)
- [AttributeScopes.FoundationAttributes.WritingDirectionAttribute](attributescopes/foundationattributes/writingdirectionattribute.md)
- [AttributeScopes.SpeechAttributes.ConfidenceAttribute](attributescopes/speechattributes/confidenceattribute.md)
- [AttributeScopes.SpeechAttributes.TimeRangeAttribute](attributescopes/speechattributes/timerangeattribute.md)
- [AttributeScopes.SwiftUIAttributes.AdaptiveImageGlyphAttribute](attributescopes/swiftuiattributes/adaptiveimageglyphattribute.md)
- [AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute](attributescopes/swiftuiattributes/backgroundcolorattribute.md)
- [AttributeScopes.SwiftUIAttributes.BaselineOffsetAttribute](attributescopes/swiftuiattributes/baselineoffsetattribute.md)
- [AttributeScopes.SwiftUIAttributes.FontAttribute](attributescopes/swiftuiattributes/fontattribute.md)
- [AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute](attributescopes/swiftuiattributes/foregroundcolorattribute.md)
- [AttributeScopes.SwiftUIAttributes.KerningAttribute](attributescopes/swiftuiattributes/kerningattribute.md)
- [AttributeScopes.SwiftUIAttributes.StrikethroughStyleAttribute](attributescopes/swiftuiattributes/strikethroughstyleattribute.md)
- [AttributeScopes.SwiftUIAttributes.TrackingAttribute](attributescopes/swiftuiattributes/trackingattribute.md)
- [AttributeScopes.SwiftUIAttributes.UnderlineStyleAttribute](attributescopes/swiftuiattributes/underlinestyleattribute.md)
- [AttributeScopes.UIKitAttributes.AdaptiveImageGlyphAttribute](attributescopes/uikitattributes/adaptiveimageglyphattribute.md)
- [AttributeScopes.UIKitAttributes.AttachmentAttribute](attributescopes/uikitattributes/attachmentattribute.md)
- [AttributeScopes.UIKitAttributes.BackgroundColorAttribute](attributescopes/uikitattributes/backgroundcolorattribute.md)
- [AttributeScopes.UIKitAttributes.BaselineOffsetAttribute](attributescopes/uikitattributes/baselineoffsetattribute.md)
- [AttributeScopes.UIKitAttributes.ExpansionAttribute](attributescopes/uikitattributes/expansionattribute.md)
- [AttributeScopes.UIKitAttributes.FontAttribute](attributescopes/uikitattributes/fontattribute.md)
- [AttributeScopes.UIKitAttributes.ForegroundColorAttribute](attributescopes/uikitattributes/foregroundcolorattribute.md)
- [AttributeScopes.UIKitAttributes.KernAttribute](attributescopes/uikitattributes/kernattribute.md)
- [AttributeScopes.UIKitAttributes.LigatureAttribute](attributescopes/uikitattributes/ligatureattribute.md)
- [AttributeScopes.UIKitAttributes.ObliquenessAttribute](attributescopes/uikitattributes/obliquenessattribute.md)
- [AttributeScopes.UIKitAttributes.ParagraphStyleAttribute](attributescopes/uikitattributes/paragraphstyleattribute.md)
- [AttributeScopes.UIKitAttributes.ShadowAttribute](attributescopes/uikitattributes/shadowattribute.md)
- [AttributeScopes.UIKitAttributes.StrikethroughColorAttribute](attributescopes/uikitattributes/strikethroughcolorattribute.md)
- [AttributeScopes.UIKitAttributes.StrikethroughStyleAttribute](attributescopes/uikitattributes/strikethroughstyleattribute.md)
- [AttributeScopes.UIKitAttributes.StrokeColorAttribute](attributescopes/uikitattributes/strokecolorattribute.md)
- [AttributeScopes.UIKitAttributes.StrokeWidthAttribute](attributescopes/uikitattributes/strokewidthattribute.md)
- [AttributeScopes.UIKitAttributes.TextEffectAttribute](attributescopes/uikitattributes/texteffectattribute.md)
- [AttributeScopes.UIKitAttributes.TextItemTagAttribute](attributescopes/uikitattributes/textitemtagattribute.md)
- [AttributeScopes.UIKitAttributes.TrackingAttribute](attributescopes/uikitattributes/trackingattribute.md)
- [AttributeScopes.UIKitAttributes.UnderlineColorAttribute](attributescopes/uikitattributes/underlinecolorattribute.md)
- [AttributeScopes.UIKitAttributes.UnderlineStyleAttribute](attributescopes/uikitattributes/underlinestyleattribute.md)

## See Also

- [protocol DecodableAttributedStringKey](decodableattributedstringkey.md)
  A protocol that defines how an attribute key decodes its value.
- [typealias CodableAttributedStringKey](codableattributedstringkey.md)
  A type alias used by attribute keys that are both encodable and decodable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/encodableattributedstringkey)*