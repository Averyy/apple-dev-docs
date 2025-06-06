# Capturing a Bracketed Photo Sequence

**Framework**: AVFoundation

Capture several photos at once, varying parameters like exposure duration or light sensitivity.

#### Overview

Bracketing is a well-known photographic technique in which a sequence of shots is rapidly taken of the same scene, usually varying only in a single parameter such as aperture or shutter speed (exposure length). Experienced photographers use this technique to help them choose the best photos after shooting, or to apply offline post-processing that fuses multiple images together to create extended dynamic range or other special effects.

In iOS, you can use [`AVCapturePhotoOutput`](avcapturephotooutput.md) and [`AVCapturePhotoBracketSettings`](avcapturephotobracketsettings.md) to automatically capture a bracket of photos for each [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) call. Once you’ve built a single-exposure camera in your app (see [`Capturing Still and Live Photos`](capturing-still-and-live-photos.md)), follow these steps to add multi-image bracket support.

##### Choose Bracket Settings

You specify a multi-exposure bracket by providing an array of bracket settings obejcts. iOS offers two types of automatic bracketing:

- Use [`AVCaptureAutoExposureBracketedStillImageSettings`](avcaptureautoexposurebracketedstillimagesettings.md) to create a bracket that varies exposure-compensation values relative to automatic exposure.
- Use [`AVCaptureManualExposureBracketedStillImageSettings`](avcapturemanualexposurebracketedstillimagesettings.md) to create a bracket with custom exposure durations and ISO sensitivity values for each photo in the bracket.

To define a bracket, create an array of one of these types, with values that describe the settings variations you want to capture. For example, the code below defines a bracket that captures three images at three different exposure values.

```swift
// Get AVCaptureBracketedStillImageSettings for a set of exposure values.
let exposureValues: [Float] = [-2, 0, +2]
let makeAutoExposureSettings = AVCaptureAutoExposureBracketedStillImageSettings.autoExposureSettings(exposureTargetBias:)
let exposureSettings = exposureValues.map(makeAutoExposureSettings)

```

> 💡 **Tip**:  In Swift, you can easily convert an array of exposure values to an array of bracket settings by passing the appropriate initializer to the `map(_:)` function, as shown above.

 In Swift, you can easily convert an array of exposure values to an array of bracket settings by passing the appropriate initializer to the `map(_:)` function, as shown above.

##### Create Photo Settings and Shoot

Instead of the [`AVCapturePhotoSettings`](avcapturephotosettings.md) object you create when shooting a single photo, to shoot a bracketed capture you’ll need an [`AVCapturePhotoBracketSettings`](avcapturephotobracketsettings.md) object. This object combines the general settings that apply to all photos in the bracket with your bracket settings that specify how each photo differs from the rest of the bracket.

As with single-image capture, you create a photo settings object by choosing the image codec and file format for the resulting photos, but you also provide the bracket settings you’ve chosen.

```swift
// Create photo settings for HEIF/HEVC capture and no RAW output
// and enable cross-bracket image stabilization.
let photoSettings = AVCapturePhotoBracketSettings(rawPixelFormatType: 0,
    processedFormat: [AVVideoCodecKey : AVVideoCodecType.hevc],
    bracketedSettings: exposureSettings)
photoSettings.isLensStabilizationEnabled =
    self.photoOutput.isLensStabilizationDuringBracketedCaptureSupported

// Shoot the bracket, using a custom class to handle capture delegate callbacks.
let captureProcessor = PhotoCaptureProcessor()
self.photoOutput.capturePhoto(with: photoSettings, delegate: captureProcessor)

```

> 💡 **Tip**:  Turning on [`isLensStabilizationEnabled`](avcapturephotobracketsettings/islensstabilizationenabled.md) (if supported) causes the camera to apply optical image stabilization (OIS) across the entire bracket, so that photos resulting from the bracket still line up with each other even if the device moves during capture.

 Turning on [`isLensStabilizationEnabled`](avcapturephotobracketsettings/islensstabilizationenabled.md) (if supported) causes the camera to apply optical image stabilization (OIS) across the entire bracket, so that photos resulting from the bracket still line up with each other even if the device moves during capture.

##### Handle Bracketed Capture Results

The photo output calls your delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method at least once for each exposure in the bracket, and possibly additional times depending on your capture settings. For example, if you request RAW+HEIF capture in a three-exposure bracket, the photo output calls your delegate’s `didFinishProcessingPhoto` method six times (2 formats × 3 exposures), providing six [`AVCapturePhoto`](avcapturephoto.md) objects.

To keep track of multiple results, compare the [`photoCount`](avcapturephoto/photocount.md) from each photo to the [`expectedPhotoCount`](avcaptureresolvedphotosettings/expectedphotocount.md) of your resolved settings. When those numbers are equal, you’ve received all results from the capture.

## See Also

- [Capturing Photos with Depth](capturing-photos-with-depth.md)
  Get a depth map with a photo to create effects like the system camera’s Portrait mode (on compatible devices).
- [Capturing Uncompressed Image Data](capturing-uncompressed-image-data.md)
  Get processed image data without compression to use for filtering or lossless output.
- [Capturing Thumbnail and Preview Images](capturing-thumbnail-and-preview-images.md)
  Enable delivery of reduced-size images with the main image in a photo capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capturing-a-bracketed-photo-sequence)*