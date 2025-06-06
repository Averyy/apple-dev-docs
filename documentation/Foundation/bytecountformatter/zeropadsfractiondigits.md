# zeroPadsFractionDigits

**Framework**: Foundation  
**Kind**: property

Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.

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
var zeroPadsFractionDigits: Bool { get set }
```

#### Discussion

Displaying values using  zero pad fraction digits causes a consistent number of fraction digits are displayed, causing updating displays to remain more stable. For instance, if the [`isAdaptive`](bytecountformatter/isadaptive.md) algorithm is used, this option formats 1.19 and 1.2 GB as `1.19 GB` and `1.20 GB`, respectively, while without the option the latter would be displayed as `1.2 GB`.

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var formattingContext: Formatter.Context](bytecountformatter/formattingcontext.md)
  Specify the formatting context for the formatted string.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/zeropadsfractiondigits)*