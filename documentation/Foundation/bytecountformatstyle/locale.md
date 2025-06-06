# locale

**Framework**: Foundation  
**Kind**: property

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

To change the format style’s locale, use [`locale(_:)`](formatstyle/locale(_:).md).

## See Also

- [var allowedUnits: ByteCountFormatStyle.Units](bytecountformatstyle/allowedunits.md)
  The units the format style can use to express the byte count.
- [ByteCountFormatStyle.Units](bytecountformatstyle/units.md)
  The units to use when formatting a byte count, such as kilobytes or gigabytes.
- [var spellsOutZero: Bool](bytecountformatstyle/spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](bytecountformatstyle/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/locale)*