# SCNReferenceNode

**Framework**: SceneKit  
**Kind**: class

A scene graph node that serves as a placeholder for content to be loaded from a separate scene file.

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
@MainActor
class SCNReferenceNode
```

#### Overview

When you tell a reference node to load its content, SceneKit loads the referenced scene file and makes children of the scene file’s root node become children of the reference node.

## Topics

### Creating a Reference Node
- [init?(url: URL)](scnreferencenode/init(url:).md)
  Initializes a node whose content is to be loaded from the referenced URL.
### Loading and Unloading a Reference Node’s Content
- [var referenceURL: URL](scnreferencenode/referenceurl.md)
  The URL to a scene file from which to load content for the reference node.
- [var loadingPolicy: SCNReferenceLoadingPolicy](scnreferencenode/loadingpolicy.md)
  An option for whether to load the node’s content automatically.
- [func load()](scnreferencenode/load.md)
  Loads content into the node from its referenced external scene file.
- [var isLoaded: Bool](scnreferencenode/isloaded.md)
  A Boolean value that indicates whether the reference node has already loaded its content.
- [func unload()](scnreferencenode/unload.md)
  Removes the node’s children and marks the node as not loaded.
### Constants
- [enum SCNReferenceLoadingPolicy](scnreferenceloadingpolicy.md)
  Options for when to load the reference node’s content, used by the [`loadingPolicy`](scnreferencenode/loadingpolicy.md) property.
### Initializers
- [init?(coder: NSCoder)](scnreferencenode/init(coder:).md)

## Relationships

### Inherits From
- [SCNNode](scnnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNActionable](scnactionable.md)
- [SCNAnimatable](scnanimatable.md)
- [SCNBoundingVolume](scnboundingvolume.md)
- [Sendable](../Swift/Sendable.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)

## See Also

- [Organizing a Scene with Nodes](organizing-a-scene-with-nodes.md)
  Use nodes to define the structure of a scene.
- [class SCNNode](scnnode.md)
  A structural element of a scene graph, representing a position and transform in a 3D coordinate space, to which you can attach geometry, lights, cameras, or other displayable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode)*