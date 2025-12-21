# MeasurementFormatter

**Framework**: Foundation  
**Kind**: class

A formatter that provides localized representations of units and measurements.

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
class MeasurementFormatter
```

#### Overview

You use the [`string(from:)`](measurementformatter/string(from:)-wt9y.md) method to create a localized representation of an [`NSMeasurement`](nsmeasurement.md) object, and you use the [`string(from:)`](measurementformatter/string(from:)-4hwjz.md) method to create a localized representation of an [`Unit`](unit.md) object. The formatter takes into account the specified [`locale`](measurementformatter/locale.md), [`unitStyle`](measurementformatter/unitstyle.md), and [`unitOptions`](measurementformatter/unitoptions-swift.property.md) when producing string representations of units and measurements.

> 💡 **Tip**:  In Swift, you can use [`Measurement.FormatStyle`](measurement/formatstyle.md) rather than [`MeasurementFormatter`](measurementformatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Topics

### Specifying the Format
- [var unitOptions: MeasurementFormatter.UnitOptions](measurementformatter/unitoptions-swift.property.md)
  The options for how the unit is formatted.
- [MeasurementFormatter.UnitOptions](measurementformatter/unitoptions-swift.struct.md)
  Measurement formatter options.
- [var unitStyle: Formatter.UnitStyle](measurementformatter/unitstyle.md)
  The unit style.
- [var locale: Locale!](measurementformatter/locale.md)
  The locale of the formatter.
- [var numberFormatter: NumberFormatter!](measurementformatter/numberformatter.md)
  The number formatter used to format the quantity of a measurement.
### Converting Measurements
- [func string(from: Measurement<Unit>) -> String](measurementformatter/string(from:)-wt9y.md)
  Creates and returns a localized string representation of the provided measurement.
- [func string<UnitType>(from: Measurement<UnitType>) -> String](measurementformatter/string(from:)-6rcb1.md)
  Creates and returns a localized string representation of the provided measurement.
- [func string(from: Unit) -> String](measurementformatter/string(from:)-4hwjz.md)
  Creates and returns a localized string representation of the provided unit of measure.

## Relationships

### Inherits From
- [Formatter](formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter)*