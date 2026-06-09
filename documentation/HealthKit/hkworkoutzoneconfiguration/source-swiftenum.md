# HKWorkoutZoneConfiguration.Source

**Framework**: HealthKit  
**Kind**: enum

An enumeration that identifies the origin of the zone configuration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Source
```

## Topics

### Identifying the source
- [HKWorkoutZoneConfiguration.Source.system](hkworkoutzoneconfiguration/source-swift.enum/system.md)
  A case that indicates the system generated the zones automatically.
- [HKWorkoutZoneConfiguration.Source.user](hkworkoutzoneconfiguration/source-swift.enum/user.md)
  A case that indicates the person configured the zones manually in Health Settings.
- [HKWorkoutZoneConfiguration.Source.app](hkworkoutzoneconfiguration/source-swift.enum/app.md)
  A case that indicates an app provided the zones for a specific workout.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let source: HKWorkoutZoneConfiguration.Source](hkworkoutzoneconfiguration/source-swift.property.md)
  A property that identifies the origin of this zone configuration.
- [var configurationType: HKWorkoutZoneConfiguration.ConfigurationType](hkworkoutzoneconfiguration/configurationtype-swift.property.md)
  A property that identifies the origin of this zone configuration.
- [HKWorkoutZoneConfiguration.ConfigurationType](hkworkoutzoneconfiguration/configurationtype-swift.enum.md)
  An enumeration that identifies the origin of the zone configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration/source-swift.enum)*