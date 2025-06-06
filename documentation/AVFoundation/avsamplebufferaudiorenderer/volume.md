# volume

**Framework**: AVFoundation  
**Kind**: property

The current audio volume for the audio renderer.

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
var volume: Float { get set }
```

#### Discussion

Use this property for frequent vloume changes; for example, a volume knob or fader. A value of `0.0` silences all audio while a value of `1.0` plays all audio at full volume.

## See Also

- [var isMuted: Bool](avsamplebufferaudiorenderer/ismuted.md)
  A Boolean value that indicates whether audio for the renderer is in a muted state.
- [var audioOutputDeviceUniqueID: String?](avsamplebufferaudiorenderer/audiooutputdeviceuniqueid.md)
  The unique identifier of the output device used to play audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/volume)*