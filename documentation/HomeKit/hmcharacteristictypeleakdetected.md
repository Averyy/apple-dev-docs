# HMCharacteristicTypeLeakDetected

**Framework**: HomeKit  
**Kind**: var

A leak detection indicator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeLeakDetected: String
```

#### Discussion

The corresponding value is one of the constants in the [`HMCharacteristicValueLeakStatus`](hmcharacteristicvalueleakstatus.md) enumeration. This characteristic typically applies to water, but can also be used for other fluids, like natural gas.

## Topics

### Values
- [enum HMCharacteristicValueLeakStatus](hmcharacteristicvalueleakstatus.md)
  Possible values for leak detection.

## See Also

- [let HMCharacteristicTypeWaterLevel: String](hmcharacteristictypewaterlevel.md)
  The water level measured by an accessory.
- [let HMCharacteristicTypeValveType: String](hmcharacteristictypevalvetype.md)
  The type of automated valve that controls fluid flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypeleakdetected)*