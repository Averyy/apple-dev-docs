# MTAudioProcessingTapFlags

**Framework**: Media Toolbox  
**Kind**: typealias  
**Role**: Type Alias

Flags that indicate where to tap the audio.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias MTAudioProcessingTapFlags = UInt32
```

```c
typedef uint32_t MTAudioProcessingTapFlags;
```

## Topics

### Flags
- [var kMTAudioProcessingTapFlag_EndOfStream: MTAudioProcessingTapFlags](./kmtaudioprocessingtapflag_endofstream.md)
  Signifies that the source audio is past the end of stream.
- [var kMTAudioProcessingTapFlag_StartOfStream: MTAudioProcessingTapFlags](./kmtaudioprocessingtapflag_startofstream.md)
  Signifies that the source audio is the beginning of a continuous stream.

## See Also

### Audio Taps
- [func MTAudioProcessingTapCreate(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<MTAudioProcessingTap?>) -> OSStatus](./mtaudioprocessingtapcreate%28_,_,_,_%29.md)
  Creates a new audio processing tap.
- [func MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>?, UnsafeMutablePointer<CMTimeRange>?, UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./mtaudioprocessingtapgetsourceaudio%28_,_,_,_,_,_%29.md)
  Retrieves source audio for an audio processing tap.
- [func MTAudioProcessingTapGetStorage(MTAudioProcessingTap) -> UnsafeMutableRawPointer](./mtaudioprocessingtapgetstorage%28_%29.md)
  Retrieves a custom storage pointer for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](./mtaudioprocessingtapgettypeid%28%29.md)
  Retrieves the type identifier for this audio processing tap.
- [class MTAudioProcessingTap](./mtaudioprocessingtap.md)
  An audio processing tap object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapflags)*