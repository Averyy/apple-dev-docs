# locale

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The locale to use to format the numeric part of the byte count.

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
var locale: Locale { get set }
```

#### Discussion

To change the format style’s locale, use [`locale(_:)`](../formatstyle/locale%28_%29.md).

## See Also

### Accessing style properties
- [var allowedUnits: ByteCountFormatStyle.Units](./allowedunits.md)
  The units the format style can use to express the byte count.
- [ByteCountFormatStyle.Units](./units.md)
  The units to use when formatting a byte count, such as kilobytes or gigabytes.
- [var spellsOutZero: Bool](./spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](./includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/locale)*