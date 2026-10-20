# categoryBitMask

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A mask that defines which categories this camera belongs to.

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
var categoryBitMask: Int { get set }
```

```objc
@property (nonatomic) NSUInteger categoryBitMask;
```

#### Discussion

Each camera and each node in a scene can be assigned to one or more categories, each corresponding to a bit in the bit mask. You define the mask values used in your app. When SceneKit renders a scene, it compares the [`categoryBitMask`](../scnnode/categorybitmask.md) property of each node with that of the [`pointOfView`](../scnscenerenderer/pointofview.md) camera using a bitwise AND operation. If the result is a nonzero value, SceneKit renders the node’s contents. Use this property to make some nodes in your scene visible only to certain cameras.

The default mask has all bits set, meaning that nodes of all categories are visible to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/categorybitmask)*