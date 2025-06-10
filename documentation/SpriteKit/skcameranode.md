# SKCameraNode

**Framework**: SpriteKit  
**Kind**: class

A node that determines which parts of the scene are visible within a view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@MainActor
class SKCameraNode
```

## Mentions

- [Positioning a Scene’s Origin Within its View](positioning-a-scene-s-origin-within-its-view.md)
- [Using Base Nodes to Lay Out SpriteKit Content](using-base-nodes-to-lay-out-spritekit-content.md)

#### Overview

If you don’t use a camera in your scene, you control the visible portion of a scene using its [`anchorPoint`](skscene/anchorpoint.md) property.

## Topics

### First Steps
- [Getting Started with a Camera](getting-started-with-a-camera.md)
  Learn the semantics of using a camera in your scene.
### Node Visibility
- [func containedNodeSet() -> Set<SKNode>](skcameranode/containednodeset.md)
  Finds nodes that are visible in the camera’s viewport.
- [func contains(SKNode) -> Bool](skcameranode/contains(_:).md)
  Checks to see if a node is visible in the camera’s viewport.

## Relationships

### Inherits From
- [SKNode](sknode.md)
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
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Using Base Nodes to Lay Out SpriteKit Content](using-base-nodes-to-lay-out-spritekit-content.md)
  Use nonvisual nodes to define the layout of a scene.
- [class SKNode](sknode.md)
  The base class of all SpriteKit nodes.
- [class SKReferenceNode](skreferencenode.md)
  A node that’s defined in an archived `.sks` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skcameranode)*