# init(quantityType:zoneBoundaries:)

**Framework**: HealthKit  
**Kind**: init

Initializes a zone configuration from zone boundaries for the specified quantity type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(quantityType: HKQuantityType, zoneBoundaries: [HKQuantity]) throws
```

#### Return Value

A zone configuration with `source` set to `.app`.

#### Discussion

The system creates the individual zones based on the boundaries you provide. This method ensures that zones are contiguous and nonoverlapping. Call this method before calling [`setCustomZoneConfiguration(_:for:)`](hkworkoutbuilder/setcustomzoneconfiguration(_:for:).md) to apply custom zones to a workout.

## Parameters

- `quantityType`: The quantity type to which these zones apply.
- `zoneBoundaries`: An array of quantities that represent the upper boundaries of each zone, ordered from lowest to highest. The first zone has no lower bound, and the last zone has no upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration/init(quantitytype:zoneboundaries:))*