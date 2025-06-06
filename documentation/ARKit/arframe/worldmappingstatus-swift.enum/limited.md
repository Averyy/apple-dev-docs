# ARFrame.WorldMappingStatus.limited

**Framework**: ARKit  
**Kind**: case

World tracking has not yet sufficiently mapped the area around the current device position.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case limited
```

#### Discussion

When the [`worldMappingStatus`](arframe/worldmappingstatus-swift.property.md) of the session’s [`currentFrame`](arsession/currentframe.md) is [`ARFrame.WorldMappingStatus.limited`](arframe/worldmappingstatus-swift.enum/limited.md), the session has not yet fully mapped the real-world space around the device, nor the scene visible to the camera.

Although it is possible at this time to save a world map by calling [`getCurrentWorldMap(completionHandler:)`](arsession/getcurrentworldmap(completionhandler:).md), the resulting [`ARWorldMap`](arworldmap.md) is unlikely to be useful for relocalization in the real-world space near the device’s current position.

To produce a higher quality world map, wait for the user to explore more of their surroundings and the session’s status to change to [`ARFrame.WorldMappingStatus.mapped`](arframe/worldmappingstatus-swift.enum/mapped.md) or [`ARFrame.WorldMappingStatus.extending`](arframe/worldmappingstatus-swift.enum/extending.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/worldmappingstatus-swift.enum/limited)*