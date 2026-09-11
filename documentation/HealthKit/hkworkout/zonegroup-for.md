# zoneGroup(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the current zone group for the specified quantity type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func zoneGroup(for quantityType: HKQuantityType) -> HKWorkoutZoneGroup?
```

#### Return Value

The zone group with current time-in-zone data, or `nil` if no zone information is available.

#### Discussion

This method provides real-time zone duration calculations during an active workout. The durations update as the system processes new samples.

## Parameters

- `quantityType`: The quantity type for which to retrieve zone information.

## See Also

- [var zoneGroupsByType: [HKQuantityType : HKWorkoutZoneGroup]?](hkworkout/zonegroupsbytype.md)
  A property that contains a dictionary that maps quantity types to their zone groups for this workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/zonegroup(for:))*