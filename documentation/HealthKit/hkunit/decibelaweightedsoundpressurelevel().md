# decibelAWeightedSoundPressureLevel()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func decibelAWeightedSoundPressureLevel() -> Self
```

```objc
+ (instancetype) decibelAWeightedSoundPressureLevelUnit;
```

## See Also

### Related Documentation
- [class func decibelHearingLevel() -> Self](./decibelhearinglevel%28%29.md)
  Returns a HealthKit unit for measuring the intensity of a sound.
### Constructing pressure units
- [class func pascal() -> Self](./pascal%28%29.md)
  Returns a HealthKit unit for measuring pressure in pascals.
- [class func pascalUnit(with: HKMetricPrefix) -> Self](./pascalunit%28with%29.md)
  Returns a HealthKit unit for measuring pressure, using pascal units with the provided prefix.
- [class func millimeterOfMercury() -> Self](./millimeterofmercury%28%29.md)
  Returns a HealthKit unit for measuring pressure in millimeters of mercury.
- [class func inchesOfMercury() -> Self](./inchesofmercury%28%29.md)
  Returns a HealthKit unit for measuring pressure in inches of mercury.
- [class func centimeterOfWater() -> Self](./centimeterofwater%28%29.md)
  Returns a HealthKit unit for measuring pressure in centimeters of water.
- [class func atmosphere() -> Self](./atmosphere%28%29.md)
  Returns a HealthKit unit for measuring pressure in atmospheres.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/decibelaweightedsoundpressurelevel())*