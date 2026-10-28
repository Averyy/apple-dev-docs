# autoExposureSettings(exposureTargetBias:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates an `AVCaptureAutoExposureBracketedStillImageSettings` using the specified exposure target bias.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class func autoExposureSettings(exposureTargetBias: Float) -> Self
```

```objc
+ (instancetype) autoExposureSettingsWithExposureTargetBias:(float) exposureTargetBias;
```

## Return Value

An initialized `AVCaptureAutoExposureBracketedStillImageSettings` instance.

## Parameters

- `exposureTargetBias`: The exposure target bias. Pass `AVCaptureExposureTargetBiasCurrent` to leave the [`exposureTargetBias`](./exposuretargetbias.md) unchanged for this image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings/autoexposuresettings(exposuretargetbias:))*