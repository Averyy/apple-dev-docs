# sphere

**Framework**: HealthKit  
**Kind**: property

The correction for farsightedness.

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
var sphere: HKQuantity { get }
```

#### Discussion

This quantity uses [`diopter()`](hkunit/diopter().md) units. The range is -10.5 to +6.5.

## See Also

- [var cylinder: HKQuantity?](hklensspecification/cylinder.md)
  Part of the correction for astigmatism that measures the strength of the correction.
- [var axis: HKQuantity?](hklensspecification/axis.md)
  Part of the correction for astigmatism that measures the orientation fo the correction.
- [var addPower: HKQuantity?](hklensspecification/addpower.md)
  The correction for nearsightedness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hklensspecification/sphere)*