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

The zone configuration, or `nil` if no configuration exists for the quantity type.

#### Discussion

This method returns any custom configuration set with [`setCustomZoneConfiguration(_:for:)`](hkworkoutbuilder/setcustomzoneconfiguration(_:for:).md), or the person’s preferred configuration if no custom configuration has been set.

## Parameters

- `quantityType`: The quantity type for which to retrieve the configuration.

## See Also

- [func setCustomZoneConfiguration(HKWorkoutZoneConfiguration?, for: HKQuantityType) async throws](hkworkoutbuilder/setcustomzoneconfiguration(_:for:).md)
  Sets the zone configuration for the specified quantity type for this workout. In order to provide a custom workout zone configuration, this must be called before beginning collection on the builder. If a custom configuration is not provided, the user’s preferred workout zone configuration will be used for zone calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/zoneconfiguration(for:))*