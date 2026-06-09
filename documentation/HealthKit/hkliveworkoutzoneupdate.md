# HKLiveWorkoutZoneUpdate

**Framework**: HealthKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS ?+
- watchOS 27.0+ (Beta)

## Declaration

```swift
class HKLiveWorkoutZoneUpdate
```

## Mentions

- [Accessing workout zone data](accessing-workout-zone-data.md)

## Topics

### Instance Properties
- [var currentZoneDuration: HKWorkoutZoneDuration?](hkliveworkoutzoneupdate/currentzoneduration.md)
  The new zone duration that has just been entered, or nil if no zone is active.
- [var lastSampleProcessedDate: Date?](hkliveworkoutzoneupdate/lastsampleprocesseddate.md)
  The timestamp of the most recent processed sample at the time of the update.
- [var previousZoneDuration: HKWorkoutZoneDuration?](hkliveworkoutzoneupdate/previouszoneduration.md)
  The new zone duration that has just been entered, or nil if no zone is active.
- [var zoneGroup: HKWorkoutZoneGroup?](hkliveworkoutzoneupdate/zonegroup.md)
  The complete zone group containing all current duration data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutzoneupdate)*