# AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A key for the color that draws a run of attributed text.

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
enum ForegroundColorAttribute
```

## Overview

Set this key to tint part of a string without splitting it into several `Text` views:

```
var status = AttributedString("Low battery")
status.foregroundColor = .red

Text(status)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/foregroundcolorattribute)*