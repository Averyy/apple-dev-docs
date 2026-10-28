# AttributeScopes.SwiftUIAttributes.TrackingAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A key for the space added between every character of a run of attributed text.

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
enum TrackingAttribute
```

## Overview

Tracking spreads a run out evenly, which suits a short label set in capitals. Give a positive value to open the run up and a negative value to tighten it:

```
var label = AttributedString("SOLD OUT")
label.tracking = 3

Text(label)
```

To adjust only the gap between particular pairs of letters, use [`AttributeScopes.SwiftUIAttributes.KerningAttribute`](./kerningattribute.md).

## Relationships

### Conforms To
- [AttributedStringKey](../../attributedstringkey.md)
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [DecodableAttributedStringKey](../../decodableattributedstringkey.md)
- [EncodableAttributedStringKey](../../encodableattributedstringkey.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/trackingattribute)*