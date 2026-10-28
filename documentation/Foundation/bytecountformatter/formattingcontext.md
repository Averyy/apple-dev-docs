# formattingContext

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property NSFormattingContext formattingContext;
```

## Discussion

The default value is `NSFormattingContextUnknown`. See [`Formatter`](../formatter.md) for possible values.

## See Also

### Setting Formatting Styles
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
- [var includesCount: Bool](./includescount.md)
  Determines whether to include the count in the resulting formatted string.
- [var includesUnit: Bool](./includesunit.md)
  Determines whether to include the units in the resulting formatted string.
- [var zeroPadsFractionDigits: Bool](./zeropadsfractiondigits.md)
  Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/formattingcontext)*