# frameRate

**Framework**: SceneKit  
**Kind**: property

A floating-point value for the frame rate of the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let frameRate: SCNScene.Attribute
```

#### Discussion

This value (in an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object) may be present in scenes loaded from scene files produced using external tools, but has no effect on SceneKit’s rendering of the scene.

## See Also

- [static let endTime: SCNScene.Attribute](scnscene/attribute/endtime.md)
- [static let startTime: SCNScene.Attribute](scnscene/attribute/starttime.md)
- [static let upAxis: SCNScene.Attribute](scnscene/attribute/upaxis.md)
  An `SCNVector3` structure specifying the orientation of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/attribute/framerate)*