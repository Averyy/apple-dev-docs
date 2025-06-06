# pascalUnit(with:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring pressure, using pascal units with the provided prefix.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func pascalUnit(with prefix: HKMetricPrefix) -> Self
```

#### Return Value

A HealthKit unit for measuring pressure based on pascals and the provided prefix.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func pascal() -> Self](hkunit/pascal.md)
  Returns a HealthKit unit for measuring pressure in pascals.
- [class func millimeterOfMercury() -> Self](hkunit/millimeterofmercury.md)
  Returns a HealthKit unit for measuring pressure in millimeters of mercury.
- [class func inchesOfMercury() -> Self](hkunit/inchesofmercury.md)
  Returns a HealthKit unit for measuring pressure in inches of mercury.
- [class func centimeterOfWater() -> Self](hkunit/centimeterofwater.md)
  Returns a HealthKit unit for measuring pressure in centimeters of water.
- [class func atmosphere() -> Self](hkunit/atmosphere.md)
  Returns a HealthKit unit for measuring pressure in atmospheres.
- [class func decibelAWeightedSoundPressureLevel() -> Self](hkunit/decibelaweightedsoundpressurelevel.md)
  Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/pascalunit(with:))*