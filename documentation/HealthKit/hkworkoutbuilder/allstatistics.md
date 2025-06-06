# allStatistics

**Framework**: HealthKit  
**Kind**: property

A dictionary that contains all the statistics for the workout builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var allStatistics: [HKQuantityType : HKStatistics] { get }
```

#### Discussion

HealthKit calculates an [`HKStatistics`](hkstatistics.md) object for each [`HKQuantityType`](hkquantitytype.md), based on the [`HKQuantitySample`](hkquantitysample.md) objects collected by the workout builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/allstatistics)*