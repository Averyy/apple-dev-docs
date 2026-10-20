# frameRate

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

A floating-point value for the frame rate of the scene.

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
static let frameRate: SCNScene.Attribute
```

```c
extern SCNSceneAttribute const SCNSceneFrameRateAttributeKey;
```

#### Discussion

This value (in an [`NSNumber`](../../../Foundation/nsnumber.md) object) may be present in scenes loaded from scene files produced using external tools, but has no effect on SceneKit’s rendering of the scene.

## See Also

### Type Properties
- [static let endTime: SCNScene.Attribute](./endtime.md)
- [static let startTime: SCNScene.Attribute](./starttime.md)
- [static let upAxis: SCNScene.Attribute](./upaxis.md)
  An `SCNVector3` structure specifying the orientation of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/attribute/framerate)*