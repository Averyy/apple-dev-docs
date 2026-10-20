# MKStandardMapConfiguration.EmphasisStyle

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

Values that control how the framework emphasizes map features.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum EmphasisStyle
```

```c
enum MKStandardMapEmphasisStyle : NSInteger;
```

## Topics

### Controlling the map’s emphasis
- [MKStandardMapConfiguration.EmphasisStyle.default](./emphasisstyle-swift.enum/default.md)
  The default level of emphasis.
- [MKStandardMapConfiguration.EmphasisStyle.muted](./emphasisstyle-swift.enum/muted.md)
  The muted level of emphasis.
- [MKStandardMapConfiguration.EmphasisStyle.default](./emphasisstyle-swift.enum/default.md)
  The default level of emphasis.
- [MKStandardMapConfiguration.EmphasisStyle.muted](./emphasisstyle-swift.enum/muted.md)
  The muted level of emphasis.
### Initializers
- [init?(rawValue: Int)](./emphasisstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a standard map configuration
- [init()](./init%28%29.md)
  Creates a new standard map configuration.
- [convenience init(elevationStyle: MKMapConfiguration.ElevationStyle)](./init%28elevationstyle%29.md)
  Creates a new standard map configuration with the specified elevation style.
- [convenience init(elevationStyle: MKMapConfiguration.ElevationStyle, emphasisStyle: MKStandardMapConfiguration.EmphasisStyle)](./init%28elevationstyle,emphasisstyle%29.md)
  Creates a standard map configuration with the specified elevation and emphasis styles.
- [convenience init(emphasisStyle: MKStandardMapConfiguration.EmphasisStyle)](./init%28emphasisstyle%29.md)
  Creates a standard map configuration with the specified emphasis style.
- [MKMapConfiguration.ElevationStyle](../mkmapconfiguration/elevationstyle-swift.enum.md)
  Values that control the map’s elevation style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkstandardmapconfiguration/emphasisstyle-swift.enum)*