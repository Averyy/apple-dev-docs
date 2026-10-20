# pascalUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring pressure, using pascal units with the provided prefix.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func pascalUnit(with prefix: HKMetricPrefix) -> Self
```

```objc
+ (instancetype) pascalUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

#### Return Value

A HealthKit unit for measuring pressure based on pascals and the provided prefix.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Constructing pressure units
- [class func pascal() -> Self](./pascal%28%29.md)
  Returns a HealthKit unit for measuring pressure in pascals.
- [class func millimeterOfMercury() -> Self](./millimeterofmercury%28%29.md)
  Returns a HealthKit unit for measuring pressure in millimeters of mercury.
- [class func inchesOfMercury() -> Self](./inchesofmercury%28%29.md)
  Returns a HealthKit unit for measuring pressure in inches of mercury.
- [class func centimeterOfWater() -> Self](./centimeterofwater%28%29.md)
  Returns a HealthKit unit for measuring pressure in centimeters of water.
- [class func atmosphere() -> Self](./atmosphere%28%29.md)
  Returns a HealthKit unit for measuring pressure in atmospheres.
- [class func decibelAWeightedSoundPressureLevel() -> Self](./decibelaweightedsoundpressurelevel%28%29.md)
  Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/pascalunit(with:))*