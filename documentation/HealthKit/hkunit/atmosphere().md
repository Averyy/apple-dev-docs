# atmosphere()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring pressure in atmospheres.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func atmosphere() -> Self
```

```objc
+ (instancetype) atmosphereUnit;
```

## Return Value

A HealthKit unit for measuring pressure in atmospheres.

## Discussion

One atmosphere is the average atmospheric pressure at sea level.

## See Also

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
- [class func decibelAWeightedSoundPressureLevel() -> Self](./decibelaweightedsoundpressurelevel%28%29.md)
  Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/atmosphere())*