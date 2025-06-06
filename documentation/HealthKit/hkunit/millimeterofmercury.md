# millimeterOfMercury()

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring pressure in millimeters of mercury.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func millimeterOfMercury() -> Self
```

#### Return Value

A HealthKit unit for measuring pressure in millimeters of mercury.

#### Discussion

One millimeter of mercury is the pressure needed to raise a column of mercury by 1 millimeter. Even through it is not an SI unit, the millimeter of mercury unit is used in many scientific fields. In HealthKit, it is commonly used to measure blood pressure.

## See Also

- [class func pascal() -> Self](hkunit/pascal.md)
  Returns a HealthKit unit for measuring pressure in pascals.
- [class func pascalUnit(with: HKMetricPrefix) -> Self](hkunit/pascalunit(with:).md)
  Returns a HealthKit unit for measuring pressure, using pascal units with the provided prefix.
- [class func inchesOfMercury() -> Self](hkunit/inchesofmercury.md)
  Returns a HealthKit unit for measuring pressure in inches of mercury.
- [class func centimeterOfWater() -> Self](hkunit/centimeterofwater.md)
  Returns a HealthKit unit for measuring pressure in centimeters of water.
- [class func atmosphere() -> Self](hkunit/atmosphere.md)
  Returns a HealthKit unit for measuring pressure in atmospheres.
- [class func decibelAWeightedSoundPressureLevel() -> Self](hkunit/decibelaweightedsoundpressurelevel.md)
  Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/millimeterofmercury())*