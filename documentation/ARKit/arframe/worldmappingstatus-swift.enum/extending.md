# ARFrame.WorldMappingStatus.extending

**Framework**: ARKit  
**Kind**: case

World tracking has mapped recently visited areas, but is still mapping around the current device position.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case extending
```

#### Discussion

When the [`worldMappingStatus`](arframe/worldmappingstatus-swift.property.md) of the session’s [`currentFrame`](arsession/currentframe.md) is [`ARFrame.WorldMappingStatus.extending`](arframe/worldmappingstatus-swift.enum/extending.md), the session has produced a high-fidelity internal map of the real-world spaces the device has recently passed thorugh, but is still collecting data to map the area around the device’s current position and the scene visible to the camera.

This status provides moderate to high reliability for relocalizing to a saved world map, provided that:

1. You call [`getCurrentWorldMap(completionHandler:)`](arsession/getcurrentworldmap(completionhandler:).md) to save the world map while the status of the [`currentFrame`](arsession/currentframe.md) is [`ARFrame.WorldMappingStatus.extending`](arframe/worldmappingstatus-swift.enum/extending.md).
2. When you run a new session (later or on another device) from that [`ARWorldMap`](arworldmap.md), the device running the new session passes through positions and orientations that were visited by the device that saved the session.

Saving or sharing a world map at this time is likely to produce adequate results, but a higher quality world map may be possible if you wait until the user explores more of their surroundings and the status changes to [`ARFrame.WorldMappingStatus.mapped`](arframe/worldmappingstatus-swift.enum/mapped.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/worldmappingstatus-swift.enum/extending)*