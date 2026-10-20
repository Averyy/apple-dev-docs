# SCNAudioSource

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A simple, reusable audio source—music or sound effects loaded from a file—for use in positional audio playback.

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
class SCNAudioSource
```

```objc
@interface SCNAudioSource : NSObject
```

#### Overview

To create positional audio effects, create an [`SCNAudioPlayer`](./scnaudioplayer.md) object from the audio source to control playback, and add that player object to an [`SCNNode`](./scnnode.md) object in your scene. SceneKit then automatically spatializes 3D audio effects based on the position of that node relative to the scene’s [`audioListener`](./scnscenerenderer/audiolistener.md) node.

## Topics

### Creating an Audio Source
- [convenience init?(named: String)](./scnaudiosource/init%28named%29.md)
  Returns the audio source associated with the specified filename.
- [convenience init?(fileNamed: String)](./scnaudiosource/init%28filenamed%29.md)
  Initializes an audio source from an audio file in the application’s main bundle.
- [init?(url: URL)](./scnaudiosource/init%28url%29-3qyjs.md)
  Initializes an audio source from the specified audio file.
### Controlling 3D Audio Spatialization
- [var isPositional: Bool](./scnaudiosource/ispositional.md)
  A Boolean value that determines whether audio from this source uses 3D positional mixing.
### Preloading Audio Data
- [func load()](./scnaudiosource/load%28%29.md)
  Loads audio data from the source and prepares it for playing.
### Setting Default Playback Parameters
- [var volume: Float](./scnaudiosource/volume.md)
  The default playback volume for the audio source.
- [var rate: Float](./scnaudiosource/rate.md)
  The default playback rate for the audio source.
- [var reverbBlend: Float](./scnaudiosource/reverbblend.md)
  The default blend of blend of unmodified and reverb-processed (also called dry and wet) audio for playback of the audio source.
- [var loops: Bool](./scnaudiosource/loops.md)
  A Boolean value that determines whether the audio source should play repeatedly.
- [var shouldStream: Bool](./scnaudiosource/shouldstream.md)
  A Boolean value that determines whether the audio source should stream content from its source URL when playing.
### Initializers
- [init?(URL: URL)](./scnaudiosource/init%28url%29-8cknu.md)
- [init?(coder: NSCoder)](./scnaudiosource/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

## See Also

### Audio
- [class SCNAudioPlayer](./scnaudioplayer.md)
  A controller for playback of a positional audio source in a SceneKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource)*