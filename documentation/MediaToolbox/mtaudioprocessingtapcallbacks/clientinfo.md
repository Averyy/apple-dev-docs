# clientInfo

**Framework**: Media Toolbox  
**Kind**: property  
**Role**: Instance Property

App data that the system passes to the initialization callback.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var clientInfo: UnsafeMutableRawPointer?
```

```c
void * clientInfo;
```

## Discussion

The system passes this value to when it calls the [`MTAudioProcessingTapInitCallback`](../mtaudioprocessingtapinitcallback.md) function. This value can be `NULL`.

## See Also

### Fields
- [var version: Int32](./version.md)
  The version number of the structure.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcallbacks/clientinfo)*