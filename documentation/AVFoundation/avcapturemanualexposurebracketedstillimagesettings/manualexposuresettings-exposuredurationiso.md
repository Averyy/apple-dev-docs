# manualExposureSettings(exposureDuration:iso:)

**Framework**: AVFoundation  
**Kind**: method

Creates a configuration of still image settings using the specified exposure duration and ISO.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class func manualExposureSettings(exposureDuration duration: CMTime, iso ISO: Float) -> Self
```

#### Return Value

An initialized `AVCaptureManualExposureBracketedStillImageSettings` instance.

## Parameters

- `duration`: The exposure duration in seconds. Pass   to leave the duration unchanged for this bracketed image.
- `ISO`: The film speed in the ISO format. Pass   to leave the ISO unchanged for this bracketed image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/manualexposuresettings(exposureduration:iso:))*