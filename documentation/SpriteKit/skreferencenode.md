# SKReferenceNode

**Framework**: SpriteKit  
**Kind**: class

A node that’s defined in an archived `.sks` file.

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
class SKReferenceNode
```

## Mentions

- [Using Base Nodes to Lay Out SpriteKit Content](using-base-nodes-to-lay-out-spritekit-content.md)

#### Overview

`SKReferenceNode` is used within an archived `.sks` file to refer to node defined in another `.sks` file without duplicating its definition. This way, a change to the referenced node propagates to all the references in other files.

> **Note**:  `SKReferenceNode` is mostly used in conjunction with Xcode’s SpriteKit Scene editor, but it’s possible to instantiate it yourself and use the [`resolve()`](skreferencenode/resolve().md) function as a handy way to restore a node’s appearance.

As an example, you might want to share an enemy ship across two different levels, Scene1.sks and Scene2.sks, in a level-based game. Reference nodes allow you to do that without creating copies of the shared node and its properties.

To use a reference node:

- Create the shared content in a separate archive
- Add references to the shared archive within your scene archives

When each scene is loaded, the reference nodes are resolved dynamically, and therefore you only need to configure a shared object in one place.

## Topics

### Initializers
- [convenience init(url: URL)](skreferencenode/init(url:)-3jryz.md)
  Creates a reference node from a URL.
- [init(url: URL?)](skreferencenode/init(url:)-429mo.md)
  Initializes a reference node from a URL.
- [convenience init(fileNamed: String)](skreferencenode/init(filenamed:)-77gs0.md)
  Creates a reference node from a file in the app’s main bundle.
- [init(fileNamed: String?)](skreferencenode/init(filenamed:)-2yeh2.md)
  Initializes a reference node from a file in the app’s main bundle.
- [init?(coder: NSCoder)](skreferencenode/init(coder:).md)
  A method that initializes a reference node from an archive.
- [init(URL: URL?)](skreferencenode/init(url:)-8glm0.md)
- [convenience init(URL: URL)](skreferencenode/init(url:)-8yn6r.md)
### Regenerating
- [func resolve()](skreferencenode/resolve.md)
  Loads the reference node’s content and adds it as a new child node.
### Loading Callback
- [func didLoad(SKNode?)](skreferencenode/didload(_:).md)
  A method called by SpriteKit after the reference node’s contents are loaded.

## Relationships

### Inherits From
- [SKNode](sknode.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Using Base Nodes to Lay Out SpriteKit Content](using-base-nodes-to-lay-out-spritekit-content.md)
  Use nonvisual nodes to define the layout of a scene.
- [class SKNode](sknode.md)
  The base class of all SpriteKit nodes.
- [class SKCameraNode](skcameranode.md)
  A node that determines which parts of the scene are visible within a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skreferencenode)*