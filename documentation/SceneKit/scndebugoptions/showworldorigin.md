# showWorldOrigin

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Display a coordinate axis visualization indicating the position and orientation of the AR world coordinate system.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
static let showWorldOrigin: SCNDebugOptions
```

## Discussion

This visualization is available to all session configurations and session [`worldAlignment`](../../ARKit/arconfiguration/worldalignment-swift.property.md) options, but is most useful with a [`ARWorldTrackingConfiguration`](../../ARKit/arworldtrackingconfiguration.md) session. For example, if you start running a session when this option is enabled, then take a step backward, the real-world position tracked by the AR world coordinate system should become visible on your device screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndebugoptions/showworldorigin)*