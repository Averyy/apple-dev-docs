# currentZoneDuration

**Framework**: HealthKit  
**Kind**: property

A property that contains the zone duration just entered.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@nonobjc
final var currentZoneDuration: HKWorkoutZoneDuration? { get }
```

#### Discussion

When this property is `nil`, no zone is currently active.

## See Also

- [var previousZoneDuration: HKWorkoutZoneDuration?](hkliveworkoutzoneupdate/previouszoneduration.md)
  A property that contains the zone duration that just completed.
- [var zoneGroup: HKWorkoutZoneGroup?](hkliveworkoutzoneupdate/zonegroup.md)
  The zone group that contains the current duration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutzoneupdate/currentzoneduration)*