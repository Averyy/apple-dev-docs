# Measurement.FormatStyle.ByteCount

**Framework**: Foundation  
**Kind**: struct

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

#### Overview

Use this style with a [`Measurement`](measurement.md) whose unit type is [`UnitInformationStorage`](unitinformationstorage.md) to format byte counts according to locale conventions.

The following example creates a measurement of 1,024 bytes, and then formats it as an expression of memory storage, with the default byte count format style:

```swift
let count = Measurement(value: 1024, unit: UnitInformationStorage.bytes)
let formatted = count.formatted(.byteCount(style: .memory)) // "1 kB"
```

You can also customize a byte count format style, and use this to format one or more [`Measurement`](measurement.md) instances. The following example creates a format style to only use kilobyte units, and to spell out the exact byte count of the measurement.

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
- [init(style: Measurement<UnitType>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitType>.FormatStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)](measurement/formatstyle/bytecount/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:).md)
  Initializes a byte count format style.
### Accessing style properties
- [var allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units](measurement/formatstyle/bytecount/allowedunits.md)
  The units the format style can use to express the byte count.
- [Measurement.FormatStyle.ByteCount.Units](measurement/formatstyle/bytecount/units.md)
  The type the measurement format style uses to represent byte-counting units.
- [var spellsOutZero: Bool](measurement/formatstyle/bytecount/spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](measurement/formatstyle/bytecount/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style](measurement/formatstyle/bytecount/style-swift.property.md)
  The style of byte count to express, such as memory or file system storage.
- [Measurement.FormatStyle.ByteCount.Style](measurement/formatstyle/bytecount/style-swift.typealias.md)
  The type used to represent the style of the formatted byte count.
- [var locale: Locale](measurement/formatstyle/bytecount/locale.md)
  The locale to use to format the numeric part of the byte count.
### Creating attributed strings
- [var attributed: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount](measurement/formatstyle/bytecount/attributed.md)
  An attributed format style based on the byte count format style.
- [Measurement.AttributedStyle.ByteCount](measurement/attributedstyle/bytecount.md)
  A format style that converts byte counts into attributed strings.

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

- [static func byteCount(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-59ep0.md)
  Returns a format style to format a data storage value.
- [struct ByteCountFormatStyle](bytecountformatstyle.md)
  A format style that provides string representations of byte counts.
- [static func byteCount(style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-ev0u.md)
  Returns a format style to format a data storage value represented with Foundation’s measurement type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount)*