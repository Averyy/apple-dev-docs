# AttributeScopes.SwiftUIAttributes.BaselineOffsetAttribute

**Framework**: Foundation  
**Kind**: enum

A key for the distance a run of attributed text shifts from its baseline.

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
enum BaselineOffsetAttribute
```

#### Overview

A positive value raises the run and a negative value lowers it, which lets you set a unit or a footnote marker above the surrounding text:

```None
var measure = AttributedString("12 m")
if let unit = measure.range(of: "m") {
    measure[unit].baselineOffset = 6
}

Text(measure)
```

Shifting a run does not change the height of the line, so a large offset can push text into the line above or below.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/baselineoffsetattribute)*