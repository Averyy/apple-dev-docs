# maxPhotoDimensions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The maximum resolution of the requested photo.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var maxPhotoDimensions: CMVideoDimensions { get set }
```

```objc
@property (nonatomic) CMVideoDimensions maxPhotoDimensions;
```

## Discussion

Set a value for this property to request images up to the specified dimensions. Images that a photo output returns may be smaller than the dimensions, but are never be larger. Once set, you can request images with any valid maximum photo dimensions by setting [`maxPhotoDimensions`](../avcapturephotosettings/maxphotodimensions.md) on [`AVCapturePhotoSettings`](../avcapturephotosettings.md) on a per photo basis.

The dimensions you set must match one returned by [`supportedMaxPhotoDimensions`](../avcapturedevice/format/supportedmaxphotodimensions.md) for the current active format.

> 💡 **Tip**:  Changing this property may trigger a lengthy reconfiguration of the capture pipeline, so set this value before calling [`startRunning()`](../avcapturesession/startrunning%28%29.md) on the capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/maxphotodimensions)*