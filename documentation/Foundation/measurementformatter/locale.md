# locale

**Framework**: Foundation  
**Kind**: property

The locale of the formatter.

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
var locale: Locale! { get set }
```

#### Discussion

If unspecified, an [`NSLocale`](nslocale.md) object representing the current system locale is used.

## See Also

- [var unitOptions: MeasurementFormatter.UnitOptions](measurementformatter/unitoptions-swift.property.md)
  The options for how the unit is formatted.
- [MeasurementFormatter.UnitOptions](measurementformatter/unitoptions-swift.struct.md)
  Measurement formatter options.
- [var unitStyle: Formatter.UnitStyle](measurementformatter/unitstyle.md)
  The unit style.
- [var numberFormatter: NumberFormatter!](measurementformatter/numberformatter.md)
  The number formatter used to format the quantity of a measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter/locale)*