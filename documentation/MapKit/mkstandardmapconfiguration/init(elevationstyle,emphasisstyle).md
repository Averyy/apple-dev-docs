# init(elevationStyle:emphasisStyle:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a standard map configuration with the specified elevation and emphasis styles.

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
convenience init(elevationStyle: MKMapConfiguration.ElevationStyle, emphasisStyle: MKStandardMapConfiguration.EmphasisStyle)
```

```objc
- (instancetype) initWithElevationStyle:(MKMapElevationStyle) elevationStyle emphasisStyle:(MKStandardMapEmphasisStyle) emphasisStyle;
```

## Parameters

- `elevationStyle`: One of the [`MKMapConfiguration.ElevationStyle`](../mkmapconfiguration/elevationstyle-swift.enum.md) modes.
- `emphasisStyle`: One of the [`MKStandardMapConfiguration.EmphasisStyle`](./emphasisstyle-swift.enum.md) styles.

## See Also

### Creating a standard map configuration
- [init()](./init%28%29.md)
  Creates a new standard map configuration.
- [convenience init(elevationStyle: MKMapConfiguration.ElevationStyle)](./init%28elevationstyle%29.md)
  Creates a new standard map configuration with the specified elevation style.
- [convenience init(emphasisStyle: MKStandardMapConfiguration.EmphasisStyle)](./init%28emphasisstyle%29.md)
  Creates a standard map configuration with the specified emphasis style.
- [MKMapConfiguration.ElevationStyle](../mkmapconfiguration/elevationstyle-swift.enum.md)
  Values that control the map’s elevation style.
- [MKStandardMapConfiguration.EmphasisStyle](./emphasisstyle-swift.enum.md)
  Values that control how the framework emphasizes map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkstandardmapconfiguration/init(elevationstyle:emphasisstyle:))*