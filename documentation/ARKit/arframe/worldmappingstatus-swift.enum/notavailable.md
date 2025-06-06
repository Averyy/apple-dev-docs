# ARFrame.WorldMappingStatus.notAvailable

**Framework**: ARKit  
**Kind**: case

No world map is available.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case notAvailable
```

#### Discussion

When the [`worldMappingStatus`](arframe/worldmappingstatus-swift.property.md) of the session’s [`currentFrame`](arsession/currentframe.md) is [`ARFrame.WorldMappingStatus.notAvailable`](arframe/worldmappingstatus-swift.enum/notavailable.md), the session has no internal map of the real-world space around the device, nor the scene visible to the camera. Calling [`getCurrentWorldMap(completionHandler:)`](arsession/getcurrentworldmap(completionhandler:).md) at this time results in an error.

This status occurs shortly after starting a new session. To save or share a world map, wait for the user to explore their surroundings and the session’s status to change to [`ARFrame.WorldMappingStatus.mapped`](arframe/worldmappingstatus-swift.enum/mapped.md) or [`ARFrame.WorldMappingStatus.extending`](arframe/worldmappingstatus-swift.enum/extending.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/worldmappingstatus-swift.enum/notavailable)*