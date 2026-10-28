# includesActualByteCount

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Determines whether to include the number of bytes after the formatted string.

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
var includesActualByteCount: Bool { get set }
```

```objc
@property BOOL includesActualByteCount;
```

## Discussion

Setting this value to [`true`](../../Swift/true.md) causes the byte count to be displayed parenthetically (localized as appropriate), for instance `723 KB (722,842 bytes)`.  This will happen only if needed, that is, the first part is already not showing the exact byte count.

If [`includesUnit`](./includesunit.md) or [`includesCount`](./includescount.md) are [`false`](../../Swift/false.md), then this setting has no effect.

Default value is [`false`](../../Swift/false.md).

## See Also

### Setting Formatting Styles
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  Specify the formatting context for the formatted string.
- [var countStyle: ByteCountFormatter.CountStyle](./countstyle-swift.property.md)
  Specify the number of bytes to be used for kilobytes.
- [var allowsNonnumericFormatting: Bool](./allowsnonnumericformatting.md)
  Determines whether to allow more natural display of some values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/includesactualbytecount)*