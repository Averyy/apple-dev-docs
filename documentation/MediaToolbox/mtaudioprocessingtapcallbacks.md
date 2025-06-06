# MTAudioProcessingTapCallbacks

**Framework**: Media Toolbox  
**Kind**: struct

A structure that defines life cycle callbacks for an audio processing tap object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MTAudioProcessingTapCallbacks
```

#### Overview

On 64-bit architectures, this struct contains misaligned function pointers. To avoid link-time issues, fill its function pointer fields by using assignment statements, rather than declaring them as global or static structs.

## Topics

### Fields
- [var version: Int32](mtaudioprocessingtapcallbacks/version.md)
  The version number of the structure.
- [var clientInfo: UnsafeMutableRawPointer?](mtaudioprocessingtapcallbacks/clientinfo.md)
  App data that the system passes to the initialization callback.
- [var `init`: MTAudioProcessingTapInitCallback?](mtaudioprocessingtapcallbacks/init.md)
  A callback to initialize the tap processor.
- [var finalize: MTAudioProcessingTapFinalizeCallback?](mtaudioprocessingtapcallbacks/finalize.md)
  A callback to perform any necessary cleanup.
- [var prepare: MTAudioProcessingTapPrepareCallback?](mtaudioprocessingtapcallbacks/prepare.md)
  A callback to prepare the tap processor.
- [var unprepare: MTAudioProcessingTapUnprepareCallback?](mtaudioprocessingtapcallbacks/unprepare.md)
  A callback to perform any necessary cleanup for previous preparation.
- [var process: MTAudioProcessingTapProcessCallback](mtaudioprocessingtapcallbacks/process.md)
  A callback for processing the audio.
### Callback functions
- [typealias MTAudioProcessingTapInitCallback](mtaudioprocessingtapinitcallback.md)
  An initialization callback function.
- [typealias MTAudioProcessingTapPrepareCallback](mtaudioprocessingtappreparecallback.md)
  An audio processing preparation callback function.
- [typealias MTAudioProcessingTapProcessCallback](mtaudioprocessingtapprocesscallback.md)
  An audio processing callback function.
- [typealias MTAudioProcessingTapUnprepareCallback](mtaudioprocessingtapunpreparecallback.md)
  An audio processing unpreparation callback function.
- [typealias MTAudioProcessingTapFinalizeCallback](mtaudioprocessingtapfinalizecallback.md)
  A finalization callback function.
### Versions
- [var kMTAudioProcessingTapCallbacksVersion_0: Int32](kmtaudioprocessingtapcallbacksversion_0.md)
  An identifier for version 0 of the callbacks structure.
### Initializers
- [init(version: Int32, clientInfo: UnsafeMutableRawPointer?, init: MTAudioProcessingTapInitCallback?, finalize: MTAudioProcessingTapFinalizeCallback?, prepare: MTAudioProcessingTapPrepareCallback?, unprepare: MTAudioProcessingTapUnprepareCallback?, process: MTAudioProcessingTapProcessCallback)](mtaudioprocessingtapcallbacks/init(version:clientinfo:init:finalize:prepare:unprepare:process:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcallbacks)*