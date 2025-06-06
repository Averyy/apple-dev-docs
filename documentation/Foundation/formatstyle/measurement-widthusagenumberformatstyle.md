# measurement(width:usage:numberFormatStyle:)

**Framework**: Foundation  
**Kind**: method

Returns a format style to format measurement units.

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
static func measurement<UnitType>(width: Measurement<UnitType>.FormatStyle.UnitWidth, usage: MeasurementFormatUnitUsage<UnitType> = .general, numberFormatStyle: FloatingPointFormatStyle<Double>? = nil) -> Self where Self == Measurement<UnitType>.FormatStyle, UnitType : Dimension
```

#### Return Value

A format style that formats measurements according to the given parameters.

#### Discussion

Use the dot-notation form of this type method when the call point allows the use of [`Measurement.FormatStyle`](measurement/formatstyle.md). You typically do this when calling the [`formatted(_:)`](measurement/formatted(_:).md) method of [`Measurement`](measurement.md).

The following example creates an array of [`Measurement`](measurement.md) values that represent distances measured in kilometers. It then uses [`formatted(_:)`](measurement/formatted(_:).md) and the format style provided by this method to format the distances. The style specifies the [`asProvided`](measurementformatunitusage/asprovided.md) usage to keep the formatted measurements in kilometers. Without this, a non-Metric locale such as the US would convert the kilometers to a locale-appropriate unit, such as miles.

```swift
let rawDistances: [Double] = [100, 1000, 10000, 100000, 1000000]
let distances = rawDistances.map { Measurement(value: $0, unit: UnitLength.kilometers) }
let formattedDistances = distances.map { $0.formatted(
    .measurement(width: .narrow,
                 usage: .asProvided,
                 numberFormatStyle: .number)) } // ["100km", "1,000km", "10,000km", "100,000km", "1,000,000km"]
```

## Parameters

- `width`: The width — such as full names or abbreviations — with which to present units.
- `usage`: The contextual usage of the measurement unit, such as whether a length measurement applies to a road distance or a person’s height.
- `numberFormatStyle`: The format style with which to format the numeric part of the measurement.

## See Also

- [static func measurement(width: Measurement<UnitTemperature>.FormatStyle.UnitWidth, usage: MeasurementFormatUnitUsage<UnitTemperature>, hidesScaleName: Bool, numberFormatStyle: FloatingPointFormatStyle<Double>?) -> Self](formatstyle/measurement(width:usage:hidesscalename:numberformatstyle:).md)
  Returns a format style to format temperature units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/measurement(width:usage:numberformatstyle:))*