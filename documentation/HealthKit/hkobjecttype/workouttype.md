# workoutType()

**Framework**: HealthKit  
**Kind**: method

Returns the shared [`HKWorkoutType`](hkworkouttype.md) object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func workoutType() -> HKWorkoutType
```

#### Return Value

The shared [`HKWorkoutType`](hkworkouttype.md) instance.

#### Discussion

This method returns an instance of the [`HKWorkoutType`](hkworkouttype.md) concrete subclass. HealthKit uses workout types to create samples that store information about individual workouts. Use workout type instances to create workout objects that you can save in the HealthKit store.  For more information, see [`HKWorkoutType`](hkworkouttype.md).

In HealthKit, all workouts use the same workout type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/workouttype())*