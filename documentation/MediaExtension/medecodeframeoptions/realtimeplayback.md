# realTimePlayback

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that hints to the decoder to use a low-power mode that can’t decode faster than 1x real-time.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var realTimePlayback: Bool { get set }
```

```objc
@property (readwrite) BOOL realTimePlayback;
```

## Discussion

The system sets this value to [`false`](../../Swift/false.md) during all uses other than 1x forward real-time playback, including seeking, playback at other rates, and export.

This hint only applies to the current decode session. If multiple instances of a decoder operate at the same time, it may not be acceptable to use a low-power mode if the system can’t sustain real-time playback across all the streams.

## See Also

### Inspecting frame decoding options
- [var doNotOutputFrame: Bool](./donotoutputframe.md)
  A Boolean value that hints to the decoder whether or not it should emit an image buffer for the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/medecodeframeoptions/realtimeplayback)*