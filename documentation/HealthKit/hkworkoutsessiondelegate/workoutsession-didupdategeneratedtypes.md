# workoutSession(_:didUpdateGeneratedTypes:)

**Framework**: HealthKit  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
optional func workoutSession(_ workoutSession: HKWorkoutSession, didUpdateGeneratedTypes generatedTypes: Set<HKSampleType>)
```

#### Discussion

With new sample types added or removed, statistics for the currentGeneratedTypes may have changed and should be read again

## Parameters

- `workoutSession`: The workout data source which provides data for active workout session.
- `generatedTypes`: The full set of sample types that are currently generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:didupdategeneratedtypes:))*