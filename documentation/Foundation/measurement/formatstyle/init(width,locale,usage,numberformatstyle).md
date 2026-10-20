# init(width:locale:usage:numberFormatStyle:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an instance using the provided width, locale, usage type, and number format.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(width: Measurement<UnitType>.FormatStyle.UnitWidth, locale: Locale = .autoupdatingCurrent, usage: MeasurementFormatUnitUsage<UnitType> = .general, numberFormatStyle: FloatingPointFormatStyle<Double>? = nil)
```

## Parameters

- `width`: The width of the measurement unit.
- `locale`: The locale to use when formatting the measurement.
- `usage`: The intended purpose of the formatted measurement.
- `numberFormatStyle`: The presentation style of the numeric value.

## See Also

### Creating a measurement format style
- [init(width: Measurement<UnitType>.FormatStyle.UnitWidth, locale: Locale, usage: MeasurementFormatUnitUsage<UnitType>, hidesScaleName: Bool, numberFormatStyle: FloatingPointFormatStyle<Double>?)](./init%28width,locale,usage,hidesscalename,numberformatstyle%29.md)
  Creates an instance using the provided width, locale, usage type, number format, and the option to hide the unit name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/init(width:locale:usage:numberformatstyle:))*