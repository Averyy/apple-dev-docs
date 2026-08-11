# setCustomZoneConfiguration(_:for:)

**Framework**: HealthKit  
**Kind**: method

Overrides the preferred zone configuration with a custom zone for the current workout.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func setCustomZoneConfiguration(_ configuration: HKWorkoutZoneConfiguration?, for quantityType: HKQuantityType) async throws
```

## Mentions

- [Accessing workout zone data](accessing-workout-zone-data.md)

#### Discussion

Call this method before calling [`beginCollection(withStart:completion:)`](hkworkoutbuilder/begincollection(withstart:completion:).md) to apply custom zones. If you don’t set a custom configuration, the system uses the person’s preferred zone configuration from Health Settings for zone calculations. Custom configurations apply only to this workout and don’t modify the person’s preferred zones.

## Parameters

- `configuration`: The zone configuration to use, or `nil` to remove any custom configuration and use the person’s preferred zones.
- `quantityType`: The quantity type to which to apply the configuration.

## See Also

- [func zoneConfiguration(for: HKQuantityType) async throws -> HKWorkoutZoneConfiguration?](hkworkoutbuilder/zoneconfiguration(for:).md)
  Returns the zone configuration for the specified quantity type.
- [func zoneGroup(for: HKQuantityType) -> HKWorkoutZoneGroup?](hkworkoutbuilder/zonegroup(for:).md)
  Returns the current zone group for the specified quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/setcustomzoneconfiguration(_:for:))*