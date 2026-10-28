# Measurement.FormatStyle.ByteCount

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A format style that provides string representations of byte counts, expressed as measurements of information storage.

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

Use this style with a [`Measurement`](../../measurement.md) whose unit type is [`UnitInformationStorage`](../../unitinformationstorage.md) to format byte counts according to locale conventions.

The following example creates a measurement of 1,024 bytes, and then formats it as an expression of memory storage, with the default byte count format style:

```swift
let count = Measurement(value: 1024, unit: UnitInformationStorage.bytes)
let formatted = count.formatted(.byteCount(style: .memory)) // "1 kB"
```

You can also customize a byte count format style, and use this to format one or more [`Measurement`](../../measurement.md) instances. The following example creates a format style to only use kilobyte units, and to spell out the exact byte count of the measurement.

```swift
let count = Measurement(value: 1024, unit: UnitInformationStorage.bytes)
let style = Measurement.FormatStyle.ByteCount(style: .memory,
                                              allowedUnits: .kb,
                                              spellsOutZero: true,
                                              includesActualByteCount: true,
                                              locale: Locale(identifier: "en_US"))
let customFormatted = style.format(count) // "1 kB (1,024 bytes)"
```

## Topics

### Creating a byte count style
- [init(style: Measurement<UnitType>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitType>.FormatStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)](./bytecount/init%28style,allowedunits,spellsoutzero,includesactualbytecount,locale%29.md)
  Initializes a byte count format style.
### Formatting byte count measurements
- [func format(Measurement<UnitInformationStorage>) -> String](./bytecount/format%28_%29.md)
  Formats a byte count measurment, using this style.
### Accessing style properties
- [var allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units](./bytecount/allowedunits.md)
  The units the format style can use to express the byte count.
- [Measurement.FormatStyle.ByteCount.Units](./bytecount/units.md)
  The type the measurement format style uses to represent byte-counting units.
- [var spellsOutZero: Bool](./bytecount/spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](./bytecount/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style](./bytecount/style-swift.property.md)
  The style of byte count to express, such as memory or file system storage.
- [Measurement.FormatStyle.ByteCount.Style](./bytecount/style-swift.typealias.md)
  The type used to represent the style of the formatted byte count.
- [var locale: Locale](./bytecount/locale.md)
  The locale to use to format the numeric part of the byte count.
### Modifying style locale
- [func locale(Locale) -> Measurement<UnitType>.FormatStyle.ByteCount](./bytecount/locale%28_%29.md)
  Modifies the format style to use the specified locale.
### Creating attributed strings
- [var attributed: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount](./bytecount/attributed.md)
  An attributed format style based on the byte count format style.
- [Measurement.AttributedStyle.ByteCount](../attributedstyle/bytecount.md)
  A format style that converts byte counts into attributed strings.

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

### Applying byte-count styles
- [static func byteCount(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](../../formatstyle/bytecount%28style,allowedunits,spellsoutzero,includesactualbytecount%29-59ep0.md)
  Returns a format style to format a data storage value.
- [struct ByteCountFormatStyle](../../bytecountformatstyle.md)
  A format style that provides string representations of byte counts.
- [static func byteCount(style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](../../formatstyle/bytecount%28style,allowedunits,spellsoutzero,includesactualbytecount%29-ev0u.md)
  Returns a format style to format a data storage value represented with Foundation’s measurement type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount)*