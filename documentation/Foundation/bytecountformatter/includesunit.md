# includesUnit

**Framework**: Foundation  
**Kind**: property

Determines whether to include the units in the resulting formatted string.

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
var includesUnit: Bool { get set }
```

#### Discussion

If set to [`true`](https://developer.apple.com/documentation/swift/true) and [`includesCount`](bytecountformatter/includescount.md) is set to [`false`](https://developer.apple.com/documentation/swift/false), no count is displayed. For example, a value of 723 KB is formatted as `KB`.

You can get the set this property to [`true`](https://developer.apple.com/documentation/swift/true) and the [`includesCount`](bytecountformatter/includescount.md) to [`true`](https://developer.apple.com/documentation/swift/true) individually to get both parts, separately. Note that putting them together yourself via string concatenation may be incorrect for some locales.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

> **Note**:  Setting this value to [`false`](https://developer.apple.com/documentation/swift/false) and [`includesCount`](bytecountformatter/includescount.md) to [`false`](https://developer.apple.com/documentation/swift/false) results in an empty string.

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
- [var zeroPadsFractionDigits: Bool](bytecountformatter/zeropadsfractiondigits.md)
  Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/includesunit)*