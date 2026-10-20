# relateWorkoutEffortSample(_:with:activity:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func relateWorkoutEffortSample(_ sample: HKSample, with workout: HKWorkout, activity: HKWorkoutActivity?, completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func relateWorkoutEffortSample(_ sample: HKSample, with workout: HKWorkout, activity: HKWorkoutActivity?) async throws -> Bool
```

```objc
- (void) relateWorkoutEffortSample:(HKSample *) sample withWorkout:(HKWorkout *) workout activity:(HKWorkoutActivity *) activity completion:(void (^)(BOOL success, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/relateworkouteffortsample(_:with:activity:completion:))*