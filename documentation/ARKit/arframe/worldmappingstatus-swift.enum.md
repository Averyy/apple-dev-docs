# ARFrame.WorldMappingStatus

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

A value describing the world mapping status for the area visible in a given frame.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
enum WorldMappingStatus
```

```c
enum ARWorldMappingStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [ARFrame.WorldMappingStatus.extending](./worldmappingstatus-swift.enum/extending.md)
  World tracking has mapped recently visited areas, but is still mapping around the current device position.
- [ARFrame.WorldMappingStatus.limited](./worldmappingstatus-swift.enum/limited.md)
  World tracking has not yet sufficiently mapped the area around the current device position.
- [ARFrame.WorldMappingStatus.mapped](./worldmappingstatus-swift.enum/mapped.md)
  World tracking has adequately mapped the visible area.
- [ARFrame.WorldMappingStatus.notAvailable](./worldmappingstatus-swift.enum/notavailable.md)
  No world map is available.
### Initializers
- [init?(rawValue: Int)](./worldmappingstatus-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking world-mapping status
- [var worldMappingStatus: ARFrame.WorldMappingStatus](./worldmappingstatus-swift.property.md)
  The feasibility of generating or relocalizing a world map for this frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/worldmappingstatus-swift.enum)*