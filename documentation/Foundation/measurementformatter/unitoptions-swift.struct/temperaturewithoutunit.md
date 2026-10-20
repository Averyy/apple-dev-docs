# temperatureWithoutUnit

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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
static var temperatureWithoutUnit: MeasurementFormatter.UnitOptions { get }
```

```c
NSMeasurementFormatterUnitOptionsTemperatureWithoutUnit
```

#### Discussion

Specifies that representations of a measurement with the `NSTemperatureUnit` unit omit the letter denoting the temperature scale. For example, a temperature measurement with value equal to 72 using the [`degreeFahrenheit()`](../../../HealthKit/hkunit/degreefahrenheit%28%29.md) would be represented as `72°` rather than `72°F`.

## See Also

### Working with options
- [static var providedUnit: MeasurementFormatter.UnitOptions](./providedunit.md)
- [static var naturalScale: MeasurementFormatter.UnitOptions](./naturalscale.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter/unitoptions-swift.struct/temperaturewithoutunit)*