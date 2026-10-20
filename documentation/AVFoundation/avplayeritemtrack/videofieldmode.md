# videoFieldMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A mode that specifies the handling of video frames that contain multiple fields.

**Availability**:
- macOS 10.10+

## Declaration

```swift
nonisolated
var videoFieldMode: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * videoFieldMode;
```

#### Discussion

A value of `nil` indicates default processing of video frames. To deinterlace video fields, set this property value to [`AVPlayerItemTrackVideoFieldModeDeinterlaceFields`](../avplayeritemtrackvideofieldmodedeinterlacefields.md).

## See Also

### Configuring video properties
- [var currentVideoFrameRate: Float](./currentvideoframerate.md)
  The current frame rate of the video track as it plays.
- [let AVPlayerItemTrackVideoFieldModeDeinterlaceFields: String](../avplayeritemtrackvideofieldmodedeinterlacefields.md)
  A video field mode that requests deinterlacing of video fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/videofieldmode)*