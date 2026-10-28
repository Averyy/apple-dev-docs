# isPositional

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether audio from this source uses 3D positional mixing.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var isPositional: Bool { get set }
```

```objc
@property (nonatomic, getter=isPositional) BOOL positional;
```

## Discussion

If this value is [`true`](../../Swift/true.md) (the default), SceneKit mixes audio from the source based on its position relative to the scene’s [`audioListener`](../scnscenerenderer/audiolistener.md) node—that is, the audio source’s volume, reverb, and other parameters automatically change depending on the distance to the listener and other objects in the scene. (To position an audio source in a scene, create an [`SCNAudioPlayer`](../scnaudioplayer.md) player from the source and attach that player to an [`SCNNode`](../scnnode.md) object.)

If you set this property to [`false`](../../Swift/false.md), the source’s audio plays with the same volume (and other mixing parameters) regardless of the listener’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/ispositional)*