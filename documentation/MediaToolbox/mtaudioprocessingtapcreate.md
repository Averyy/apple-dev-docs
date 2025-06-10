# MTAudioProcessingTapCreate(_:_:_:_:)

**Framework**: Media Toolbox  
**Kind**: func

Creates a new audio processing tap.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MTAudioProcessingTapCreate(_ allocator: CFAllocator?, _ callbacks: UnsafePointer<MTAudioProcessingTapCallbacks>, _ flags: MTAudioProcessingTapCreationFlags, _ tapOut: UnsafeMutablePointer<MTAudioProcessingTap?>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Overview

The processing tap will then be used to process decoded data. The processing is performed on audio either before or after any effects or other processing (varispeed, etc) is applied by the audio queue.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new tap. Pass   or   to use the current default allocator.
- `callbacks`: An callbacks struct.   makes a copy of this struct.
- `flags`: Flags that are used to control aspects of the processing tap. Valid flags are:
- `tapOut`: The processing tap object.

## Topics

### Flags
- [typealias MTAudioProcessingTapCreationFlags](mtaudioprocessingtapcreationflags.md)
  Flags to use when creating audio processing taps.
### Callbacks
- [struct MTAudioProcessingTapCallbacks](mtaudioprocessingtapcallbacks.md)
  A structure that defines life cycle callbacks for an audio processing tap object.

## See Also

- [func MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>?, UnsafeMutablePointer<CMTimeRange>?, UnsafeMutablePointer<CMItemCount>?) -> OSStatus](mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:).md)
  Retrieves source audio for an audio processing tap.
- [func MTAudioProcessingTapGetStorage(MTAudioProcessingTap) -> UnsafeMutableRawPointer](mtaudioprocessingtapgetstorage(_:).md)
  Retrieves a custom storage pointer for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](mtaudioprocessingtapgettypeid().md)
  Retrieves the type identifier for this audio processing tap.
- [typealias MTAudioProcessingTapFlags](mtaudioprocessingtapflags.md)
  Flags that indicate where to tap the audio.
- [class MTAudioProcessingTap](mtaudioprocessingtap.md)
  An audio processing tap object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcreate(_:_:_:_:))*