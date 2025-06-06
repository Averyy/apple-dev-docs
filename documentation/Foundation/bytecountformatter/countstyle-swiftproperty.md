# countStyle

**Framework**: Foundation  
**Kind**: property

Specify the number of bytes to be used for kilobytes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var countStyle: ByteCountFormatter.CountStyle { get set }
```

#### Discussion

The default setting is [`ByteCountFormatter.CountStyle.file`](bytecountformatter/countstyle-swift.enum/file.md), which is the system specific value for file and storage sizes.

## See Also

- [var formattingContext: Formatter.Context](bytecountformatter/formattingcontext.md)
  Specify the formatting context for the formatted string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/countstyle-swift.property)*