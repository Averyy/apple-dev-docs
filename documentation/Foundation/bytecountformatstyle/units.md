# ByteCountFormatStyle.Units

**Framework**: Foundation  
**Kind**: struct

The units to use when formatting a byte count, such as kilobytes or gigabytes.

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
struct Units
```

## Topics

### Units
- [static var `default`: ByteCountFormatStyle.Units](bytecountformatstyle/units/default.md)
  A value that indicates a format style should use the most appropriate units to express a byte count.
- [static var all: ByteCountFormatStyle.Units](bytecountformatstyle/units/all.md)
  A value that allows the use of all byte-count units.
- [static var bytes: ByteCountFormatStyle.Units](bytecountformatstyle/units/bytes.md)
  A value that indicates a format style should express byte counts in individual bytes.
- [static var kb: ByteCountFormatStyle.Units](bytecountformatstyle/units/kb.md)
  The kilobytes unit.
- [static var mb: ByteCountFormatStyle.Units](bytecountformatstyle/units/mb.md)
  The megabytes unit.
- [static var gb: ByteCountFormatStyle.Units](bytecountformatstyle/units/gb.md)
  The gigabytes unit.
- [static var tb: ByteCountFormatStyle.Units](bytecountformatstyle/units/tb.md)
  The terabytes unit.
- [static var pb: ByteCountFormatStyle.Units](bytecountformatstyle/units/pb.md)
  The petabytes unit.
- [static var eb: ByteCountFormatStyle.Units](bytecountformatstyle/units/eb.md)
  The exabytes unit.
- [static var zb: ByteCountFormatStyle.Units](bytecountformatstyle/units/zb.md)
  The zettabytes unit.
- [static var ybOrHigher: ByteCountFormatStyle.Units](bytecountformatstyle/units/yborhigher.md)
  A value that indicates a format style should express byte counts as yottabytes or higher.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)](bytecountformatstyle/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:).md)
  Initializes a byte count format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/units)*