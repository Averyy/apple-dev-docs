# Deprecated symbols

**Framework**: AVFoundation

Review unsupported symbols and their replacements.

## Topics

### Getting formatted output
- [class func jpegPhotoDataRepresentation(forJPEGSampleBuffer: CMSampleBuffer, previewPhotoSampleBuffer: CMSampleBuffer?) -> Data?](avcapturephotooutput/jpegphotodatarepresentation(forjpegsamplebuffer:previewphotosamplebuffer:).md)
  Returns data in JPEG format corresponding to the captured photo in the specified sample buffer.
- [class func dngPhotoDataRepresentation(forRawSampleBuffer: CMSampleBuffer, previewPhotoSampleBuffer: CMSampleBuffer?) -> Data?](avcapturephotooutput/dngphotodatarepresentation(forrawsamplebuffer:previewphotosamplebuffer:).md)
  Returns data in digital negative (DNG) format corresponding to the captured RAW photo in the specified sample buffer.
### Configuring dual camera capture
- [var isDualCameraFusionSupported: Bool](avcapturephotooutput/isdualcamerafusionsupported.md)
  A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device.
- [var isDualCameraDualPhotoDeliverySupported: Bool](avcapturephotooutput/isdualcameradualphotodeliverysupported.md)
  A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device.
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](avcapturephotooutput/isdualcameradualphotodeliveryenabled.md)
  A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device.
### Configuring high-resolution still capture
- [var isHighResolutionCaptureEnabled: Bool](avcapturephotooutput/ishighresolutioncaptureenabled.md)
  A Boolean value that specifies whether to configure the capture pipeline for high resolution still image capture.
### Monitoring the visible scene
- [var isStillImageStabilizationScene: Bool](avcapturephotooutput/isstillimagestabilizationscene.md)
  A Boolean value indicating whether the scene currently being previewed by the camera warrants image stabilization.
### Determining available settings
- [var isStillImageStabilizationSupported: Bool](avcapturephotooutput/isstillimagestabilizationsupported.md)
  A Boolean value indicating whether the capture output currently supports automatic stabilization for still image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput-deprecated-symbols)*