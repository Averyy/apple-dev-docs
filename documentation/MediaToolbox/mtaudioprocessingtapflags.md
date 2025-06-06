# MTAudioProcessingTapFlags

**Framework**: Media Toolbox  
**Kind**: typealias

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

## Topics

### Flags
- [var kMTAudioProcessingTapFlag_EndOfStream: MTAudioProcessingTapFlags](kmtaudioprocessingtapflag_endofstream.md)
  Signifies that the source audio is past the end of stream.
- [var kMTAudioProcessingTapFlag_StartOfStream: MTAudioProcessingTapFlags](kmtaudioprocessingtapflag_startofstream.md)
  Signifies that the source audio is the beginning of a continuous stream.

## See Also

- [func MTAudioProcessingTapCreate(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus](mtaudioprocessingtapcreate(_:_:_:_:).md)
  Creates a new audio processing tap.
- [func MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>?, UnsafeMutablePointer<CMTimeRange>?, UnsafeMutablePointer<CMItemCount>?) -> OSStatus](mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:).md)
  Retrieves source audio for an audio processing tap.
- [func MTAudioProcessingTapGetStorage(MTAudioProcessingTap) -> UnsafeMutableRawPointer](mtaudioprocessingtapgetstorage(_:).md)
  Retrieves a custom storage pointer for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](mtaudioprocessingtapgettypeid().md)
  Retrieves the type identifier for this audio processing tap.
- [class MTAudioProcessingTap](mtaudioprocessingtap.md)
  An audio processing tap object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapflags)*