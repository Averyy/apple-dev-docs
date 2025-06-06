# locale

**Framework**: Foundation  
**Kind**: property

The locale to use to format the numeric part of the byte count.

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
var locale: Locale { get set }
```

#### Discussion

To change the format style’s locale, use [`locale(_:)`](formatstyle/locale(_:).md).

## See Also

- [var allowedUnits: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount.Units](measurement/attributedstyle/bytecount/allowedunits.md)
  The units the format style can use to express the byte count.
- [Measurement.AttributedStyle.ByteCount.Units](measurement/attributedstyle/bytecount/units.md)
  The type the measurement format style uses to represent byte-counting units.
- [var spellsOutZero: Bool](measurement/attributedstyle/bytecount/spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](measurement/attributedstyle/bytecount/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var style: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount.Style](measurement/attributedstyle/bytecount/style-swift.property.md)
  The style of byte count to express, such as memory or file system storage.
- [Measurement.AttributedStyle.ByteCount.Style](measurement/attributedstyle/bytecount/style-swift.typealias.md)
  The type used to represent the style of the formatted byte count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/locale)*