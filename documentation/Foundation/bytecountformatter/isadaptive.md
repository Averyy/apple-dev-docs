# isAdaptive

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Determines the display style of the size representation.

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
var isAdaptive: Bool { get set }
```

```objc
@property (getter=isAdaptive) BOOL adaptive;
```

#### Discussion

The “adaptive” algorithm is platform specific and uses a different number of fraction digits based on the magnitude (in OS X v10.8: 0 fraction digits for bytes and KB; 1 fraction digits for MB; 2 for GB and above). Otherwise the result always tries to show at least three significant digits, introducing fraction digits as necessary.

Default is [`true`](../../Swift/true.md).

## See Also

### Setting Formatting Styles
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  Specify the formatting context for the formatted string.
- [var countStyle: ByteCountFormatter.CountStyle](./countstyle-swift.property.md)
  Specify the number of bytes to be used for kilobytes.
- [var allowsNonnumericFormatting: Bool](./allowsnonnumericformatting.md)
  Determines whether to allow more natural display of some values.
- [var includesActualByteCount: Bool](./includesactualbytecount.md)
  Determines whether to include the number of bytes after the formatted string.
- [var allowedUnits: ByteCountFormatter.Units](./allowedunits.md)
  Specify the units that can be used in the output.
- [var includesCount: Bool](./includescount.md)
  Determines whether to include the count in the resulting formatted string.
- [var includesUnit: Bool](./includesunit.md)
  Determines whether to include the units in the resulting formatted string.
- [var zeroPadsFractionDigits: Bool](./zeropadsfractiondigits.md)
  Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/isadaptive)*