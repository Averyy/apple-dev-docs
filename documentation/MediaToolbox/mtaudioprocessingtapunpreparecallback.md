# MTAudioProcessingTapUnprepareCallback

**Framework**: Media Toolbox  
**Kind**: typealias

An audio processing unpreparation callback function.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias MTAudioProcessingTapUnprepareCallback = (MTAudioProcessingTap) -> Void
```

#### Overview

The unpreparation callback is invoked when the underlying audio machinery stops calling the process callback.

Preparation and unpreparation callbacks are always paired.

Process callbacks will only ever be called after the prepare callback returns, and before unprepare is called.

## Parameters

- `tap`: The processing tap.

## Topics

### Flags
- [typealias MTAudioProcessingTapCreationFlags](mtaudioprocessingtapcreationflags.md)
  Flags to use when creating audio processing taps.

## See Also

- [typealias MTAudioProcessingTapInitCallback](mtaudioprocessingtapinitcallback.md)
  An initialization callback function.
- [typealias MTAudioProcessingTapPrepareCallback](mtaudioprocessingtappreparecallback.md)
  An audio processing preparation callback function.
- [typealias MTAudioProcessingTapProcessCallback](mtaudioprocessingtapprocesscallback.md)
  An audio processing callback function.
- [typealias MTAudioProcessingTapFinalizeCallback](mtaudioprocessingtapfinalizecallback.md)
  A finalization callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapunpreparecallback)*