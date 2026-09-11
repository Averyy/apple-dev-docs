# zones

**Framework**: HealthKit  
**Kind**: property

A property that contains the workout zones, ordered from lowest to highest threshold.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
let zones: [HKWorkoutZone]
```

#### Discussion

Each zone in this array represents a contiguous range within the configuration.

## See Also

- [var quantityType: HKQuantityType](hkworkoutzoneconfiguration/quantitytype.md)
  A property that specifies the quantity type to which the zones apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration/zones)*