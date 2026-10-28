# includesCount

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Determines whether to include the count in the resulting formatted string.

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
var includesCount: Bool { get set }
```

```objc
@property BOOL includesCount;
```

## Discussion

If set to [`true`](../../Swift/true.md) and [`includesUnit`](./includesunit.md) is set to [`false`](../../Swift/false.md), no unit is displayed. For example, a value of 723 KB is formatted as `723`.

You can get the set this property to [`true`](../../Swift/true.md) and the [`includesUnit`](./includesunit.md) to [`true`](../../Swift/true.md) individually to get both parts, separately. Note that putting them together yourself via string concatenation may be incorrect for some locales.

The default value is [`true`](../../Swift/true.md).

> **Note**:  Setting this value to [`false`](../../Swift/false.md) and [`allowedUnits`](./allowedunits.md) to [`false`](../../Swift/false.md) results in an empty string.

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
- [var allowedUnits: ByteCountFormatter.Units](./allowedunits.md)
  Specify the units that can be used in the output.
- [var includesUnit: Bool](./includesunit.md)
  Determines whether to include the units in the resulting formatted string.
- [var zeroPadsFractionDigits: Bool](./zeropadsfractiondigits.md)
  Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/includescount)*