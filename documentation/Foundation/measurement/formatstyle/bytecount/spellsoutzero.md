# spellsOutZero

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the format style should spell out zero-byte values as text.

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
var spellsOutZero: Bool
```

#### Discussion

When this value is true, the format style produces output like `Zero kB`.

## See Also

- [var allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units](measurement/formatstyle/bytecount/allowedunits.md)
  The units the format style can use to express the byte count.
- [Measurement.FormatStyle.ByteCount.Units](measurement/formatstyle/bytecount/units.md)
  The type the measurement format style uses to represent byte-counting units.
- [var includesActualByteCount: Bool](measurement/formatstyle/bytecount/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style](measurement/formatstyle/bytecount/style-swift.property.md)
  The style of byte count to express, such as memory or file system storage.
- [Measurement.FormatStyle.ByteCount.Style](measurement/formatstyle/bytecount/style-swift.typealias.md)
  The type used to represent the style of the formatted byte count.
- [var locale: Locale](measurement/formatstyle/bytecount/locale.md)
  The locale to use to format the numeric part of the byte count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount/spellsoutzero)*