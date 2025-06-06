# byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)

**Framework**: Foundation  
**Kind**: method

Returns a format style to format a data storage value represented with Foundation’s measurement type.

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
static func byteCount(style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units = .all, spellsOutZero: Bool = true, includesActualByteCount: Bool = false) -> Self
```

#### Return Value

A format style for formatting a measurement of data storage, customized with the provided behaviors.

#### Discussion

Use this type method when the call point allows the use of [`Measurement.FormatStyle.ByteCount`](measurement/formatstyle/bytecount.md). You typically do this when calling the [`formatted()`](measurement/formatted().md) on a [`Measurement`](measurement.md) whose unit type is [`UnitInformationStorage`](unitinformationstorage.md), as seen in the following example.

```swift
let count = Measurement(value: 1024, unit: UnitInformationStorage.bytes)
let formatted = count.formatted(.byteCount(style: .memory)) // "1 kB"
```

## Parameters

- `style`: The style of byte count to express, such as memory or file system storage.
- `allowedUnits`: The units the format style can use to express the byte count.
- `spellsOutZero`: A Boolean value that indicates whether the format style should spell out zero-byte values as text, like  .
- `includesActualByteCount`: A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units. For example,  .

## See Also

- [static func byteCount(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-59ep0.md)
  Returns a format style to format a data storage value.
- [struct ByteCountFormatStyle](bytecountformatstyle.md)
  A format style that provides string representations of byte counts.
- [Measurement.FormatStyle.ByteCount](measurement/formatstyle/bytecount.md)
  A format style that provides string representations of byte counts, expressed as measurements of information storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-ev0u)*