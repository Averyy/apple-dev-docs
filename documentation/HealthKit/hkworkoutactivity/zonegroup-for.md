# zoneGroup(for:)

**Framework**: HealthKit  
**Kind**: method

Returns a zone group for the specified quantity type.

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

The zone group for the quantity type, or `nil` if no zone information exists for the given type.

## Parameters

- `quantityType`: The quantity type for which to retrieve zone information.

## See Also

- [var zoneGroupsByType: [HKQuantityType : HKWorkoutZoneGroup]?](hkworkoutactivity/zonegroupsbytype.md)
  A property that contains a dictionary that maps quantity types to their zone groups for this activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/zonegroup(for:))*