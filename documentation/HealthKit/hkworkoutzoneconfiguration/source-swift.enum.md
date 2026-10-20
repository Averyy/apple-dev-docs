# HKWorkoutZoneConfiguration.Source

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that identifies the origin of the zone configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Source
```

## Topics

### Identifying the source
- [HKWorkoutZoneConfiguration.Source.system](./source-swift.enum/system.md)
  A case that indicates the system generated the zones automatically.
- [HKWorkoutZoneConfiguration.Source.user](./source-swift.enum/user.md)
  A case that indicates the person configured the zones manually in Health Settings.
- [HKWorkoutZoneConfiguration.Source.app](./source-swift.enum/app.md)
  A case that indicates an app provided the zones for a specific workout.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying the configuration source
- [let source: HKWorkoutZoneConfiguration.Source](./source-swift.property.md)
  A property that identifies the origin of this zone configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration/source-swift.enum)*