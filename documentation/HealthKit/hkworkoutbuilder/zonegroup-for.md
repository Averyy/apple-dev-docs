# zoneGroup(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the current zone group for the specified quantity type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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

- [func setCustomZoneConfiguration(HKWorkoutZoneConfiguration?, for: HKQuantityType) async throws](hkworkoutbuilder/setcustomzoneconfiguration(_:for:).md)
  Overrides the preferred zone configuration with a custom zone for the current workout.
- [func zoneConfiguration(for: HKQuantityType) async throws -> HKWorkoutZoneConfiguration?](hkworkoutbuilder/zoneconfiguration(for:).md)
  Returns the zone configuration for the specified quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/zonegroup(for:))*