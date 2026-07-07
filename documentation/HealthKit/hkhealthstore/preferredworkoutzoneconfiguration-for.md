# preferredWorkoutZoneConfiguration(for:)

**Framework**: HealthKit  
**Kind**: method

Returns someone’s preferred zone configuration for the specified quantity type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func preferredWorkoutZoneConfiguration(for quantityType: HKQuantityType) async throws -> HKWorkoutZoneConfiguration?
```

## Mentions

- [Accessing workout zone data](accessing-workout-zone-data.md)

#### Return Value

The preferred zone configuration, or `nil` if the person hasn’t configured zones for the quantity type.

#### Discussion

The system returns the person’s manually configured zones from Health Settings, or the system-generated zones if the person hasn’t set custom values. System-generated zones update periodically as the person’s health metrics change, while zones configured by the person remain constant until modified. Apps can use this method to display zone information that aligns with the person’s preferences across all workouts.

> **Note**:  An error if the zone configuration can’t be retrieved.

## Parameters

- `quantityType`: The quantity type for which to retrieve the preferred zone configuration.

## See Also

- [func preferredUnits(for: Set<HKQuantityType>, completion: ([HKQuantityType : HKUnit], (any Error)?) -> Void)](hkhealthstore/preferredunits(for:completion:).md)
  Returns the user’s preferred units for the given quantity types.
- [static let HKUserPreferencesDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/HKUserPreferencesDidChange.md)
  Notifies observers whenever the user changes his or her preferred units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/preferredworkoutzoneconfiguration(for:))*