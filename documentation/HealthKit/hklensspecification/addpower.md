# addPower

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) HKQuantity * addPower;
```

#### Discussion

This quantity uses [`diopter()`](../hkunit/diopter%28%29.md) units. The range is from 0.25 to 2.5. The right and left eyes should have the same value.

## See Also

### Accessing lens specification data
- [var sphere: HKQuantity](./sphere.md)
  The correction for farsightedness.
- [var cylinder: HKQuantity?](./cylinder.md)
  Part of the correction for astigmatism that measures the strength of the correction.
- [var axis: HKQuantity?](./axis.md)
  Part of the correction for astigmatism that measures the orientation fo the correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hklensspecification/addpower)*