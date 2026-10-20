# isRedEyeReductionEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the camera automatically reduces red-eye when capturing photos.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isRedEyeReductionEnabled: Bool { get }
```

```objc
@property (readonly, getter=isRedEyeReductionEnabled) BOOL redEyeReductionEnabled;
```

## See Also

### Examining photo capture settings
- [var isFlashEnabled: Bool](./isflashenabled.md)
  A Boolean value indicating whether the camera flash fires for this capture.
- [var isVirtualDeviceFusionEnabled: Bool](./isvirtualdevicefusionenabled.md)
  A Boolean value that specifies whether the system automatically uses virtual device image fusion.
- [var isFastCapturePrioritizationEnabled: Bool](./isfastcaptureprioritizationenabled.md)
  A Boolean value that indicates whether the system uses fast capture prioritization when capturing the photo.
- [var isContentAwareDistortionCorrectionEnabled: Bool](./iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the system applies content-aware distortion correction when capturing the photo.
- [var isStillImageStabilizationEnabled: Bool](./isstillimagestabilizationenabled.md)
  A Boolean value indicating whether this capture uses image stabilization.
- [var isDualCameraFusionEnabled: Bool](./isdualcamerafusionenabled.md)
  A Boolean value indicating whether this capture combines image data from a dual camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/isredeyereductionenabled)*