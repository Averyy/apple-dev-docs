# SKVideoNode

**Framework**: SpriteKit  
**Kind**: class

A graphical element that plays video content.

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
class SKVideoNode
```

## Mentions

- [Adding a Video to a Scene](adding-a-video-to-a-scene.md)
- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)

#### Overview

This class renders a video at a given size and location in your scene with no exposed player controls.

## Topics

### Getting Started with Video
- [Adding a Video to a Scene](adding-a-video-to-a-scene.md)
  Play video in your scene by adding a video node.
### Creating a Video Node
- [init(avPlayer: AVPlayer)](skvideonode/init(avplayer:)-9ydbu.md)
  Initializes a video node using an existing [`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer) object.
- [init(fileNamed: String)](skvideonode/init(filenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(url: URL)](skvideonode/init(url:)-2im38.md)
  Initializes a video node using a URL.
- [init?(coder: NSCoder)](skvideonode/init(coder:).md)
  Tells you when to initialize a video node that was created from an archive.
- [init(videoFileNamed: String)](skvideonode/init(videofilenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(videoURL: URL)](skvideonode/init(videourl:).md)
  Initializes a video node using a URL that points to a video file.
### Setting the Video Node’s Visual Properties
- [var anchorPoint: CGPoint](skvideonode/anchorpoint.md)
  The point in the sprite that corresponds to the node’s position.
- [var size: CGSize](skvideonode/size.md)
  The dimensions of the video node, in points.
### Controlling Video Playback
- [func play()](skvideonode/play.md)
  Starts video playback.
- [func pause()](skvideonode/pause.md)
  Pauses video playback.
### Initializers
- [init(AVPlayer: AVPlayer)](skvideonode/init(avplayer:)-7s6co.md)
- [init(AVPlayer: AVPlayer)](skvideonode/init(avplayer:)-8uhsn.md)
- [init(URL: URL)](skvideonode/init(url:)-49ou9.md)
- [init(URL: URL)](skvideonode/init(url:)-8rxuu.md)

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

- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)
  Structure your nodes for maximum performance.
- [class SKSpriteNode](skspritenode.md)
  An image or solid color.
- [class SKShapeNode](skshapenode.md)
  A mathematical shape that can be stroked or filled.
- [class SKEmitterNode](skemitternode.md)
  A source of various particle effects.
- [class SKLabelNode](sklabelnode.md)
  A graphical element that draws text.
- [class SKTileMapNode](sktilemapnode.md)
  A two-dimensional array of images.
- [class SK3DNode](sk3dnode.md)
  3D SceneKit content drawn as a flattened sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode)*