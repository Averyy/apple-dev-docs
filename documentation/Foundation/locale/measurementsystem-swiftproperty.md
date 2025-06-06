# measurementSystem

**Framework**: Foundation  
**Kind**: property

The measurement system used by the locale, like metric or the US system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var measurementSystem: Locale.MeasurementSystem { get }
```

#### Discussion

When called on the special [`Locale`](locale.md) instances [`current`](locale/current.md) or [`autoupdatingCurrent`](locale/autoupdatingcurrent.md), if the user overrode the default measurement system, this property provides the user’s preference.

This property corresponds to the `ms` key of the Unicode BCP 47 extension.

For locale instances created with the `ms` specifier (such as `en-US@ms=metric`), or with a custom [`Locale.Components`](locale/components.md), this property represents the custom measurement system. Otherwise, it represents the locale’s default measurement system.

## See Also

- [var currency: Locale.Currency?](locale/currency-swift.property.md)
  The currency used by the locale.
- [Locale.Currency](locale/currency-swift.struct.md)
  A type that represents the currency system used by a locale, like dollars or euros.
- [Locale.MeasurementSystem](locale/measurementsystem-swift.struct.md)
  A type that represents the measurement system used by a locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem](locale/numberingsystem-swift.property.md)
  The numbering system used by the locale.
- [var availableNumberingSystems: [Locale.NumberingSystem]](locale/availablenumberingsystems.md)
  An array containing all the valid numbering systems for the locale.
- [Locale.NumberingSystem](locale/numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/measurementsystem-swift.property)*