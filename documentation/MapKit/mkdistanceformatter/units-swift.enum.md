# MKDistanceFormatter.Units

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

Constants that reflect the type of units to use in the string.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Units
```

```c
enum MKDistanceFormatterUnits : NSUInteger;
```

## Topics

### Constants
- [MKDistanceFormatter.Units.default](./units-swift.enum/default.md)
  The format uses the locale information to determine which units to use.
- [MKDistanceFormatter.Units.metric](./units-swift.enum/metric.md)
  The format uses metric units.
- [MKDistanceFormatter.Units.imperial](./units-swift.enum/imperial.md)
  The format uses imperial units.
- [MKDistanceFormatter.Units.imperialWithYards](./units-swift.enum/imperialwithyards.md)
  The format uses imperial units that include measurements in yards.
- [MKDistanceFormatter.Units.default](./units-swift.enum/default.md)
  The format uses the locale information to determine which units to use.
- [MKDistanceFormatter.Units.metric](./units-swift.enum/metric.md)
  The format uses metric units.
- [MKDistanceFormatter.Units.imperial](./units-swift.enum/imperial.md)
  The format uses imperial units.
- [MKDistanceFormatter.Units.imperialWithYards](./units-swift.enum/imperialwithyards.md)
  The format uses imperial units that include measurements in yards.
### Initializers
- [init?(rawValue: UInt)](./units-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the format
- [var locale: Locale!](./locale.md)
  The locale to use when formatting strings.
- [var units: MKDistanceFormatter.Units](./units-swift.property.md)
  The measuring system — imperial or metric — to use for units.
- [var unitStyle: MKDistanceFormatter.DistanceUnitStyle](./unitstyle.md)
  The preferred style for units.
- [MKDistanceFormatter.DistanceUnitStyle](./distanceunitstyle.md)
  Constants that indicate the format style to use for strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/units-swift.enum)*