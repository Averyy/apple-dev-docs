# setCustomZoneConfiguration(_:for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Overrides the preferred zone configuration with a custom zone for the current workout.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func setCustomZoneConfiguration(_ configuration: HKWorkoutZoneConfiguration?, for quantityType: HKQuantityType) async throws
```

## Mentions

- [Accessing workout zone data](../accessing-workout-zone-data.md)

#### Discussion

Call this method before calling [`beginCollection(withStart:completion:)`](./begincollection%28withstart,completion%29.md) to apply custom zones. If you don’t set a custom configuration, the system uses the person’s preferred zone configuration from Health Settings for zone calculations. Custom configurations apply only to this workout and don’t modify the person’s preferred zones.

## Parameters

- `configuration`: The zone configuration to use, or `nil` to remove any custom configuration and use the person’s preferred zones.
- `quantityType`: The quantity type to which to apply the configuration.

## See Also

### Configuring zone data
- [func zoneConfiguration(for: HKQuantityType) async throws -> HKWorkoutZoneConfiguration?](./zoneconfiguration%28for%29.md)
  Returns the zone configuration for the specified quantity type.
- [func zoneGroup(for: HKQuantityType) -> HKWorkoutZoneGroup?](./zonegroup%28for%29.md)
  Returns the current zone group for the specified quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/setcustomzoneconfiguration(_:for:))*