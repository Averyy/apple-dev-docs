# upAxis

**Framework**: SceneKit  
**Kind**: property

An `SCNVector3` structure specifying the orientation of the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let upAxis: SCNScene.Attribute
```

#### Discussion

The [`SCNVector3`](scnvector3.md)structure (in an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object) may be present in scenes loaded from scene files produced using external tools, but has no effect on SceneKit’s processing of the scene. Use this vector when combining elements from different scenes so that they appear in their expected orientation.

## See Also

- [static let endTime: SCNScene.Attribute](scnscene/attribute/endtime.md)
- [static let frameRate: SCNScene.Attribute](scnscene/attribute/framerate.md)
  A floating-point value for the frame rate of the scene.
- [static let startTime: SCNScene.Attribute](scnscene/attribute/starttime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/attribute/upaxis)*