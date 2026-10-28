# Measurement.AttributedStyle.ByteCount.Style

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

The type used to represent the style of the formatted byte count.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
typealias Style = ByteCountFormatStyle.Style
```

## Discussion

This format style uses the [`ByteCountFormatStyle.Style`](../../../bytecountformatstyle/style-swift.enum.md) type to represent the byte-count style.

## See Also

### Accessing style properties
- [var allowedUnits: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount.Units](./allowedunits.md)
  The units the format style can use to express the byte count.
- [Measurement.AttributedStyle.ByteCount.Units](./units.md)
  The type the measurement format style uses to represent byte-counting units.
- [var spellsOutZero: Bool](./spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](./includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var style: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount.Style](./style-swift.property.md)
  The style of byte count to express, such as memory or file system storage.
- [var locale: Locale](./locale.md)
  The locale to use to format the numeric part of the byte count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/style-swift.typealias)*