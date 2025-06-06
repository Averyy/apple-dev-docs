# automaticImageScaleEstimationEnabled

**Framework**: ARKit  
**Kind**: property

A flag that instructs ARKit to estimate and set the scale of a tracked image on your behalf.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var automaticImageScaleEstimationEnabled: Bool { get set }
```

#### Discussion

If set to [`true`](https://developer.apple.com/documentation/swift/true), ARKit uses its knowledge of the world to set an image anchor’s [`estimatedScaleFactor`](arimageanchor/estimatedscalefactor.md) property, which corrects the image anchor’s position in the physical environment.

Enable this property when you want to detect different sized versions of a reference image. ARKit must know the physical size of an image in the real world to accurately estimate its real-world position. You enable this property to tell ARKit to estimate a recognized image’s physical size before it calculates the real-world position.

## See Also

- [var detectionImages: Set<ARReferenceImage>](arbodytrackingconfiguration/detectionimages.md)
  A set of images that ARKit searches for in the user’s environment.
- [var maximumNumberOfTrackedImages: Int](arbodytrackingconfiguration/maximumnumberoftrackedimages.md)
  The number of image anchors to monitor closely for position and orientation updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodytrackingconfiguration/automaticimagescaleestimationenabled)*