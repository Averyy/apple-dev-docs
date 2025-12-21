# SKAudioNode

**Framework**: SpriteKit  
**Kind**: class

A node that plays audio.

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
class SKAudioNode
```

## Mentions

- [Using Audio Nodes with the Scene’s Listener](using-audio-nodes-with-the-scene-s-listener.md)

#### Overview

A [`SKAudioNode`](skaudionode.md) object is used to add an audio to a scene. The sounds are played automatically using AVFoundation, and the node can optionally add 3D spatial audio effects to the audio when it is played.

The currently presented [`SKScene`](skscene.md) object mixes the audio from nodes in the scene based on parameters defined in the [`AVAudio3DMixing`](https://developer.apple.com/documentation/AVFAudio/AVAudio3DMixing) protocol. A scene’s [`audioEngine`](skscene/audioengine.md) property allows overall control of volume and playback.

By default, [`SKAudioNode`](skaudionode.md) objects are positional, i.e. their [`isPositional`](skaudionode/ispositional.md) property is set to [`true`](https://developer.apple.com/documentation/Swift/true). If you add an audio node to a scene with a [`listener`](skscene/listener.md) set, SpriteKit will set the stereo balance and the volume based on the relative positions of the two nodes.

You can explicitly set the volume or stereo balance to an audio node by running actions on it.

SpriteKit includes actions that reduce an audio node’s volume by changing either its occlusion or obstruction. The difference between these actions is that occlusion affects both the direct and reverb paths of the sound while obstruction only affects the direct path. The  action offers absolute control over an audio node’s volume.

You can manually set the stereo balance of an audio node with a  action.

Special effects, such as speeding up or slowing down audio by changing the playback rate and adding reverb are also available as audio actions.

To learn more about audio actions, see Controlling the Audio of a Node in [`Action Initializers`](action-initializers.md).

## Topics

### First Steps
- [Using Audio Nodes with the Scene’s Listener](using-audio-nodes-with-the-scene-s-listener.md)
  Add audio to your scene, and optionally give it 2D-positional mixing characteristics.
### Initializing Audio Nodes
- [init(avAudioNode: AVAudioNode?)](skaudionode/init(avaudionode:).md)
  Initializes an audio node from an AVFoundation audio node.
- [convenience init(fileNamed: String)](skaudionode/init(filenamed:).md)
  Initializes an audio node from an audio asset with the specified filename.
- [convenience init(url: URL)](skaudionode/init(url:).md)
  Initializes an audio node from an audio asset with the specified URL.
- [init?(coder: NSCoder)](skaudionode/init(coder:).md)
  Tells you when to initialize an audio node that has been unarchived.
### Configuring Audio Nodes
- [var avAudioNode: AVAudioNode?](skaudionode/avaudionode.md)
  The audio node’s current audio asset.
- [var isPositional: Bool](skaudionode/ispositional.md)
  A Boolean property that indicates whether the node’s audio is altered based on the position of the node.
- [var autoplayLooped: Bool](skaudionode/autoplaylooped.md)
  A Boolean value that indicates whether the audio should play in a loop when the node is added to the scene.

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

- [class SKLightNode](sklightnode.md)
  A node that lights surrounding nodes.
- [class SKFieldNode](skfieldnode.md)
  A node that applies physics effects to nearby nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode)*