# MTAudioProcessingTapGetStorage(_:)

**Framework**: Media Toolbox  
**Kind**: func  
**Role**: Function

Retrieves a custom storage pointer for an audio processing tap.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MTAudioProcessingTapGetStorage(_ tap: MTAudioProcessingTap) -> UnsafeMutableRawPointer
```

```c
extern void *MTAudioProcessingTapGetStorage(MTAudioProcessingTapRef tap);
```

#### Return Value

The tap storage returned by the init callback.

## Parameters

- `tap`: The processing tap.

## See Also

### Audio Taps
- [func MTAudioProcessingTapCreate(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<MTAudioProcessingTap?>) -> OSStatus](./mtaudioprocessingtapcreate%28_,_,_,_%29.md)
  Creates a new audio processing tap.
- [func MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>?, UnsafeMutablePointer<CMTimeRange>?, UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./mtaudioprocessingtapgetsourceaudio%28_,_,_,_,_,_%29.md)
  Retrieves source audio for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](./mtaudioprocessingtapgettypeid%28%29.md)
  Retrieves the type identifier for this audio processing tap.
- [typealias MTAudioProcessingTapFlags](./mtaudioprocessingtapflags.md)
  Flags that indicate where to tap the audio.
- [class MTAudioProcessingTap](./mtaudioprocessingtap.md)
  An audio processing tap object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapgetstorage(_:))*