# Measurement.AttributedStyle.ByteCount

**Framework**: Foundation  
**Kind**: struct

A format style that converts byte counts into attributed strings.

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
struct ByteCount
```

#### Overview

Use the [`attributed`](measurement/formatstyle/bytecount/attributed.md) modifier on a [`Measurement.FormatStyle.ByteCount`](measurement/formatstyle/bytecount.md) instance to create a format style of this type.

The attributed strings that this fomat style creates contain attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## Topics

### Creating an attributed byte count format style
- [init(style: Measurement<UnitType>.AttributedStyle.ByteCount.Style, allowedUnits: Measurement<UnitType>.AttributedStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)](measurement/attributedstyle/bytecount/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:).md)
  Initializes an attributed byte count format style.
### Accessing style properties
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
- [var locale: Locale](measurement/attributedstyle/bytecount/locale.md)
  The locale to use to format the numeric part of the byte count.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var attributed: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount](measurement/formatstyle/bytecount/attributed.md)
  An attributed format style based on the byte count format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount)*