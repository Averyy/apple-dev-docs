# MTAudioProcessingTapGetStorage(_:)

**Framework**: Media Toolbox  
**Kind**: func

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

#### Return Value

The tap storage returned by the init callback.

## Parameters

- `tap`: The processing tap.

## See Also

- [func MTAudioProcessingTapCreate(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus](mtaudioprocessingtapcreate(_:_:_:_:).md)
  Creates a new audio processing tap.
- [func MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>?, UnsafeMutablePointer<CMTimeRange>?, UnsafeMutablePointer<CMItemCount>?) -> OSStatus](mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:).md)
  Retrieves source audio for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](mtaudioprocessingtapgettypeid().md)
  Retrieves the type identifier for this audio processing tap.
- [typealias MTAudioProcessingTapFlags](mtaudioprocessingtapflags.md)
  Flags that indicate where to tap the audio.
- [class MTAudioProcessingTap](mtaudioprocessingtap.md)
  An audio processing tap object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapgetstorage(_:))*