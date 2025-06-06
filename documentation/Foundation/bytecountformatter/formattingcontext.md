# formattingContext

**Framework**: Foundation  
**Kind**: property

Specify the formatting context for the formatted string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var formattingContext: Formatter.Context { get set }
```

#### Discussion

The default value is `NSFormattingContextUnknown`. See [`Formatter`](formatter.md) for possible values.

## See Also

- [var countStyle: ByteCountFormatter.CountStyle](bytecountformatter/countstyle-swift.property.md)
  Specify the number of bytes to be used for kilobytes.
- [var allowsNonnumericFormatting: Bool](bytecountformatter/allowsnonnumericformatting.md)
  Determines whether to allow more natural display of some values.
- [var includesActualByteCount: Bool](bytecountformatter/includesactualbytecount.md)
  Determines whether to include the number of bytes after the formatted string.
- [var isAdaptive: Bool](bytecountformatter/isadaptive.md)
  Determines the display style of the size representation.
- [var allowedUnits: ByteCountFormatter.Units](bytecountformatter/allowedunits.md)
  Specify the units that can be used in the output.
- [var includesCount: Bool](bytecountformatter/includescount.md)
  Determines whether to include the count in the resulting formatted string.
- [var includesUnit: Bool](bytecountformatter/includesunit.md)
  Determines whether to include the units in the resulting formatted string.
- [var zeroPadsFractionDigits: Bool](bytecountformatter/zeropadsfractiondigits.md)
  Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/formattingcontext)*