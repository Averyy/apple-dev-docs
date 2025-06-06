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
var spellsOutZero: Bool { get set }
```

#### Discussion

When this value is true, the format style produces output like `Zero kB`.

## See Also

- [var allowedUnits: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount.Units](measurement/attributedstyle/bytecount/allowedunits.md)
  The units the format style can use to express the byte count.
- [Measurement.AttributedStyle.ByteCount.Units](measurement/attributedstyle/bytecount/units.md)
  The type the measurement format style uses to represent byte-counting units.
- [var includesActualByteCount: Bool](measurement/attributedstyle/bytecount/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var style: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount.Style](measurement/attributedstyle/bytecount/style-swift.property.md)
  The style of byte count to express, such as memory or file system storage.
- [Measurement.AttributedStyle.ByteCount.Style](measurement/attributedstyle/bytecount/style-swift.typealias.md)
  The type used to represent the style of the formatted byte count.
- [var locale: Locale](measurement/attributedstyle/bytecount/locale.md)
  The locale to use to format the numeric part of the byte count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/spellsoutzero)*