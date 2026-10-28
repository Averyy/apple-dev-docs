# init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a byte count format style.

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
init(style: ByteCountFormatStyle.Style = .file, allowedUnits: ByteCountFormatStyle.Units = .all, spellsOutZero: Bool = true, includesActualByteCount: Bool = false, locale: Locale = .autoupdatingCurrent)
```

## Discussion

In situations that can infer the [`ByteCountFormatStyle`](../bytecountformatstyle.md) type, you can call [`byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)`](../formatstyle/bytecount%28style,allowedunits,spellsoutzero,includesactualbytecount%29-59ep0.md) instead of explicitly using this initializer. This is the case when you call [`formatted(_:)`](../../Swift/binaryinteger/formatted%28_%29-4qd73.md) on a [`BinaryInteger`](../../Swift/binaryinteger.md).

## Parameters

- `style`: The style of byte count to express, such as memory or file system storage.
- `allowedUnits`: The units the format style can use to express the byte count.
- `spellsOutZero`: A Boolean value that indicates whether the format style should spell out zero-byte values as text, like `Zero kB`.
- `includesActualByteCount`: A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units. For example, `1 kB (1,024 bytes)`.
- `locale`: The locale to use to format the numeric part of the byte count.

## See Also

### Creating a byte count style
- [ByteCountFormatStyle.Units](./units.md)
  The units to use when formatting a byte count, such as kilobytes or gigabytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:))*