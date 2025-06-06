# init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)

**Framework**: Foundation  
**Kind**: init

Initializes a byte count format style.

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
init(style: Measurement<UnitType>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitType>.FormatStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)
```

#### Discussion

In situations that infer the [`Measurement.FormatStyle.ByteCount`](measurement/formatstyle/bytecount.md) type, you can call `Measurement/FormatStyle/ByteCount/byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)` instead of explicitly using this initializer. This is the case when you call [`formatted()`](measurement/formatted().md) on a [`Measurement`](measurement.md) whose unit type is [`UnitInformationStorage`](unitinformationstorage.md).

## Parameters

- `style`: The style of byte count to express, such as memory or file system storage.
- `allowedUnits`: The units the format style can use to express the byte count.
- `spellsOutZero`: A Boolean value that indicates whether the format style should spell out zero-byte values as text, like  .
- `includesActualByteCount`: A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units. For example,  .
- `locale`: The locale to use to format the numeric part of the byte count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:))*