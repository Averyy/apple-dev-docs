# Measurement.FormatStyle

**Framework**: Foundation  
**Kind**: struct

A type that provides localized representations of measurements.

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
struct FormatStyle
```

#### Overview

A measurement format style creates human-readable text from a [`Measurement`](measurement.md). You can customize the formatting behavior of the format style using the [`width`](measurement/formatstyle/width.md), `numberFormat`, [`usage`](measurement/formatstyle/usage.md), and [`locale`](measurement/formatstyle/locale.md) properties. The system automatically caches unique configurations of [`Measurement.FormatStyle`](measurement/formatstyle.md) to enhance performance.

Use either the [`formatted()`](measurement/formatted().md) or the [`formatted(_:)`](measurement/formatted(_:).md) instance method of [`Measurement`](measurement.md) to create a string representation of a measurement.

The [`formatted()`](measurement/formatted().md) method generates a string using the default measurement format style.

```swift
let temperature = Measurement<UnitTemperature>(value: 38, unit: .celsius)
temperature.formatted()
// For locale: en_US: 100°F
// For locale: fr_FR: 38°C
```

The default format style in the previous example abbreviates the measurement unit. To customize any of the properties of the formatted measurement, you provide a measurement format style to the [`formatted(_:)`](measurement/formatted(_:).md) method. For example, to create a string with the full name of the unit, the code might resemble the following:

```swift
temperature.formatted(.measurement(width: .wide))
// For locale: en_US: 100 degrees Fahrenheit
// For locale: fr_FR: 38 degrés Celsius
```

The previous example uses a static factory method to create a measurement format style within the call to the [`formatted(_:)`](measurement/formatted(_:).md) method. You can also create a measurement format style and pass it to the method, such as in the following example:

```swift
let distance = Measurement<UnitLength>(value: 36, unit: .miles)
let distanceStyle = Measurement<UnitLength>.FormatStyle(width: .wide, usage: .road)
distanceStyle.format(distance)
// for locale: en_US: 36 miles
// for locale: fr_FR: 58 kilomètres

```

After you create an instance of a format style, you can use it to format measurements of the same unit type.

## Topics

### Creating a measurement format style
- [init(width: Measurement<UnitType>.FormatStyle.UnitWidth, locale: Locale, usage: MeasurementFormatUnitUsage<UnitType>, numberFormatStyle: FloatingPointFormatStyle<Double>?)](measurement/formatstyle/init(width:locale:usage:numberformatstyle:).md)
  Creates an instance using the provided width, locale, usage type, and number format.
- [init(width: Measurement<UnitType>.FormatStyle.UnitWidth, locale: Locale, usage: MeasurementFormatUnitUsage<UnitType>, hidesScaleName: Bool, numberFormatStyle: FloatingPointFormatStyle<Double>?)](measurement/formatstyle/init(width:locale:usage:hidesscalename:numberformatstyle:).md)
  Creates an instance using the provided width, locale, usage type, number format, and the option to hide the unit name.
### Modifying a measurement format style
- [var width: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/width.md)
  The width of the measurement unit.
- [Measurement.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth.md)
  Specifies the width of the unit, determining the textual representation.
- [var numberFormatStyle: FloatingPointFormatStyle<Double>?](measurement/formatstyle/numberformatstyle.md)
  The formatting of the measurement value.
- [var usage: MeasurementFormatUnitUsage<UnitType>?](measurement/formatstyle/usage.md)
  The intended purpose of the formatted measurement.
- [var hidesScaleName: Bool](measurement/formatstyle/hidesscalename.md)
  The visibility of the unit name of a temperature.
- [var locale: Locale](measurement/formatstyle/locale.md)
  The locale of the format style.
### Inspecting a measurement format style
- [var attributed: Measurement<UnitType>.AttributedStyle](measurement/formatstyle/attributed.md)
  The attributed style for the measurement format style.
### Applying byte count styles
- [Measurement.FormatStyle.ByteCount](measurement/formatstyle/bytecount.md)
  A format style that provides string representations of byte counts, expressed as measurements of information storage.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle)*