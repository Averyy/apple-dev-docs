# showWorldOrigin

**Framework**: SceneKit  
**Kind**: property

Display a coordinate axis visualization indicating the position and orientation of the AR world coordinate system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let showWorldOrigin: SCNDebugOptions
```

#### Discussion

This visualization is available to all session configurations and session [`worldAlignment`](https://developer.apple.com/documentation/ARKit/ARConfiguration/worldAlignment-swift.property) options, but is most useful with a [`ARWorldTrackingConfiguration`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration) session. For example, if you start running a session when this option is enabled, then take a step backward, the real-world position tracked by the AR world coordinate system should become visible on your device screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndebugoptions/showworldorigin)*