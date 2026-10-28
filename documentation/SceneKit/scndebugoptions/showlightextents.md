# showLightExtents

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Display the regions affected by each [`SCNLight`](../scnlight.md) object in the scene.

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
static var showLightExtents: SCNDebugOptions { get }
```

```c
SCNDebugOptionShowLightExtents
```

## Discussion

Only lights whose type is [`omni`](../scnlight/lighttype/omni.md) or [`spot`](../scnlight/lighttype/spot.md) have an area of effect; directional and ambient lights affect the entire scene.

## See Also

### Debugging Cameras and Lighting
- [static var showCameras: SCNDebugOptions](./showcameras.md)
  Display visualizations for nodes in the scene with attached cameras and their fields of view.
- [static var showLightInfluences: SCNDebugOptions](./showlightinfluences.md)
  Display the locations of each [`SCNLight`](../scnlight.md) object in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndebugoptions/showlightextents)*