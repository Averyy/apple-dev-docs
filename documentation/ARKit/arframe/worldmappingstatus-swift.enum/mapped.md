# ARFrame.WorldMappingStatus.mapped

**Framework**: ARKit  
**Kind**: case

World tracking has adequately mapped the visible area.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case mapped
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Discussion

When the [`worldMappingStatus`](arframe/worldmappingstatus-swift.property.md) of the session’s [`currentFrame`](arsession/currentframe.md) is [`ARFrame.WorldMappingStatus.mapped`](arframe/worldmappingstatus-swift.enum/mapped.md), the session has produced a high-fidelity internal map of the real-world space around the device’s current position and the scene visible to the camera.

This status provides the highest reliability for relocalizing to a saved world map, provided that:

1. You call [`getCurrentWorldMap(completionHandler:)`](arsession/getcurrentworldmap(completionhandler:).md) to save the world map while the status of the [`currentFrame`](arsession/currentframe.md) is [`ARFrame.WorldMappingStatus.mapped`](arframe/worldmappingstatus-swift.enum/mapped.md).
2. When you run a new session (later or on another device) from that [`ARWorldMap`](arworldmap.md), the device running the new session is at a real-world position and orientation similar to that when the world map was saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/worldmappingstatus-swift.enum/mapped)*