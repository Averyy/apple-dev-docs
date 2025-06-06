# addPower

**Framework**: HealthKit  
**Kind**: property

The correction for nearsightedness.

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
var addPower: HKQuantity? { get }
```

#### Discussion

This quantity uses [`diopter()`](hkunit/diopter().md) units. The range is from 0.25 to 2.5. The right and left eyes should have the same value.

## See Also

- [var sphere: HKQuantity](hklensspecification/sphere.md)
  The correction for farsightedness.
- [var cylinder: HKQuantity?](hklensspecification/cylinder.md)
  Part of the correction for astigmatism that measures the strength of the correction.
- [var axis: HKQuantity?](hklensspecification/axis.md)
  Part of the correction for astigmatism that measures the orientation fo the correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hklensspecification/addpower)*