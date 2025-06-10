# SCNAudioSource

**Framework**: SceneKit  
**Kind**: class

A simple, reusable audio source—music or sound effects loaded from a file—for use in positional audio playback.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNAudioSource
```

#### Overview

To create positional audio effects, create an [`SCNAudioPlayer`](scnaudioplayer.md) object from the audio source to control playback, and add that player object to an [`SCNNode`](scnnode.md) object in your scene. SceneKit then automatically spatializes 3D audio effects based on the position of that node relative to the scene’s [`audioListener`](scnscenerenderer/audiolistener.md) node.

## Topics

### Creating an Audio Source
- [convenience init?(named: String)](scnaudiosource/init(named:).md)
  Returns the audio source associated with the specified filename.
- [convenience init?(fileNamed: String)](scnaudiosource/init(filenamed:).md)
  Initializes an audio source from an audio file in the application’s main bundle.
- [init?(url: URL)](scnaudiosource/init(url:).md)
  Initializes an audio source from the specified audio file.
### Controlling 3D Audio Spatialization
- [var isPositional: Bool](scnaudiosource/ispositional.md)
  A Boolean value that determines whether audio from this source uses 3D positional mixing.
### Preloading Audio Data
- [func load()](scnaudiosource/load.md)
  Loads audio data from the source and prepares it for playing.
### Setting Default Playback Parameters
- [var volume: Float](scnaudiosource/volume.md)
  The default playback volume for the audio source.
- [var rate: Float](scnaudiosource/rate.md)
  The default playback rate for the audio source.
- [var reverbBlend: Float](scnaudiosource/reverbblend.md)
  The default blend of blend of unmodified and reverb-processed (also called dry and wet) audio for playback of the audio source.
- [var loops: Bool](scnaudiosource/loops.md)
  A Boolean value that determines whether the audio source should play repeatedly.
- [var shouldStream: Bool](scnaudiosource/shouldstream.md)
  A Boolean value that determines whether the audio source should stream content from its source URL when playing.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

## See Also

- [class SCNAudioPlayer](scnaudioplayer.md)
  A controller for playback of a positional audio source in a SceneKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource)*