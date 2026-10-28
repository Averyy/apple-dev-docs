# spellsOutZero

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the format style should spell out zero-byte values as text.

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
var spellsOutZero: Bool
```

## Discussion

When this value is true, the format style produces output like `Zero kB`.

## See Also

### Accessing style properties
- [var allowedUnits: ByteCountFormatStyle.Units](./allowedunits.md)
  The units the format style can use to express the byte count.
- [var includesActualByteCount: Bool](./includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var locale: Locale](./locale.md)
  The locale to use to format the numeric part of the byte count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/attributed-swift.struct/spellsoutzero)*