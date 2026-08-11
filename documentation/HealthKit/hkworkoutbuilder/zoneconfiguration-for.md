# zoneConfiguration(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the zone configuration for the specified quantity type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func zoneConfiguration(for quantityType: HKQuantityType) async throws -> HKWorkoutZoneConfiguration?
```

#### Return Value

This method returns a custom configuration set by `setZoneConfiguration(_:for:)`, if it exists. Otherwise, this method returns the person’s preferred workout zone configuration from the health store.

#### Discussion

This method throws an error if the framework can’t retrieve a zone configuration for the given quantity type.

## Parameters

- `quantityType`: The quantity type for which to retrieve the configuration.

## See Also

- [func setCustomZoneConfiguration(HKWorkoutZoneConfiguration?, for: HKQuantityType) async throws](hkworkoutbuilder/setcustomzoneconfiguration(_:for:).md)
  Overrides the preferred zone configuration with a custom zone for the current workout.
- [func zoneGroup(for: HKQuantityType) -> HKWorkoutZoneGroup?](hkworkoutbuilder/zonegroup(for:).md)
  Returns the current zone group for the specified quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/zoneconfiguration(for:))*