# showLightExtents

**Framework**: SceneKit  
**Kind**: property

Display the regions affected by each [`SCNLight`](scnlight.md) object in the scene.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var showLightExtents: SCNDebugOptions { get }
```

#### Discussion

Only lights whose type is [`omni`](scnlight/lighttype/omni.md) or [`spot`](scnlight/lighttype/spot.md) have an area of effect; directional and ambient lights affect the entire scene.

## See Also

- [static var showCameras: SCNDebugOptions](scndebugoptions/showcameras.md)
  Display visualizations for nodes in the scene with attached cameras and their fields of view.
- [static var showLightInfluences: SCNDebugOptions](scndebugoptions/showlightinfluences.md)
  Display the locations of each [`SCNLight`](scnlight.md) object in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndebugoptions/showlightextents)*