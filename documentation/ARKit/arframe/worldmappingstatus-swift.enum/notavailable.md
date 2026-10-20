# ARFrame.WorldMappingStatus.notAvailable

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

No world map is available.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
case notAvailable
```

```c
ARWorldMappingStatusNotAvailable
```

#### Discussion

When the [`worldMappingStatus`](../worldmappingstatus-swift.property.md) of the session’s [`currentFrame`](../../arsession/currentframe.md) is [`ARFrame.WorldMappingStatus.notAvailable`](./notavailable.md), the session has no internal map of the real-world space around the device, nor the scene visible to the camera. Calling [`getCurrentWorldMap(completionHandler:)`](../../arsession/getcurrentworldmap%28completionhandler%29.md) at this time results in an error.

This status occurs shortly after starting a new session. To save or share a world map, wait for the user to explore their surroundings and the session’s status to change to [`ARFrame.WorldMappingStatus.mapped`](./mapped.md) or [`ARFrame.WorldMappingStatus.extending`](./extending.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/worldmappingstatus-swift.enum/notavailable)*