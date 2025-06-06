# init

**Framework**: Media Toolbox  
**Kind**: property

A callback to initialize the tap processor.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var `init`: MTAudioProcessingTapInitCallback?
```

#### Discussion

This callback is called before [`MTAudioProcessingTapCreate(_:_:_:_:)`](mtaudioprocessingtapcreate(_:_:_:_:).md) returns. This field can be `NULL`.

## See Also

- [var version: Int32](mtaudioprocessingtapcallbacks/version.md)
  The version number of the structure.
- [var clientInfo: UnsafeMutableRawPointer?](mtaudioprocessingtapcallbacks/clientinfo.md)
  App data that the system passes to the initialization callback.
- [var finalize: MTAudioProcessingTapFinalizeCallback?](mtaudioprocessingtapcallbacks/finalize.md)
  A callback to perform any necessary cleanup.
- [var prepare: MTAudioProcessingTapPrepareCallback?](mtaudioprocessingtapcallbacks/prepare.md)
  A callback to prepare the tap processor.
- [var unprepare: MTAudioProcessingTapUnprepareCallback?](mtaudioprocessingtapcallbacks/unprepare.md)
  A callback to perform any necessary cleanup for previous preparation.
- [var process: MTAudioProcessingTapProcessCallback](mtaudioprocessingtapcallbacks/process.md)
  A callback for processing the audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcallbacks/init)*