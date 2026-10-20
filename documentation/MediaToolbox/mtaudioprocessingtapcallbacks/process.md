# process

**Framework**: Media Toolbox  
**Kind**: property  
**Role**: Instance Property

A callback for processing the audio.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var process: MTAudioProcessingTapProcessCallback
```

```c
MTAudioProcessingTapProcessCallback process;
```

## See Also

### Fields
- [var version: Int32](./version.md)
  The version number of the structure.
- [var clientInfo: UnsafeMutableRawPointer?](./clientinfo.md)
  App data that the system passes to the initialization callback.
- [var `init`: MTAudioProcessingTapInitCallback?](./init.md)
  A callback to initialize the tap processor.
- [var finalize: MTAudioProcessingTapFinalizeCallback?](./finalize.md)
  A callback to perform any necessary cleanup.
- [var prepare: MTAudioProcessingTapPrepareCallback?](./prepare.md)
  A callback to prepare the tap processor.
- [var unprepare: MTAudioProcessingTapUnprepareCallback?](./unprepare.md)
  A callback to perform any necessary cleanup for previous preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcallbacks/process)*