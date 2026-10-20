# SKVideoNode

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A graphical element that plays video content.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class SKVideoNode
```

```objc
@interface SKVideoNode : SKNode
```

## Mentions

- [Adding a Video to a Scene](./adding-a-video-to-a-scene.md)
- [Animate the Warping of a Sprite](./animate-the-warping-of-a-sprite.md)

#### Overview

This class renders a video at a given size and location in your scene with no exposed player controls.

## Topics

### Getting Started with Video
- [Adding a Video to a Scene](./adding-a-video-to-a-scene.md)
  Play video in your scene by adding a video node.
### Creating a Video Node
- [init(avPlayer: AVPlayer)](./skvideonode/init%28avplayer%29-9ydbu.md)
  Initializes a video node using an existing [`AVPlayer`](../AVFoundation/avplayer.md) object.
- [init(fileNamed: String)](./skvideonode/init%28filenamed%29.md)
  Initializes a video node using a video file stored in the app bundle.
- [init(url: URL)](./skvideonode/init%28url%29-2im38.md)
  Initializes a video node using a URL.
- [init?(coder: NSCoder)](./skvideonode/init%28coder%29.md)
  Tells you when to initialize a video node that was created from an archive.
- [init(videoFileNamed: String)](./skvideonode/init%28videofilenamed%29.md)
  Initializes a video node using a video file stored in the app bundle.
- [init(videoURL: URL)](./skvideonode/init%28videourl%29.md)
  Initializes a video node using a URL that points to a video file.
### Setting the Video Node’s Visual Properties
- [var anchorPoint: CGPoint](./skvideonode/anchorpoint.md)
  The point in the sprite that corresponds to the node’s position.
- [var size: CGSize](./skvideonode/size.md)
  The dimensions of the video node, in points.
### Controlling Video Playback
- [func play()](./skvideonode/play%28%29.md)
  Starts video playback.
- [func pause()](./skvideonode/pause%28%29.md)
  Pauses video playback.
### Initializers
- [init(AVPlayer: AVPlayer)](./skvideonode/init%28avplayer%29-7s6co.md)
- [init(AVPlayer: AVPlayer)](./skvideonode/init%28avplayer%29-8uhsn.md)
- [init(URL: URL)](./skvideonode/init%28url%29-49ou9.md)
- [init(URL: URL)](./skvideonode/init%28url%29-8rxuu.md)

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

### Nodes that Draw
- [Maximizing Node Drawing Performance](./maximizing-node-drawing-performance.md)
  Structure your nodes for maximum performance.
- [class SKSpriteNode](./skspritenode.md)
  An image or solid color.
- [class SKShapeNode](./skshapenode.md)
  A mathematical shape that can be stroked or filled.
- [class SKEmitterNode](./skemitternode.md)
  A source of various particle effects.
- [class SKLabelNode](./sklabelnode.md)
  A graphical element that draws text.
- [class SKTileMapNode](./sktilemapnode.md)
  A two-dimensional array of images.
- [class SK3DNode](./sk3dnode.md)
  3D SceneKit content drawn as a flattened sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode)*