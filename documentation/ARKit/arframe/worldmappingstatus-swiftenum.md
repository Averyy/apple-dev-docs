# ARFrame.WorldMappingStatus

**Framework**: ARKit  
**Kind**: enum

A value describing the world mapping status for the area visible in a given frame.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum WorldMappingStatus
```

## Topics

### Enumeration Cases
- [ARFrame.WorldMappingStatus.extending](arframe/worldmappingstatus-swift.enum/extending.md)
  World tracking has mapped recently visited areas, but is still mapping around the current device position.
- [ARFrame.WorldMappingStatus.limited](arframe/worldmappingstatus-swift.enum/limited.md)
  World tracking has not yet sufficiently mapped the area around the current device position.
- [ARFrame.WorldMappingStatus.mapped](arframe/worldmappingstatus-swift.enum/mapped.md)
  World tracking has adequately mapped the visible area.
- [ARFrame.WorldMappingStatus.notAvailable](arframe/worldmappingstatus-swift.enum/notavailable.md)
  No world map is available.
### Initializers
- [init?(rawValue: Int)](arframe/worldmappingstatus-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var worldMappingStatus: ARFrame.WorldMappingStatus](arframe/worldmappingstatus-swift.property.md)
  The feasibility of generating or relocalizing a world map for this frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/worldmappingstatus-swift.enum)*