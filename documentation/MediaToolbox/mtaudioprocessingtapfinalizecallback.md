# MTAudioProcessingTapFinalizeCallback

**Framework**: Media Toolbox  
**Kind**: typealias

A finalization callback function.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias MTAudioProcessingTapFinalizeCallback = (MTAudioProcessingTap) -> Void
```

#### Overview

This callback is called when it is safe to free any buffers or other state associated with the tap. This callback will be called exactly once when the MTAudioProcessingTap object is finalized. If tapStorage was allocated in the init callback, it should be freed here.

## Parameters

- `tap`: The processing tap.

## See Also

- [typealias MTAudioProcessingTapInitCallback](mtaudioprocessingtapinitcallback.md)
  An initialization callback function.
- [typealias MTAudioProcessingTapPrepareCallback](mtaudioprocessingtappreparecallback.md)
  An audio processing preparation callback function.
- [typealias MTAudioProcessingTapProcessCallback](mtaudioprocessingtapprocesscallback.md)
  An audio processing callback function.
- [typealias MTAudioProcessingTapUnprepareCallback](mtaudioprocessingtapunpreparecallback.md)
  An audio processing unpreparation callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapfinalizecallback)*