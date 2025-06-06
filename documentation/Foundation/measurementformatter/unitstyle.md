# unitStyle

**Framework**: Foundation  
**Kind**: property

The unit style.

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
var unitStyle: Formatter.UnitStyle { get set }
```

#### Discussion

The possible values are [`Formatter.UnitStyle.short`](formatter/unitstyle/short.md), [`Formatter.UnitStyle.medium`](formatter/unitstyle/medium.md), and [`Formatter.UnitStyle.long`](formatter/unitstyle/long.md). The default value is [`Formatter.UnitStyle.medium`](formatter/unitstyle/medium.md).

## See Also

- [var unitOptions: MeasurementFormatter.UnitOptions](measurementformatter/unitoptions-swift.property.md)
  The options for how the unit is formatted.
- [var locale: Locale!](measurementformatter/locale.md)
  The locale of the formatter.
- [var numberFormatter: NumberFormatter!](measurementformatter/numberformatter.md)
  The number formatter used to format the quantity of a measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter/unitstyle)*