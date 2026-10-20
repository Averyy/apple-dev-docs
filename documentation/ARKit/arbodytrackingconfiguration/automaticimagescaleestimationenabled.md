# automaticImageScaleEstimationEnabled

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A flag that instructs ARKit to estimate and set the scale of a tracked image on your behalf.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var automaticImageScaleEstimationEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL automaticImageScaleEstimationEnabled;
```

#### Discussion

If set to [`true`](../../Swift/true.md), ARKit uses its knowledge of the world to set an image anchor’s [`estimatedScaleFactor`](../arimageanchor/estimatedscalefactor.md) property, which corrects the image anchor’s position in the physical environment.

Enable this property when you want to detect different sized versions of a reference image. ARKit must know the physical size of an image in the real world to accurately estimate its real-world position. You enable this property to tell ARKit to estimate a recognized image’s physical size before it calculates the real-world position.

## See Also

### Enabling Image Tracking
- [var detectionImages: Set<ARReferenceImage>](./detectionimages.md)
  A set of images that ARKit searches for in the user’s environment.
- [var maximumNumberOfTrackedImages: Int](./maximumnumberoftrackedimages.md)
  The number of image anchors to monitor closely for position and orientation updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodytrackingconfiguration/automaticimagescaleestimationenabled)*