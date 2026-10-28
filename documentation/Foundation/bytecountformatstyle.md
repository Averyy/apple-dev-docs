# ByteCountFormatStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A format style that provides string representations of byte counts.

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
struct ByteCountFormatStyle
```

## Overview

The following example creates an `Int` representing 1,024 bytes, and then formats it as an expression of memory storage, with the default byte count format style.

```swift
let count: Int64 = 1024
let formatted = count.formatted(.byteCount(style: .memory)) // "1 kB"
```

You can also customize a byte count format style, and use this to format one or more [`Int64`](../Swift/int64.md) instances. The following example creates a format style to only use kilobyte units, and to spell out the exact byte count of the measurement.

```swift
let style = ByteCountFormatStyle(style: .memory,                                 
                                 allowedUnits: [.kb],
                                 spellsOutZero: true,
                                 includesActualByteCount: false,
                                 locale: Locale(identifier: "en_US"))
let counts: [Int64] = [0, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
let formatted = counts.map ( {style.format($0) } ) // ["Zero kB", "1 kB", "2 kB", "4 kB", "8 kB", "16 kB", "32 kB", "64 kB"]
```

## Topics

### Creating a byte count style
- [init(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)](./bytecountformatstyle/init%28style,allowedunits,spellsoutzero,includesactualbytecount,locale%29.md)
  Initializes a byte count format style.
- [ByteCountFormatStyle.Units](./bytecountformatstyle/units.md)
  The units to use when formatting a byte count, such as kilobytes or gigabytes.
### Formatting byte count values
- [func format(Int64) -> String](./bytecountformatstyle/format%28_%29.md)
  Formats a numeric byte count, using this style.
### Customizing style behavior
- [var style: ByteCountFormatStyle.Style](./bytecountformatstyle/style-swift.property.md)
  The semantic style the format style uses to represent a byte count value.
- [ByteCountFormatStyle.Style](./bytecountformatstyle/style-swift.enum.md)
  The semantic style to use when formatting a byte count value.
### Accessing style properties
- [var allowedUnits: ByteCountFormatStyle.Units](./bytecountformatstyle/allowedunits.md)
  The units the format style can use to express the byte count.
- [ByteCountFormatStyle.Units](./bytecountformatstyle/units.md)
  The units to use when formatting a byte count, such as kilobytes or gigabytes.
- [var spellsOutZero: Bool](./bytecountformatstyle/spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](./bytecountformatstyle/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var locale: Locale](./bytecountformatstyle/locale.md)
  The locale to use to format the numeric part of the byte count.
### Modifying style locale
- [func locale(Locale) -> ByteCountFormatStyle](./bytecountformatstyle/locale%28_%29.md)
  Modifies the format style to use the specified locale.
### Creating attributed strings
- [var attributed: ByteCountFormatStyle.Attributed](./bytecountformatstyle/attributed-swift.property.md)
  An attributed format style based on the byte count format style.
- [ByteCountFormatStyle.Attributed](./bytecountformatstyle/attributed-swift.struct.md)
  A format style that converts byte counts into attributed strings.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [FormatStyle](./formatstyle.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Applying byte-count styles
- [static func byteCount(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](./formatstyle/bytecount%28style,allowedunits,spellsoutzero,includesactualbytecount%29-59ep0.md)
  Returns a format style to format a data storage value.
- [static func byteCount(style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](./formatstyle/bytecount%28style,allowedunits,spellsoutzero,includesactualbytecount%29-ev0u.md)
  Returns a format style to format a data storage value represented with Foundation’s measurement type.
- [Measurement.FormatStyle.ByteCount](./measurement/formatstyle/bytecount.md)
  A format style that provides string representations of byte counts, expressed as measurements of information storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle)*