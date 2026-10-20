# AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A key for the color that fills the area behind a run of attributed text.

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
enum BackgroundColorAttribute
```

#### Overview

Set this key to highlight part of a string, such as the way a search result marks the term someone typed:

```
var line = AttributedString("No matches for swift")
if let match = line.range(of: "swift") {
    line[match].backgroundColor = .yellow
}

Text(line)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/backgroundcolorattribute)*