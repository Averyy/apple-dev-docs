# byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a format style to format a data storage value.

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
static func byteCount(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units = .all, spellsOutZero: Bool = true, includesActualByteCount: Bool = false) -> Self
```

Available when `Self` is `ByteCountFormatStyle`.

## Return Value

A format style for formatting a measurement of data storage, customized with the provided behaviors.

## Discussion

Use this type method when the call point allows the use of [`ByteCountFormatStyle`](../bytecountformatstyle.md). You typically do this when calling the [`formatted(_:)`](../../Swift/binaryinteger/formatted%28_%29-4qd73.md) method of [`BinaryInteger`](../../Swift/binaryinteger.md) values that represent byte counts, as seen here:

```swift
let count: Int64 = 1024
let formatted = count.formatted(.byteCount(style: .memory)) // "1 kB"
```

## Parameters

- `style`: The style of byte count to express, such as memory or file system storage.
- `allowedUnits`: The units the format style can use to express the byte count.
- `spellsOutZero`: A Boolean value that indicates whether the format style should spell out zero-byte values as text, like `Zero kB`.
- `includesActualByteCount`: A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units. For example, `1 kB (1,024 bytes)`.

## See Also

### Applying byte-count styles
- [struct ByteCountFormatStyle](../bytecountformatstyle.md)
  A format style that provides string representations of byte counts.
- [static func byteCount(style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](./bytecount%28style,allowedunits,spellsoutzero,includesactualbytecount%29-ev0u.md)
  Returns a format style to format a data storage value represented with Foundation’s measurement type.
- [Measurement.FormatStyle.ByteCount](../measurement/formatstyle/bytecount.md)
  A format style that provides string representations of byte counts, expressed as measurements of information storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-59ep0)*