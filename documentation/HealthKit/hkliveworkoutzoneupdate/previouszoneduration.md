# previousZoneDuration

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A property that contains the zone duration that just completed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- watchOS 27.0+

## Declaration

```swift
@nonobjc
final var previousZoneDuration: HKWorkoutZoneDuration? { get }
```

## Discussion

When this property contains `nil`, it’s the first zone entry for the workout.

## See Also

### Accessing zone data
- [var currentZoneDuration: HKWorkoutZoneDuration?](./currentzoneduration.md)
  A property that contains the zone duration just entered.
- [var zoneGroup: HKWorkoutZoneGroup?](./zonegroup.md)
  The zone group that contains the current duration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutzoneupdate/previouszoneduration)*