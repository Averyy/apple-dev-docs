# zones

**Framework**: HealthKit  
**Kind**: property

A property that contains the workout zones, ordered from lowest to highest threshold.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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