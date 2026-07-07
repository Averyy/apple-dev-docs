# setCustomZoneConfiguration(_:for:)

**Framework**: HealthKit  
**Kind**: method

Sets the zone configuration for the specified quantity type for this workout. In order to provide a custom workout zone configuration, this must be called before beginning collection on the builder. If a custom configuration is not provided, the user’s preferred workout zone configuration will be used for zone calculations.

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

> **Note**: An error if the configuration cannot be set or is incompatible with the quantity type.

## Parameters

- `configuration`: The zone configuration to use. Setting to `nil` will remove any custom configuration and use the preferred zone configuration for the quantity type.
- `quantityType`: The quantity type to apply the configuration to.

## See Also

- [func zoneConfiguration(for: HKQuantityType) async throws -> HKWorkoutZoneConfiguration?](hkworkoutbuilder/zoneconfiguration(for:).md)
  Returns the zone configuration for the specified quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/setcustomzoneconfiguration(_:for:))*