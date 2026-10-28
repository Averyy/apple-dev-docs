# allowedUnits

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specify the units that can be used in the output.

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
var allowedUnits: ByteCountFormatter.Units { get set }
```

```objc
@property NSByteCountFormatterUnits allowedUnits;
```

## Discussion

If the value is [`NSByteCountFormatterUseDefault`](../nsbytecountformatterunits/nsbytecountformatterusedefault.md), the formatter uses platform-appropriate settings; otherwise will only the specified units are used.

[`ByteCountFormatter.Units`](./units.md) values can be combined using the C `OR` operator to specify complex formatting strings. The [`NSByteCountFormatterUseDefault`](../nsbytecountformatterunits/nsbytecountformatterusedefault.md) or [`useAll`](./units/useall.md) constants can be used with the C `AND` or the C `NOT` operators to create custom formats as well.

This is the default value if [`NSByteCountFormatterUseDefault`](../nsbytecountformatterunits/nsbytecountformatterusedefault.md).

> **Note**:  ZB and YB cannot be covered by the range of possible values, but you can still choose to use these units to get fractional display (`0.0035 ZB` for instance).

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
- [var isAdaptive: Bool](./isadaptive.md)
  Determines the display style of the size representation.
- [var includesCount: Bool](./includescount.md)
  Determines whether to include the count in the resulting formatted string.
- [var includesUnit: Bool](./includesunit.md)
  Determines whether to include the units in the resulting formatted string.
- [var zeroPadsFractionDigits: Bool](./zeropadsfractiondigits.md)
  Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/allowedunits)*