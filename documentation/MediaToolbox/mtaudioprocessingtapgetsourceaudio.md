# MTAudioProcessingTapGetSourceAudio(_:_:_:_:_:_:)

**Framework**: Media Toolbox  
**Kind**: func

Retrieves source audio for an audio processing tap.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MTAudioProcessingTapGetSourceAudio(_ tap: MTAudioProcessingTap, _ numberFrames: CMItemCount, _ bufferListInOut: UnsafeMutablePointer<AudioBufferList>, _ flagsOut: UnsafeMutablePointer<MTAudioProcessingTapFlags>?, _ timeRangeOut: UnsafeMutablePointer<CMTimeRange>?, _ numberFramesOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Overview

This function may only be called from the processing tap’s callback.

## Parameters

- `tap`: The processing tap.
- `numberFrames`: The number of frames the processing tap requires for its processing.
- `bufferListInOut`: The audio buffer list which will contain the source data.   On input, all fields except for the buffer pointers must be filled in.   If the buffer pointers are NULL (recommended), non-NULL pointers will be   returned and system owns the source buffers; these buffers are only applicable   for the duration of the processing tap callback.   If the buffer pointers are non-NULL, then they must be big enough to hold   numberFrames, and the source data will be copied into these buffers.
- `flagsOut`: Flags to describe state about the input requested, e.g., discontinuity/complete. Can be NULL.
- `timeRangeOut`: The asset time range corresponding to the provided source audio frames. Can be NULL.
- `numberFramesOut`: The number of source frames that have been provided. Can be NULL. This can be less than the number of requested frames specified in numberFrames.

## See Also

- [func MTAudioProcessingTapCreate(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus](mtaudioprocessingtapcreate(_:_:_:_:).md)
  Creates a new audio processing tap.
- [func MTAudioProcessingTapGetStorage(MTAudioProcessingTap) -> UnsafeMutableRawPointer](mtaudioprocessingtapgetstorage(_:).md)
  Retrieves a custom storage pointer for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](mtaudioprocessingtapgettypeid().md)
  Retrieves the type identifier for this audio processing tap.
- [typealias MTAudioProcessingTapFlags](mtaudioprocessingtapflags.md)
  Flags that indicate where to tap the audio.
- [class MTAudioProcessingTap](mtaudioprocessingtap.md)
  An audio processing tap object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:))*