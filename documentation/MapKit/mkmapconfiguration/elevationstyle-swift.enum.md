# MKMapConfiguration.ElevationStyle

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

Values that control the map’s elevation style.

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
enum ElevationStyle
```

```c
enum MKMapElevationStyle : NSInteger;
```

## Topics

### Constants
- [MKMapConfiguration.ElevationStyle.flat](./elevationstyle-swift.enum/flat.md)
  The value that represents the flat map elevation style.
- [MKMapConfiguration.ElevationStyle.realistic](./elevationstyle-swift.enum/realistic.md)
  The value that represents a map elevation style with realistic ground contours.
### Initializers
- [init?(rawValue: Int)](./elevationstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a hybrid map configuration
- [init()](../mkhybridmapconfiguration/init%28%29.md)
  Creates a new hybrid map configuration.
- [convenience init(elevationStyle: MKMapConfiguration.ElevationStyle)](../mkhybridmapconfiguration/init%28elevationstyle%29.md)
  Creates a new hybrid map configuration with the specified elevation style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapconfiguration/elevationstyle-swift.enum)*