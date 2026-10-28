# SCNReferenceNode

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A scene graph node that serves as a placeholder for content to be loaded from a separate scene file.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
@MainActor
class SCNReferenceNode
```

*macOS, watchOS*

```swift
class SCNReferenceNode
```

```objc
@interface SCNReferenceNode : SCNNode
```

## Overview

When you tell a reference node to load its content, SceneKit loads the referenced scene file and makes children of the scene file’s root node become children of the reference node.

## Topics

### Creating a Reference Node
- [init?(url: URL)](./scnreferencenode/init%28url%29-9dkfj.md)
  Initializes a node whose content is to be loaded from the referenced URL.
- [+ referenceNodeWithURL:](./scnreferencenode/referencenodewithurl_.md)
  Creates a node whose content is to be loaded from the referenced URL.
### Loading and Unloading a Reference Node’s Content
- [var referenceURL: URL](./scnreferencenode/referenceurl.md)
  The URL to a scene file from which to load content for the reference node.
- [var loadingPolicy: SCNReferenceLoadingPolicy](./scnreferencenode/loadingpolicy.md)
  An option for whether to load the node’s content automatically.
- [func load()](./scnreferencenode/load%28%29.md)
  Loads content into the node from its referenced external scene file.
- [var isLoaded: Bool](./scnreferencenode/isloaded.md)
  A Boolean value that indicates whether the reference node has already loaded its content.
- [func unload()](./scnreferencenode/unload%28%29.md)
  Removes the node’s children and marks the node as not loaded.
### Constants
- [enum SCNReferenceLoadingPolicy](./scnreferenceloadingpolicy.md)
  Options for when to load the reference node’s content, used by the [`loadingPolicy`](./scnreferencenode/loadingpolicy.md) property.
### Initializers
- [convenience init?(URL: URL)](./scnreferencenode/init%28url%29-9w131.md)
- [init?(URL: URL)](./scnreferencenode/init%28url%29-w5vu.md)
- [init?(coder: NSCoder)](./scnreferencenode/init%28coder%29.md)

## Relationships

### Inherits From
- [SCNNode](./scnnode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [SCNActionable](./scnactionable.md)
- [SCNAnimatable](./scnanimatable.md)
- [SCNBoundingVolume](./scnboundingvolume.md)
- [Sendable](../Swift/sendable.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)

## See Also

### Scene Structure
- [Organizing a Scene with Nodes](./organizing-a-scene-with-nodes.md)
  Use nodes to define the structure of a scene.
- [class SCNNode](./scnnode.md)
  A structural element of a scene graph, representing a position and transform in a 3D coordinate space, to which you can attach geometry, lights, cameras, or other displayable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode)*