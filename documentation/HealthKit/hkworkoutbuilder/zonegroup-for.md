# zoneGroup(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the current zone group for the specified quantity type, including real-time duration calculations.

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

The zone group with current time-in-zone data, or nil if no zone information is available.

## Parameters

- `quantityType`: The quantity type to retrieve zone information for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/zonegroup(for:))*