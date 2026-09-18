# AttributeScopes.SwiftUIAttributes.TrackingAttribute

**Framework**: Foundation  
**Kind**: enum

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

#### Overview

Tracking spreads a run out evenly, which suits a short label set in capitals. Give a positive value to open the run up and a negative value to tighten it:

```None
var label = AttributedString("SOLD OUT")
label.tracking = 3

Text(label)
```

To adjust only the gap between particular pairs of letters, use [`AttributeScopes.SwiftUIAttributes.KerningAttribute`](attributescopes/swiftuiattributes/kerningattribute.md).

## Relationships

### Conforms To
- [AttributedStringKey](attributedstringkey.md)
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [DecodableAttributedStringKey](decodableattributedstringkey.md)
- [EncodableAttributedStringKey](encodableattributedstringkey.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/trackingattribute)*