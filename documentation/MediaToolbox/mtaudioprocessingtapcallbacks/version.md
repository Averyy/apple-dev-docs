# version

**Framework**: Media Toolbox  
**Kind**: property  
**Role**: Instance Property

The version number of the structure.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var version: Int32
```

```c
int version;
```

## Discussion

The value is passed as a parameter to [`MTAudioProcessingTapCreate(_:_:_:_:)`](../mtaudioprocessingtapcreate%28_,_,_,_%29.md). It must be set to [`kMTAudioProcessingTapCallbacksVersion_0`](../kmtaudioprocessingtapcallbacksversion_0.md).

## See Also

### Fields
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
- [var process: MTAudioProcessingTapProcessCallback](./process.md)
  A callback for processing the audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcallbacks/version)*