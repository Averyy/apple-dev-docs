# SKCameraNode

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

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
class SKCameraNode
```

```objc
@interface SKCameraNode : SKNode
```

## Mentions

- [Positioning a Scene’s Origin Within its View](./positioning-a-scene-s-origin-within-its-view.md)
- [Using Base Nodes to Lay Out SpriteKit Content](./using-base-nodes-to-lay-out-spritekit-content.md)

## Overview

If you don’t use a camera in your scene, you control the visible portion of a scene using its [`anchorPoint`](./skscene/anchorpoint.md) property.

## Topics

### First Steps
- [Getting Started with a Camera](./getting-started-with-a-camera.md)
  Learn the semantics of using a camera in your scene.
### Node Visibility
- [func containedNodeSet() -> Set<SKNode>](./skcameranode/containednodeset%28%29.md)
  Finds nodes that are visible in the camera’s viewport.
- [func contains(SKNode) -> Bool](./skcameranode/contains%28_%29.md)
  Checks to see if a node is visible in the camera’s viewport.

## Relationships

### Inherits From
- [SKNode](./sknode.md)
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
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Base Nodes
- [Using Base Nodes to Lay Out SpriteKit Content](./using-base-nodes-to-lay-out-spritekit-content.md)
  Use nonvisual nodes to define the layout of a scene.
- [class SKNode](./sknode.md)
  The base class of all SpriteKit nodes.
- [class SKReferenceNode](./skreferencenode.md)
  A node that’s defined in an archived `.sks` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skcameranode)*