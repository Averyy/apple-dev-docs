# HKMetadataKeyAverageMETs

**Framework**: HealthKit  
**Kind**: var

A key that indicates the average Metabolic Equivalent of Task (METs) during a workout.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let HKMetadataKeyAverageMETs: String
```

#### Discussion

Set this key on a workout. Set its value to an [`HKQuantity`](hkquantity.md) object with a METs unit (for example, kcal/(kg*hr)). For more information on creating complex units, see Performing unit math.

The value represents the average intensity over the entire workout’s duration.

## See Also

- [let HKMetadataKeyPhysicalEffortEstimationType: String](hkmetadatakeyphysicaleffortestimationtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyaveragemets)*