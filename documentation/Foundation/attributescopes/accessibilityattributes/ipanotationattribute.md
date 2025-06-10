# AttributeScopes.AccessibilityAttributes.IPANotationAttribute

**Framework**: Foundation  
**Kind**: enum

An attribute to define the International Phonetic Alphabet representation for speech.

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
@frozen
enum IPANotationAttribute
```

#### Overview

The IPA representation defines pronunciation of words that have the same spelling but different sounds.

For example, consider the different pronunciations of the word “live” in the following two sentences:

- “Anne wants to live on Main Street.”
- “Maria wants to go to the live concert.”

In the first sentence, “live” rhymes with “give.”  Its IPA representation would be “lɪv”. In the second sentence, it rhymes with “hive”. Its IPA representation would be “laɪv”.

> **Note**: This attribute is not used on macOS

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/ipanotationattribute)*