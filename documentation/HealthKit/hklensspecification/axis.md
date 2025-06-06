# axis

**Framework**: HealthKit  
**Kind**: property

Part of the correction for astigmatism that measures the orientation fo the correction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var axis: HKQuantity? { get }
```

#### Discussion

This quantity measures the orientation of the correction in [`degreeAngle()`](hkunit/degreeangle().md) units.

## See Also

- [var sphere: HKQuantity](hklensspecification/sphere.md)
  The correction for farsightedness.
- [var cylinder: HKQuantity?](hklensspecification/cylinder.md)
  Part of the correction for astigmatism that measures the strength of the correction.
- [var addPower: HKQuantity?](hklensspecification/addpower.md)
  The correction for nearsightedness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hklensspecification/axis)*