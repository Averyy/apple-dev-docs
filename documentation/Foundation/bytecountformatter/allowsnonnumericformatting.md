# allowsNonnumericFormatting

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Determines whether to allow more natural display of some values.

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
var allowsNonnumericFormatting: Bool { get set }
```

```objc
@property BOOL allowsNonnumericFormatting;
```

#### Discussion

Displays a more natural display of some values, such as zero, where it may be displayed as `Zero KB`, ignoring all other flags or options (with the exception of [`useBytes`](./units/usebytes.md), which would generate `Zero bytes`).The result is appropriate for standalone output.

Special handling of certain values such as zero is especially important in some languages, so it’s highly recommended that this property be left in its default state.

Default value is [`true`](../../Swift/true.md).

## See Also

### Setting Formatting Styles
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  Specify the formatting context for the formatted string.
- [var countStyle: ByteCountFormatter.CountStyle](./countstyle-swift.property.md)
  Specify the number of bytes to be used for kilobytes.
- [var includesActualByteCount: Bool](./includesactualbytecount.md)
  Determines whether to include the number of bytes after the formatted string.
- [var isAdaptive: Bool](./isadaptive.md)
  Determines the display style of the size representation.
- [var allowedUnits: ByteCountFormatter.Units](./allowedunits.md)
  Specify the units that can be used in the output.
- [var includesCount: Bool](./includescount.md)
  Determines whether to include the count in the resulting formatted string.
- [var includesUnit: Bool](./includesunit.md)
  Determines whether to include the units in the resulting formatted string.
- [var zeroPadsFractionDigits: Bool](./zeropadsfractiondigits.md)
  Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/allowsnonnumericformatting)*