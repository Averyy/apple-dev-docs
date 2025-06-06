# measurement(width:usage:hidesScaleName:numberFormatStyle:)

**Framework**: Foundation  
**Kind**: method

Returns a format style to format temperature units.

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
static func measurement(width: Measurement<UnitTemperature>.FormatStyle.UnitWidth = .abbreviated, usage: MeasurementFormatUnitUsage<UnitTemperature> = .general, hidesScaleName: Bool = false, numberFormatStyle: FloatingPointFormatStyle<Double>? = nil) -> Self where Self == Measurement<UnitTemperature>.FormatStyle
```

#### Return Value

A format style that formats measurements according to the given parameters.

#### Discussion

Use this static method when the call point allows the use of [`Measurement.FormatStyle`](measurement/formatstyle.md) and the value type is `Measurement<UnitTemperature>`. You typically do this when calling the [`formatted(_:)`](measurement/formatted(_:).md) method of [`Measurement`](measurement.md).

The following example creates an array of [`Measurement`](measurement.md) values that represent body temperatures from a human patient. It then uses [`formatted(_:)`](measurement/formatted(_:).md) and the format style provided by this method to format the distances. The style specifies the [`person`](measurementformatunitusage/person-4ifk7.md) usage to clarify that the temperatures refer to a person’s body temperature, as opposed to other uses like weather.

```swift
let rawTemparatures: [Double] = [36.4, 36.6, 37.0, 36.9, 36.7]
let temperatures = rawTemparatures.map { Measurement(value: $0, unit: UnitTemperature.celsius) }
let formattedTemperatures = temperatures.map { $0.formatted(
    .measurement(width: .abbreviated,
                 usage: .person,
                 hidesScaleName: false,
                 numberFormatStyle: .number)) } // ["36.4°C", "36.6°C", "37°C", "36.9°C", "36.7°C"]
```

## Parameters

- `width`: The width — such as full names or abbreviations — with which to present units.
- `usage`: The contextual usage of the measurement unit, such as whether a temperature applies to a person or to the weather.
- `hidesScaleName`: A Boolean value that directs the formatter to hide the name of the scale (Kelvin, degrees Celsius, or degrees Fahrenheit). Defaults to  .
- `numberFormatStyle`: The format style with which to format the numeric part of the temperature.

## See Also

- [static func measurement<UnitType>(width: Measurement<UnitType>.FormatStyle.UnitWidth, usage: MeasurementFormatUnitUsage<UnitType>, numberFormatStyle: FloatingPointFormatStyle<Double>?) -> Self](formatstyle/measurement(width:usage:numberformatstyle:).md)
  Returns a format style to format measurement units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/measurement(width:usage:hidesscalename:numberformatstyle:))*