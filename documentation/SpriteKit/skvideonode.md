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

- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)
- [Adding a Video to a Scene](adding-a-video-to-a-scene.md)

#### Overview

This class renders a video at a given size and location in your scene with no exposed player controls.

## Topics

### Getting Started with Video
- [Adding a Video to a Scene](adding-a-video-to-a-scene.md)
  Play video in your scene by adding a video node.
### Creating a Video Node
- [init(avPlayer: AVPlayer)](skvideonode/init(avplayer:).md)
  Initializes a video node using an existing [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object.
- [init(fileNamed: String)](skvideonode/init(filenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(url: URL)](skvideonode/init(url:).md)
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