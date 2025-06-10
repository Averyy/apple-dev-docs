# MTAudioProcessingTap

**Framework**: Media Toolbox  
**Kind**: class

An audio processing tap object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MTAudioProcessingTap
```

## Topics

### Default Implementations
- [Equatable Implementations](mtaudioprocessingtap/equatable-implementations.md)
- [Hashable Implementations](mtaudioprocessingtap/hashable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func MTAudioProcessingTapCreate(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<MTAudioProcessingTap?>) -> OSStatus](mtaudioprocessingtapcreate(_:_:_:_:).md)
  Creates a new audio processing tap.
- [func MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>?, UnsafeMutablePointer<CMTimeRange>?, UnsafeMutablePointer<CMItemCount>?) -> OSStatus](mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:).md)
  Retrieves source audio for an audio processing tap.
- [func MTAudioProcessingTapGetStorage(MTAudioProcessingTap) -> UnsafeMutableRawPointer](mtaudioprocessingtapgetstorage(_:).md)
  Retrieves a custom storage pointer for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](mtaudioprocessingtapgettypeid().md)
  Retrieves the type identifier for this audio processing tap.
- [typealias MTAudioProcessingTapFlags](mtaudioprocessingtapflags.md)
  Flags that indicate where to tap the audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtap)*