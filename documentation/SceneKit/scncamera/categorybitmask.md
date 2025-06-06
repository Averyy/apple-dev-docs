# categoryBitMask

**Framework**: SceneKit  
**Kind**: property

A mask that defines which categories this camera belongs to.

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
var categoryBitMask: Int { get set }
```

#### Discussion

Each camera and each node in a scene can be assigned to one or more categories, each corresponding to a bit in the bit mask. You define the mask values used in your app. When SceneKit renders a scene, it compares the [`categoryBitMask`](scnnode/categorybitmask.md) property of each node with that of the [`pointOfView`](scnscenerenderer/pointofview.md) camera using a bitwise AND operation. If the result is a nonzero value, SceneKit renders the node’s contents. Use this property to make some nodes in your scene visible only to certain cameras.

The default mask has all bits set, meaning that nodes of all categories are visible to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/categorybitmask)*