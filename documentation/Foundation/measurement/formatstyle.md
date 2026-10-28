# Measurement.FormatStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

Available when `UnitType` inherits `Dimension`.

## Overview

A measurement format style creates human-readable text from a [`Measurement`](../measurement.md). You can customize the formatting behavior of the format style using the [`width`](./formatstyle/width.md), `numberFormat`, [`usage`](./formatstyle/usage.md), and [`locale`](./formatstyle/locale.md) properties. The system automatically caches unique configurations of [`Measurement.FormatStyle`](./formatstyle.md) to enhance performance.

Use either the [`formatted()`](./formatted%28%29.md) or the [`formatted(_:)`](./formatted%28_%29.md) instance method of [`Measurement`](../measurement.md) to create a string representation of a measurement.

The [`formatted()`](./formatted%28%29.md) method generates a string using the default measurement format style.

```swift
let temperature = Measurement<UnitTemperature>(value: 38, unit: .celsius)
temperature.formatted()
// For locale: en_US: 100°F
// For locale: fr_FR: 38°C
```

The default format style in the previous example abbreviates the measurement unit. To customize any of the properties of the formatted measurement, you provide a measurement format style to the [`formatted(_:)`](./formatted%28_%29.md) method. For example, to create a string with the full name of the unit, the code might resemble the following:

```swift
temperature.formatted(.measurement(width: .wide))
// For locale: en_US: 100 degrees Fahrenheit
// For locale: fr_FR: 38 degrés Celsius
```

The previous example uses a static factory method to create a measurement format style within the call to the [`formatted(_:)`](./formatted%28_%29.md) method. You can also create a measurement format style and pass it to the method, such as in the following example:

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
- [init(width: Measurement<UnitType>.FormatStyle.UnitWidth, locale: Locale, usage: MeasurementFormatUnitUsage<UnitType>, numberFormatStyle: FloatingPointFormatStyle<Double>?)](./formatstyle/init%28width,locale,usage,numberformatstyle%29.md)
  Creates an instance using the provided width, locale, usage type, and number format.
- [init(width: Measurement<UnitType>.FormatStyle.UnitWidth, locale: Locale, usage: MeasurementFormatUnitUsage<UnitType>, hidesScaleName: Bool, numberFormatStyle: FloatingPointFormatStyle<Double>?)](./formatstyle/init%28width,locale,usage,hidesscalename,numberformatstyle%29.md)
  Creates an instance using the provided width, locale, usage type, number format, and the option to hide the unit name.
### Modifying a measurement format style
- [var width: Measurement<UnitType>.FormatStyle.UnitWidth](./formatstyle/width.md)
  The width of the measurement unit.
- [Measurement.FormatStyle.UnitWidth](./formatstyle/unitwidth.md)
  Specifies the width of the unit, determining the textual representation.
- [var numberFormatStyle: FloatingPointFormatStyle<Double>?](./formatstyle/numberformatstyle.md)
  The formatting of the measurement value.
- [var usage: MeasurementFormatUnitUsage<UnitType>?](./formatstyle/usage.md)
  The intended purpose of the formatted measurement.
- [var hidesScaleName: Bool](./formatstyle/hidesscalename.md)
  The visibility of the unit name of a temperature.
- [var locale: Locale](./formatstyle/locale.md)
  The locale of the format style.
- [func locale(Locale) -> Measurement<UnitType>.FormatStyle](./formatstyle/locale%28_%29.md)
  Modifies the measurement format style to use the specified locale.
### Inspecting a measurement format style
- [var attributed: Measurement<UnitType>.AttributedStyle](./formatstyle/attributed.md)
  The attributed style for the measurement format style.
### Formatting a measurement
- [func format(Measurement<UnitType>) -> String](./formatstyle/format%28_%29.md)
  Creates a string representation of a measurement.
### Applying byte count styles
- [Measurement.FormatStyle.ByteCount](./formatstyle/bytecount.md)
  A format style that provides string representations of byte counts, expressed as measurements of information storage.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [FormatStyle](../formatstyle.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle)*