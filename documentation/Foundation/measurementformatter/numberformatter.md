# numberFormatter

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number formatter used to format the quantity of a measurement.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var numberFormatter: NumberFormatter! { get set }
```

```objc
@property (copy, null_resettable) NSNumberFormatter * numberFormatter;
```

## Discussion

If unspecified, an [`NumberFormatter`](../numberformatter.md) object with [`NumberFormatter.Style.decimal`](../numberformatter/style/decimal.md) style is used.

## See Also

### Specifying the Format
- [var unitOptions: MeasurementFormatter.UnitOptions](./unitoptions-swift.property.md)
  The options for how the unit is formatted.
- [MeasurementFormatter.UnitOptions](./unitoptions-swift.struct.md)
  Measurement formatter options.
- [var unitStyle: Formatter.UnitStyle](./unitstyle.md)
  The unit style.
- [var locale: Locale!](./locale.md)
  The locale of the formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter/numberformatter)*