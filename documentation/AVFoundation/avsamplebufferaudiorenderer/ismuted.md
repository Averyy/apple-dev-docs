# isMuted

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether audio for the renderer is in a muted state.

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
var isMuted: Bool { get set }
```

```objc
@property (nonatomic, getter=isMuted) BOOL muted;
```

## Discussion

This property only affects muting the renderer instance and not the device.

## See Also

### Managing audio output
- [var volume: Float](./volume.md)
  The current audio volume for the audio renderer.
- [var audioOutputDeviceUniqueID: String?](./audiooutputdeviceuniqueid.md)
  The unique identifier of the output device used to play audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/ismuted)*