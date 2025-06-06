# availableLivePhotoVideoCodecTypes

**Framework**: AVFoundation  
**Kind**: property

An array of video codecs currently available for Live Photo movie captures.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var availableLivePhotoVideoCodecTypes: [AVVideoCodecType] { get }
```

#### Discussion

By default, Live Photo capture encodes the movie portion of a Live Photo using the H.264 codec. To use a different codec, set the [`livePhotoVideoCodecType`](avcapturephotosettings/livephotovideocodectype.md) property of your photo settings object to one of the values in this array.

The system always presents its default video codec first. If you haven’t added the photo output to an [`AVCaptureSession`](avcapturesession.md) with a video source, no codecs are available.

This property is key-value observable.

## See Also

- [var isLivePhotoCaptureSupported: Bool](avcapturephotooutput/islivephotocapturesupported.md)
  A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [var isLivePhotoCaptureEnabled: Bool](avcapturephotooutput/islivephotocaptureenabled.md)
  A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [var isLivePhotoCaptureSuspended: Bool](avcapturephotooutput/islivephotocapturesuspended.md)
  A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool](avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop.md)
  A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [var isLivePhotoAutoTrimmingEnabled: Bool](avcapturephotooutput/islivephotoautotrimmingenabled.md)
  A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablelivephotovideocodectypes)*