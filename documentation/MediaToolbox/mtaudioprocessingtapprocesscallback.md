# MTAudioProcessingTapProcessCallback

**Framework**: Media Toolbox  
**Kind**: typealias

An audio processing callback function.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias MTAudioProcessingTapProcessCallback = (MTAudioProcessingTap, CMItemCount, MTAudioProcessingTapFlags, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<CMItemCount>, UnsafeMutablePointer<MTAudioProcessingTapFlags>) -> Void
```

#### Overview

The system calls this function when the audio track has data that can be processed by a given tap.

The processing callback will be called when there is sufficient input data to provide for processing. The callback should then go and request as much source data as it needs in order to produce the requested number of processed samples. When the callback requests source data, it may receive less data than it requests.

The tap must provide the same number of samples that are being requested. Under normal circumstances, the source data it requests should be satisfied (as the client running the audio queue is also providing the queue with the audio source material). If there is insufficient source data available (this is indicated by the number of frames from the [`MTAudioProcessingTapGetSourceAudio(_:_:_:_:_:_:)`](mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:).md) call), then the processing tap should cope as best as it can; it can either return less data than was requested, insert silence, insert noise, etc. If less data is returned than requested, the remainder will be filled with silence.

A processing tap is a real-time operation, so the general Core Audio limitations for real-time processing apply.  For example, care should be taken not to allocate memory or call into blocking system calls, as this will interfere with the real-time nature of audio playback.

Under normal operation, the source data will be continuous from the last time the callback was called, and the processed samples should be continuous from the previous samples returned. If there is any discontinuity between the last samples provided for processing, the audio queue will set the [`kMTAudioProcessingTapFlag_StartOfStream`](kmtaudioprocessingtapflag_startofstream.md) bit in the flags. After a discontinuity, the first sample that the processing tap outputs should correspond to the first sample that was provided in the source samples (so a reset + consequent process serves to re-anchor a relationship between the processing tap’s source and processed samples). In this case, the processing tap will typically discard any previous state (for example, if a processing tap was adding a reverb to a signal, then the discontinuity flag would act the same as AudioUnitReset; any previous source information in the processing tap should be discarded).

The caller is responsible for absorbing any processing delays. For example, if the processing is to be done by an audio unit that reports a processing latency, then the caller should remove those latency samples from the audio unit’s rendering and not return them to the tap.

The processing tap may operate on the provided source data in place (“in-place processing”) and return pointers to that buffer, rather than its own. This is similar to audio unit render operations. The processing tap will be provided with a bufferList on input where the mData pointers are `NULL`.

When the output audio is stopped asynchronously, the processing tap will see the [`kMTAudioProcessingTapFlag_EndOfStream`](kmtaudioprocessingtapflag_endofstream.md) bit set on return from [`MTAudioProcessingTapGetSourceAudio(_:_:_:_:_:_:)`](mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:).md), and is responsible for propagating this bit from the callback when its processing has reached this point.

A processing tap never sees the same source data again, so, it should keep its own copy, if it needs to keep it for further reference past the duration of this call. It also cannot assume that the pointers to the source data that it retrieves will remain valid after the processing tap has executed.

Should the processing tap provide custom buffers in `bufferListInOut`, it should ensure that the data pointers remain valid until the tap is executed again.

## Parameters

- `tap`: The processing tap.
- `numberFrames`: The requested number of sample frames that should be rendered.
- `flags`: The flags passed at construction time are provided.
- `bufferListInOut`: The audio buffer list which will contain processed source data. On input, all fields except for the buffer pointers will be filled in, and can be passed directly to   if in-place processing is desired. On output, the buffer list should contain the processed audio buffers.
- `numberFramesOut`: The number of frames of audio data provided in the processed data. Can be 0.
- `flagsOut`: The start/end of stream flags should be set when appropriate.

## See Also

- [typealias MTAudioProcessingTapInitCallback](mtaudioprocessingtapinitcallback.md)
  An initialization callback function.
- [typealias MTAudioProcessingTapPrepareCallback](mtaudioprocessingtappreparecallback.md)
  An audio processing preparation callback function.
- [typealias MTAudioProcessingTapUnprepareCallback](mtaudioprocessingtapunpreparecallback.md)
  An audio processing unpreparation callback function.
- [typealias MTAudioProcessingTapFinalizeCallback](mtaudioprocessingtapfinalizecallback.md)
  A finalization callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapprocesscallback)*