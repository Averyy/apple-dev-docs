# ARFrame.WorldMappingStatus.limited

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

World tracking has not yet sufficiently mapped the area around the current device position.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
case limited
```

```c
ARWorldMappingStatusLimited
```

#### Discussion

When the [`worldMappingStatus`](../worldmappingstatus-swift.property.md) of the session’s [`currentFrame`](../../arsession/currentframe.md) is [`ARFrame.WorldMappingStatus.limited`](./limited.md), the session has not yet fully mapped the real-world space around the device, nor the scene visible to the camera.

Although it is possible at this time to save a world map by calling [`getCurrentWorldMap(completionHandler:)`](../../arsession/getcurrentworldmap%28completionhandler%29.md), the resulting [`ARWorldMap`](../../arworldmap.md) is unlikely to be useful for relocalization in the real-world space near the device’s current position.

To produce a higher quality world map, wait for the user to explore more of their surroundings and the session’s status to change to [`ARFrame.WorldMappingStatus.mapped`](./mapped.md) or [`ARFrame.WorldMappingStatus.extending`](./extending.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/worldmappingstatus-swift.enum/limited)*