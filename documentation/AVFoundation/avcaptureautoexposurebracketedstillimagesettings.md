# AVCaptureAutoExposureBracketedStillImageSettings

**Framework**: AVFoundation  
**Kind**: class

A configuration for defining bracketed photo captures in terms of bias relative to automatic exposure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureAutoExposureBracketedStillImageSettings
```

## Mentions

- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)

#### Overview

An [`AVCaptureAutoExposureBracketedStillImageSettings`](avcaptureautoexposurebracketedstillimagesettings.md) instance defines the exposure target bias setting that should be applied to one image in a bracket. An array of `AVCaptureAutoExposureBracketedStillImageSettings` objects is passed to `captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:` to specify the bracketing.

The minimum and maximum exposure target bias are properties of the [`AVCaptureDevice`](avcapturedevice.md) instance supplying data to an [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) instance. If you wish to leave [`exposureTargetBias`](avcaptureautoexposurebracketedstillimagesettings/exposuretargetbias.md) unchanged for this bracketed still image, you may pass the value `AVCaptureExposureTargetBiasCurrent`.

## Topics

### Creating an Auto Exposure Settings Instance
- [class func autoExposureSettings(exposureTargetBias: Float) -> Self](avcaptureautoexposurebracketedstillimagesettings/autoexposuresettings(exposuretargetbias:).md)
  Creates an `AVCaptureAutoExposureBracketedStillImageSettings` using the specified exposure target bias.
### Getting the Exposure Target Bias
- [var exposureTargetBias: Float](avcaptureautoexposurebracketedstillimagesettings/exposuretargetbias.md)
  The exposure bias for the auto exposure bracketed settings

## Relationships

### Inherits From
- [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureManualExposureBracketedStillImageSettings](avcapturemanualexposurebracketedstillimagesettings.md)
  A configuration for defining bracketed photo captures in terms of specific exposure and ISO values.
- [class AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md)
  The abstract superclass for bracketed photo capture settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings)*