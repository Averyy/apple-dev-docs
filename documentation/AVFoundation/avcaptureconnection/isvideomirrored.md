# isVideoMirrored

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the connection horizontally flips the video flowing through it.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isVideoMirrored: Bool { get set }
```

#### Discussion

You can apply a mirror-image effect to a video flowing through the connection by setting the value to [`true`](https://developer.apple.com/documentation/swift/true). The mirroring effect only applies to video or depth connections, similar to [`videoRotationAngle`](avcaptureconnection/videorotationangle.md), and if [`isVideoMirroringSupported`](avcaptureconnection/isvideomirroringsupported.md) is [`true`](https://developer.apple.com/documentation/swift/true).

Not all capture connections mirror each frame. For example, a video connection to an [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md) or [`AVCapturePhotoOutput`](avcapturephotooutput.md) instance applies the mirror effect with a QuickTime track matrix or with EXIF tags, respectively.

Capture connections to [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) and [`AVCaptureDepthDataOutput`](avcapturedepthdataoutput.md) instances mirror video frames they provide to their [`captureOutput(_:didOutput:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md) and [`depthDataOutput(_:didOutput:timestamp:connection:)`](avcapturedepthdataoutputdelegate/depthdataoutput(_:didoutput:timestamp:connection:).md) delegate methods, respectively. Each [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) instance uses hardware acceleration to mirror every frame.

> 💡 **Tip**:  Avoid potential performance issues by only mirroring video with a capture connection when necessary.

You can mirror the video of a movie file you record with an [`AVAssetWriter`](avassetwriter.md) instance by applying a scale factor to the [`transform`](avassetwriterinput/transform.md) property of its [`AVAssetWriterInput`](avassetwriterinput.md). For example, you can horizontally flip an image by scaling the x-axis by `-1`. This approach avoids the performance costs that come with rotating each video frame.

```swift
func horizontallyFlipInput(_ assetInput: AVAssetWriterInput) {
    let horiztonalFlip = CGAffineTransform(scaleX: -1.0, y: 1.0)

    assetInput.transform = assetInput.transform.concatenating(horiztonalFlip)
}
```

## See Also

- [var isVideoMirroringSupported: Bool](avcaptureconnection/isvideomirroringsupported.md)
  A Boolean value that indicates whether the connection supports video mirroring.
- [var automaticallyAdjustsVideoMirroring: Bool](avcaptureconnection/automaticallyadjustsvideomirroring.md)
  A Boolean value that indicates whether you can enable mirroring based on a session’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideomirrored)*