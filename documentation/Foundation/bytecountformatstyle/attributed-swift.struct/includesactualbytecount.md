# includesActualByteCount

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.

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
var includesActualByteCount: Bool
```

#### Discussion

When this value is `true`, a format style produces output like `1 kB (1,024 bytes)`.

## See Also

- [var allowedUnits: ByteCountFormatStyle.Units](bytecountformatstyle/attributed-swift.struct/allowedunits.md)
  The units the format style can use to express the byte count.
- [var spellsOutZero: Bool](bytecountformatstyle/attributed-swift.struct/spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var locale: Locale](bytecountformatstyle/attributed-swift.struct/locale.md)
  The locale to use to format the numeric part of the byte count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/attributed-swift.struct/includesactualbytecount)*