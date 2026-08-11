# AttributeScopes.AccessibilityAttributes.SpeechSSMLAttribute

**Framework**: Foundation  
**Kind**: enum

An attribute for an SSML fragment describing how the annotated range should be spoken.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
enum SpeechSSMLAttribute
```

#### Overview

The value is an SSML fragment string. Assistive technologies that produce speech use the fragment to determine pronunciation, language, pacing, and emphasis for the annotated range. Non-speech clients (e.g. Braille) ignore this attribute.

When present, this attribute takes precedence over the older single-purpose speech attributes (IPA notation, spell out, pitch, punctuation, language).

## Relationships

### Conforms To
- [AttributedStringKey](attributedstringkey.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [DecodableAttributedStringKey](decodableattributedstringkey.md)
- [EncodableAttributedStringKey](encodableattributedstringkey.md)
- [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/speechssmlattribute)*