# ByteCountFormatStyle.Units

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [static var `default`: ByteCountFormatStyle.Units](./units/default.md)
  A value that indicates a format style should use the most appropriate units to express a byte count.
- [static var all: ByteCountFormatStyle.Units](./units/all.md)
  A value that allows the use of all byte-count units.
- [static var bytes: ByteCountFormatStyle.Units](./units/bytes.md)
  A value that indicates a format style should express byte counts in individual bytes.
- [static var kb: ByteCountFormatStyle.Units](./units/kb.md)
  The kilobytes unit.
- [static var mb: ByteCountFormatStyle.Units](./units/mb.md)
  The megabytes unit.
- [static var gb: ByteCountFormatStyle.Units](./units/gb.md)
  The gigabytes unit.
- [static var tb: ByteCountFormatStyle.Units](./units/tb.md)
  The terabytes unit.
- [static var pb: ByteCountFormatStyle.Units](./units/pb.md)
  The petabytes unit.
- [static var eb: ByteCountFormatStyle.Units](./units/eb.md)
  The exabytes unit.
- [static var zb: ByteCountFormatStyle.Units](./units/zb.md)
  The zettabytes unit.
- [static var ybOrHigher: ByteCountFormatStyle.Units](./units/yborhigher.md)
  A value that indicates a format style should express byte counts as yottabytes or higher.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a byte count style
- [init(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)](./init%28style,allowedunits,spellsoutzero,includesactualbytecount,locale%29.md)
  Initializes a byte count format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/units)*