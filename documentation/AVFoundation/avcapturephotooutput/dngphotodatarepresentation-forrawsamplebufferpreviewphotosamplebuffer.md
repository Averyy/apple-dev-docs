# dngPhotoDataRepresentation(forRawSampleBuffer:previewPhotoSampleBuffer:)

**Framework**: AVFoundation  
**Kind**: method

Returns data in digital negative (DNG) format corresponding to the captured RAW photo in the specified sample buffer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func dngPhotoDataRepresentation(forRawSampleBuffer rawSampleBuffer: CMSampleBuffer, previewPhotoSampleBuffer: CMSampleBuffer?) -> Data?
```

#### Return Value

A data object containing a DNG representation of the requested photo capture results, or `nil` if the sample buffers cannot be packaged for output.

#### Discussion

After you request a photo capture with the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method, the photo capture output delivers results to your delegate as one or more [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) objects. (See the [`photoOutput(_:didFinishProcessingRawPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:).md) method.) To repackage the sample buffer’s content for output as a DNG file, use this class method. Optionally, you can include metadata in the resulting DNG output by attaching it to the sample buffer before calling this method.

> ❗ **Important**:  The `rawSampleBuffer` parameter must reference a sample buffer from a RAW capture. See the [`rawPhotoPixelFormatType`](avcapturephotosettings/rawphotopixelformattype.md) property for photo capture settings.

 The `rawSampleBuffer` parameter must reference a sample buffer from a RAW capture. See the [`rawPhotoPixelFormatType`](avcapturephotosettings/rawphotopixelformattype.md) property for photo capture settings.

## Parameters

- `rawSampleBuffer`: A sample buffer containing the RAW photo capture result to be formatted for output.
- `previewPhotoSampleBuffer`: An optional additional sample buffer containing a preview-resolution version of the photo capture result, to be added to the DNG output as a thumbnail image. Pass   to skip adding a preview image to the output.

## See Also

- [class func jpegPhotoDataRepresentation(forJPEGSampleBuffer: CMSampleBuffer, previewPhotoSampleBuffer: CMSampleBuffer?) -> Data?](avcapturephotooutput/jpegphotodatarepresentation(forjpegsamplebuffer:previewphotosamplebuffer:).md)
  Returns data in JPEG format corresponding to the captured photo in the specified sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/dngphotodatarepresentation(forrawsamplebuffer:previewphotosamplebuffer:))*