# Measurement.AttributedStyle.ByteCount

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

Available when `UnitType` is `UnitInformationStorage`.

## Overview

Use the [`attributed`](../formatstyle/bytecount/attributed.md) modifier on a [`Measurement.FormatStyle.ByteCount`](../formatstyle/bytecount.md) instance to create a format style of this type.

The attributed strings that this fomat style creates contain attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](../../attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## Topics

### Creating an attributed byte count format style
- [init(style: Measurement<UnitType>.AttributedStyle.ByteCount.Style, allowedUnits: Measurement<UnitType>.AttributedStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)](./bytecount/init%28style,allowedunits,spellsoutzero,includesactualbytecount,locale%29.md)
  Initializes an attributed byte count format style.
### Formatting a byte count
- [func format(Measurement<UnitInformationStorage>) -> AttributedString](./bytecount/format%28_%29.md)
  Formats a byte count measurment, using this style.
### Accessing style properties
- [var allowedUnits: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount.Units](./bytecount/allowedunits.md)
  The units the format style can use to express the byte count.
- [Measurement.AttributedStyle.ByteCount.Units](./bytecount/units.md)
  The type the measurement format style uses to represent byte-counting units.
- [var spellsOutZero: Bool](./bytecount/spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](./bytecount/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var style: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount.Style](./bytecount/style-swift.property.md)
  The style of byte count to express, such as memory or file system storage.
- [Measurement.AttributedStyle.ByteCount.Style](./bytecount/style-swift.typealias.md)
  The type used to represent the style of the formatted byte count.
- [var locale: Locale](./bytecount/locale.md)
  The locale to use to format the numeric part of the byte count.
### Modifying style locale
- [func locale(Locale) -> Measurement<UnitType>.AttributedStyle.ByteCount](./bytecount/locale%28_%29.md)
  Modifies the format style to use the specified locale.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [FormatStyle](../../formatstyle.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating attributed strings
- [var attributed: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount](../formatstyle/bytecount/attributed.md)
  An attributed format style based on the byte count format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount)*