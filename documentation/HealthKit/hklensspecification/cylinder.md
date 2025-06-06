# cylinder

**Framework**: HealthKit  
**Kind**: property

Part of the correction for astigmatism that measures the strength of the correction.

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
var cylinder: HKQuantity? { get }
```

#### Discussion

This quantity measures the strength of the correction in [`diopter()`](hkunit/diopter().md) units. The range is -3.0 to 3.0.

## See Also

- [var sphere: HKQuantity](hklensspecification/sphere.md)
  The correction for farsightedness.
- [var axis: HKQuantity?](hklensspecification/axis.md)
  Part of the correction for astigmatism that measures the orientation fo the correction.
- [var addPower: HKQuantity?](hklensspecification/addpower.md)
  The correction for nearsightedness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hklensspecification/cylinder)*