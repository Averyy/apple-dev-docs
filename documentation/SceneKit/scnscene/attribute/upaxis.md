# upAxis

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

An `SCNVector3` structure specifying the orientation of the scene.

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
static let upAxis: SCNScene.Attribute
```

```c
extern SCNSceneAttribute const SCNSceneUpAxisAttributeKey;
```

#### Discussion

The [`SCNVector3`](../../scnvector3.md)structure (in an [`NSValue`](../../../Foundation/nsvalue.md) object) may be present in scenes loaded from scene files produced using external tools, but has no effect on SceneKit’s processing of the scene. Use this vector when combining elements from different scenes so that they appear in their expected orientation.

## See Also

### Type Properties
- [static let endTime: SCNScene.Attribute](./endtime.md)
- [static let frameRate: SCNScene.Attribute](./framerate.md)
  A floating-point value for the frame rate of the scene.
- [static let startTime: SCNScene.Attribute](./starttime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/attribute/upaxis)*