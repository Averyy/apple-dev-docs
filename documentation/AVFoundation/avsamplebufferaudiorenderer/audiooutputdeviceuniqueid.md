# audioOutputDeviceUniqueID

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the output device used to play audio.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var audioOutputDeviceUniqueID: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * audioOutputDeviceUniqueID;
```

## Discussion

The default value of this property is `nil`, which indicates the use of the default audio device. Otherwise, set the value to an [`NSString`](../../Foundation/nsstring.md) containing the unique identifier of the Core Audio output device to use for audio output. [`kAudioDevicePropertyDeviceUID`](../../CoreAudio/kaudiodevicepropertydeviceuid.md) is a suitable source of audio output device unique IDs.

Modifying this property while the timebase’s rate isn’t `0.0` may cause the rate to briefly change to `0.0`.

On macOS, you can use the audio device clock as the [`AVSampleBufferRenderSynchronizer`](../avsamplebufferrendersynchronizer.md) and all attached [`AVQueuedSampleBufferRendering`](../avqueuedsamplebufferrendering.md) timebase clocks. If you modify the `audioOutputDeviceUniqueID`, the clocks of all these timebases may also change.

If you attach multiple renderers with different values for `audioOutputDeviceUniqueID` to the same buffer renderer synchronizer, audio may not stay in sync during playback. To avoid this, ensure that all synchronized sample buffer renderers are using the same audio output device.

## See Also

### Managing audio output
- [var volume: Float](./volume.md)
  The current audio volume for the audio renderer.
- [var isMuted: Bool](./ismuted.md)
  A Boolean value that indicates whether audio for the renderer is in a muted state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/audiooutputdeviceuniqueid)*