# MarkdownDecodableAttributedStringKey

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines how an attribute key decodes a value that corresponds to Markdown syntax.

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
protocol MarkdownDecodableAttributedStringKey : AttributedStringKey
```

#### Overview

This protocol is separate from [`DecodableAttributedStringKey`](decodableattributedstringkey.md) to separate explicit attributes defined by the SDK from Markdown’s semantic styling attributes. You use these attributes with Apple’s extended syntax for markdown: `^[text](attribute: value)`.

Using this protocol allows your markup names to differ from the names of your attributes. For example, the automatic grammar agreement feature uses markup like `^[text to inflect](inflect: true)`. This feature defines an [`AttributeScopes.FoundationAttributes.InflectionRuleAttribute`](attributescopes/foundationattributes/inflectionruleattribute.md) that conforms to [`MarkdownDecodableAttributedStringKey`](markdowndecodableattributedstringkey.md). The value of its `AttributeScopes/FoundationAttributes/InflectionRuleAttribute/name` proprerty is `NSInflect`, while its `AttributeScopes/FoundationAttributes/InflectionRuleAttribute/markdownName-aom1`, used in actual Markdown strings like the one shown here, is `inflect`.

To define your own attributes for use with Markdown syntax, make sure your attributes conform to this protocol. The markdown parser ignores attributes that don’t conform, even if you use the extended Markdown syntax.

> 💡 **Tip**:  When creating attributed strings from Markdown-based initializers like [`init(markdown:options:baseURL:)`](attributedstring/init(markdown:options:baseurl:)-52n3u.md), be sure to set the [`allowsExtendedAttributes`](attributedstring/markdownparsingoptions/allowsextendedattributes.md) option. If you don’t include this option, the string won’t parse [`MarkdownDecodableAttributedStringKey`](markdowndecodableattributedstringkey.md)-based attributes.

 When creating attributed strings from Markdown-based initializers like [`init(markdown:options:baseURL:)`](attributedstring/init(markdown:options:baseurl:)-52n3u.md), be sure to set the [`allowsExtendedAttributes`](attributedstring/markdownparsingoptions/allowsextendedattributes.md) option. If you don’t include this option, the string won’t parse [`MarkdownDecodableAttributedStringKey`](markdowndecodableattributedstringkey.md)-based attributes.

## Topics

### Decoding Values
- [static func decodeMarkdown(from: any Decoder) throws -> Self.Value](markdowndecodableattributedstringkey/decodemarkdown(from:).md)
  Decodes a value from the provided decoder.
### Accessing the Markdown Name
- [static var markdownName: String](markdowndecodableattributedstringkey/markdownname.md)
  The Markdown name associated with an attributed string key.

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
- [AttributeScopes.FoundationAttributes.AgreementArgumentAttribute](attributescopes/foundationattributes/agreementargumentattribute.md)
- [AttributeScopes.FoundationAttributes.AgreementConceptAttribute](attributescopes/foundationattributes/agreementconceptattribute.md)
- [AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternativeattribute.md)
- [AttributeScopes.FoundationAttributes.InflectionRuleAttribute](attributescopes/foundationattributes/inflectionruleattribute.md)
- [AttributeScopes.FoundationAttributes.LanguageIdentifierAttribute](attributescopes/foundationattributes/languageidentifierattribute.md)
- [AttributeScopes.FoundationAttributes.LocalizedNumberFormatAttribute](attributescopes/foundationattributes/localizednumberformatattribute.md)
- [AttributeScopes.FoundationAttributes.MorphologyAttribute](attributescopes/foundationattributes/morphologyattribute.md)
- [AttributeScopes.FoundationAttributes.ReferentConceptAttribute](attributescopes/foundationattributes/referentconceptattribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/markdowndecodableattributedstringkey)*