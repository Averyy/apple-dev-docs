# isMuted

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether audio for the renderer is in a muted state.

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
var isMuted: Bool { get set }
```

#### Discussion

This property only affects muting the renderer instance and not the device.

## See Also

- [var volume: Float](avsamplebufferaudiorenderer/volume.md)
  The current audio volume for the audio renderer.
- [var audioOutputDeviceUniqueID: String?](avsamplebufferaudiorenderer/audiooutputdeviceuniqueid.md)
  The unique identifier of the output device used to play audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/ismuted)*