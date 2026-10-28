# AttributeScopes.SwiftUIAttributes.FontAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A key for the font of a run of attributed text.

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
enum FontAttribute
```

## Overview

Access this key through the [`font`](./font.md) property of an attribute container, or set it on an `AttributedString` and pass the result to a `Text` view:

```
var headline = AttributedString("On Sale")
headline.font = .headline

Text(headline)
```

## Relationships

### Conforms To
- [AttributedStringKey](../../attributedstringkey.md)
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [DecodableAttributedStringKey](../../decodableattributedstringkey.md)
- [EncodableAttributedStringKey](../../encodableattributedstringkey.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/fontattribute)*