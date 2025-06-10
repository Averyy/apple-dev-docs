# AVCapturePhotoBracketSettings

**Framework**: AVFoundation  
**Kind**: class

A specification of the features and settings to use for a photo capture request that captures multiple images with varied settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCapturePhotoBracketSettings
```

## Mentions

- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)

#### Overview

To take a bracketed capture, you create and configure an [`AVCapturePhotoBracketSettings`](avcapturephotobracketsettings.md) object, using [`AVCaptureBracketedStillImageSettings`](avcapturebracketedstillimagesettings.md) objects to describe the individual captures in the bracket, and then pass it to the [`AVCapturePhotoOutput`](avcapturephotooutput.md) [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method.

To request a bracketed capture, follow these steps:

1. Create an array of [`AVCaptureBracketedStillImageSettings`](avcapturebracketedstillimagesettings.md) objects describing the number of images to capture in the bracket and the variations on capture settings between them.
2. Create a bracketed photo settings object with the [`init(rawPixelFormatType:processedFormat:bracketedSettings:)`](avcapturephotobracketsettings/init(rawpixelformattype:processedformat:bracketedsettings:).md) initializer, passing the array of bracketed still image settings, along with the processed format (such as JPEG) or RAW format to capture images in.
3. Configure other settings to share across all images in the bracket, such as the [`isLensStabilizationEnabled`](avcapturephotobracketsettings/islensstabilizationenabled.md) property and certain inherited properties.

> ❗ **Important**:  Bracketed capture supports only the [`isHighResolutionPhotoEnabled`](avcapturephotosettings/ishighresolutionphotoenabled.md) and [`previewPhotoFormat`](avcapturephotosettings/previewphotoformat.md) settings defined by the [`AVCapturePhotoSettings`](avcapturephotosettings.md) superclass. Bracketed capture does not support flash, auto stabilization, or Live Photos—attempting to set any of the corresponding properties raises an exception.

1. Initiate capture by passing the bracketed photo settings object to your photo output’s [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method, along with a delegate object to receive messages about the progress and results of the capture.

> 💡 **Tip**:  Capturing a multiple-image bracket may require allocation of additional resources. See the [`setPreparedPhotoSettingsArray(_:completionHandler:)`](avcapturephotooutput/setpreparedphotosettingsarray(_:completionhandler:).md) method.

1. The photo output calls your delegate’s [`photoOutput(_:didFinishProcessingPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:previewphoto:resolvedsettings:bracketsettings:error:).md) or [`photoOutput(_:didFinishProcessingRawPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:).md) methods many times corresponding to the number of captures in the bracket. Each call provides the [`AVCaptureBracketedStillImageSettings`](avcapturebracketedstillimagesettings.md) object indicating which capture in the bracket the captured image corresponds to.

The following code example illustrates capturing a bracket of three RAW images with varying exposure value settings.

Listing 1. Capturing a Multi-Exposure Bracket

## Topics

### Creating a Bracket Settings Object
- [convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?, bracketedSettings: [AVCaptureBracketedStillImageSettings])](avcapturephotobracketsettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:bracketedsettings:).md)
  Creates a photo settings object for capture in both RAW format and a processed format.
- [convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?, bracketedSettings: [AVCaptureBracketedStillImageSettings])](avcapturephotobracketsettings/init(rawpixelformattype:processedformat:bracketedsettings:).md)
  Creates a photo settings object for the specified bracket of captures, in the specified formats.
### Working with Bracketed Settings
- [var bracketedSettings: [AVCaptureBracketedStillImageSettings]](avcapturephotobracketsettings/bracketedsettings.md)
  An array describing the number of and settings for images to produce in a bracketed capture.
- [var isLensStabilizationEnabled: Bool](avcapturephotobracketsettings/islensstabilizationenabled.md)
  A Boolean value that specifies whether to stabilize the lens for the duration of the bracketed capture.
### Bracketed Settings Types
- [class AVCaptureAutoExposureBracketedStillImageSettings](avcaptureautoexposurebracketedstillimagesettings.md)
  A configuration for defining bracketed photo captures in terms of bias relative to automatic exposure.
- [class AVCaptureManualExposureBracketedStillImageSettings](avcapturemanualexposurebracketedstillimagesettings.md)
  A configuration for defining bracketed photo captures in terms of specific exposure and ISO values.
- [class AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md)
  The abstract superclass for bracketed photo capture settings.

## Relationships

### Inherits From
- [AVCapturePhotoSettings](avcapturephotosettings.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCapturePhotoSettings](avcapturephotosettings.md)
  A specification of the features and settings to use for a single photo capture request.
- [class AVCaptureResolvedPhotoSettings](avcaptureresolvedphotosettings.md)
  A description of the features and settings in use for an in-progress or complete photo capture request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings)*