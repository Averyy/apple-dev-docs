# Adding a Video to a Scene

**Framework**: SpriteKit

Play video in your scene by adding a video node.

#### Overview

A video node renders a video at a given size and location in your scene with no exposed player controls. You might use a video node to animate visual behaviors that would be expensive to define using a collection of textures.

Be aware that a video node offers only a subset of the features available to the [`SKSpriteNode`](skspritenode.md) class. The following are a video node’s relevant limitations:

- A video node is always scaled proportionally.
- A video node cannot be colorized. However, it can be added as a child of a [`SKEffectNode`](skeffectnode.md) to add Core Image filters for color treatments and other effects.
- A video node always uses an alpha blend mode.
- A video node cannot use custom shaders or lighting.

When a video node is created, its [`size`](skvideonode/size.md) property is initialized to the base size of the video content, but you can change it. The video content is automatically stretched to the new size. As with a sprite node, the [`anchorPoint`](skvideonode/anchorpoint.md) property defines where the content is displayed relative to the node position.

The following code initializes the video node using a video file stored in the app bundle and then adds the node to the scene. It calls the node’s [`play()`](skvideonode/play().md) method to start the video playback.

You control playback using the node’s [`play()`](skvideonode/play().md) and [`pause()`](skvideonode/pause().md) methods.

If you need more precise control over the video playback behavior, you can use AVFoundation to create an [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object for your video content and then use this object to initialize the [`SKVideoNode`](skvideonode.md) node. Then, instead of using the node’s playback methods, you use the [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object to control playback. The video content is automatically displayed in the video node. For more information, see [`AVFoundation Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/adding-a-video-to-a-scene)*