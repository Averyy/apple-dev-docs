# AVCaptureManualExposureBracketedStillImageSettings

**Framework**: AVFoundation  
**Kind**: class

A configuration for defining bracketed photo captures in terms of specific exposure and ISO values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureManualExposureBracketedStillImageSettings
```

## Mentions

- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)

#### Overview

The `AVCaptureManualExposureBracketedStillImageSettings` class is a concrete subclass of the `AVCaptureBracketedStillImageSettings` class used when bracketing exposure duration and ISO.

An `AVCaptureManualExposureBracketedStillImageSettings` instance defines exposure duration and ISO settings that should be applied to one image in a bracket. An array of `AVCaptureManualExposureBracketedStillImageSettings` objects is passed to `captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:` to specify the bracketing.

You can query the minimum and maximum duration and ISO properties of the [`AVCaptureDevice`](avcapturedevice.md) instance supplying data to an [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) instance. If you wish to leave [`exposureDuration`](avcapturemanualexposurebracketedstillimagesettings/exposureduration.md) unchanged for this bracketed still image, you pass the value `AVCaptureExposureDurationCurrent` when creating the instance. To keep the ISO unchanged, you pass `AVCaptureISOCurrent` when creating the instance.

## Topics

### Creating a Manual Bracketed Exposure Settings Instance
- [class func manualExposureSettings(exposureDuration: CMTime, iso: Float) -> Self](avcapturemanualexposurebracketedstillimagesettings/manualexposuresettings(exposureduration:iso:).md)
  Creates a configuration of still image settings using the specified exposure duration and ISO.
### Getting Manual Exposure Setting Values
- [var iso: Float](avcapturemanualexposurebracketedstillimagesettings/iso.md)
  The ISO for the still image.
- [var exposureDuration: CMTime](avcapturemanualexposurebracketedstillimagesettings/exposureduration.md)
  The exposure duration for the still image.

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

- [class AVCaptureAutoExposureBracketedStillImageSettings](avcaptureautoexposurebracketedstillimagesettings.md)
  A configuration for defining bracketed photo captures in terms of bias relative to automatic exposure.
- [class AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md)
  The abstract superclass for bracketed photo capture settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings)*