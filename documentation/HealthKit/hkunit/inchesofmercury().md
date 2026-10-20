# inchesOfMercury()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring pressure in inches of mercury.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func inchesOfMercury() -> Self
```

```objc
+ (instancetype) inchesOfMercuryUnit;
```

#### Return Value

A HealthKit unit for measuring pressure in inches of mercury.

## See Also

### Constructing pressure units
- [class func pascal() -> Self](./pascal%28%29.md)
  Returns a HealthKit unit for measuring pressure in pascals.
- [class func pascalUnit(with: HKMetricPrefix) -> Self](./pascalunit%28with%29.md)
  Returns a HealthKit unit for measuring pressure, using pascal units with the provided prefix.
- [class func millimeterOfMercury() -> Self](./millimeterofmercury%28%29.md)
  Returns a HealthKit unit for measuring pressure in millimeters of mercury.
- [class func centimeterOfWater() -> Self](./centimeterofwater%28%29.md)
  Returns a HealthKit unit for measuring pressure in centimeters of water.
- [class func atmosphere() -> Self](./atmosphere%28%29.md)
  Returns a HealthKit unit for measuring pressure in atmospheres.
- [class func decibelAWeightedSoundPressureLevel() -> Self](./decibelaweightedsoundpressurelevel%28%29.md)
  Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/inchesofmercury())*