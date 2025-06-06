# Capturing Thumbnail and Preview Images

**Framework**: AVFoundation

Enable delivery of reduced-size images with the main image in a photo capture.

#### Overview

Generating your own preview or thumbnail images from high-resolution source images can be difficult and time-consuming. Instead, use [`AVCapturePhotoOutput`](avcapturephotooutput.md) to get easy, fast preview and thumbnail generation as part of your capture process.

In the capture system, the names  and  have specific meanings:

- A  is a reduced-size (screen resolution or smaller) version of the photo, in an uncompressed format, delivered only in memory for purposes of displaying feedback shortly after capture. For example, the system Camera app displays a preview image of the last captured photo.
- A  is a smaller version of the photo, encoded in a compressed format and embedded in the output image file for use by other software. For example, image browsers reading a folder full of images can preview the contents of many files without reading and decoding each file’s entire contents.

You can add preview images, thumbnail images, or both with minor additions to any [`AVCapturePhotoOutput`](avcapturephotooutput.md) workflow (see [`Capturing Still and Live Photos`](capturing-still-and-live-photos.md) and related topics).

##### Choose Settings

After you create an [`AVCapturePhotoSettings`](avcapturephotosettings.md) object for the kind of photo you plan to shoot, use its [`previewPhotoFormat`](avcapturephotosettings/previewphotoformat.md) dictionary to specify the format and size of preview image you want.

```swift
if photoSettings.availablePreviewPhotoPixelFormatTypes.count > 0 {
    photoSettings.previewPhotoFormat = [
        kCVPixelBufferPixelFormatTypeKey : photoSettings.availablePreviewPhotoPixelFormatTypes.first!,
        kCVPixelBufferWidthKey : 512,
        kCVPixelBufferHeightKey : 512
    ] as [String: Any]
}

```

To request that a thumbnail version of the photo be embedded in the resulting image file, use the photo settings object’s [`embeddedThumbnailPhotoFormat`](avcapturephotosettings/embeddedthumbnailphotoformat.md) dictionary to specify the format and size of the thumbnail.

```swift
photoSettings.embeddedThumbnailPhotoFormat = [
    AVVideoCodecKey: AVVideoCodecType.jpeg,
    AVVideoWidthKey: 1024,
    AVVideoHeightKey: 1024,
]
```

##### Handle Results

When the photo output calls your delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method, you can get the preview image from the [`AVCapturePhoto`](avcapturephoto.md) [`previewPixelBuffer`](avcapturephoto/previewpixelbuffer.md) property. A pixel buffer provides direct access to pixel data, so you can process or display it using other graphics technologies such as Metal, Vision, or Core Image. One way to simply display the preview image in your UI is to use Core Image to wrap the buffer in a UIImage object:

```swift
func showPreview(for photo: AVCapturePhoto) {
    guard let previewPixelBuffer = photo.previewPixelBuffer else { return }
    let ciImage = CIImage(cvPixelBuffer: previewPixelBuffer)
    let uiImage = UIImage(ciImage: ciImage)
    self.imageView.image = uiImage
}

```

If you requested an embedded thumbnail image, that image isn’t directly accessible from the [`AVCapturePhoto`](avcapturephoto.md) object—it’s embedded in the image file data that you get by calling the photo object’s [`fileDataRepresentation()`](avcapturephoto/filedatarepresentation().md) method.

## See Also

- [Capturing Photos with Depth](capturing-photos-with-depth.md)
  Get a depth map with a photo to create effects like the system camera’s Portrait mode (on compatible devices).
- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)
  Capture several photos at once, varying parameters like exposure duration or light sensitivity.
- [Capturing Uncompressed Image Data](capturing-uncompressed-image-data.md)
  Get processed image data without compression to use for filtering or lossless output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capturing-thumbnail-and-preview-images)*