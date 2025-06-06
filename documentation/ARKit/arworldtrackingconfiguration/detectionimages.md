# detectionImages

**Framework**: ARKit  
**Kind**: property

A set of images that ARKit searches for in the user’s environment.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
var detectionImages: Set<ARReferenceImage>! { get set }
```

#### Discussion

Add members to this set for each image that ARKit searches for in the user’s environment. When ARKit  a matching image, the framework creates an [`ARImageAnchor`](arimageanchor.md) object and adds it to the session.

To define the reference images that this property contains, create an asset catalog in Xcode or create [`ARReferenceImage`](arreferenceimage.md) objects programmatically. For more information, see [`Detecting Images in an AR Experience`](detecting-images-in-an-ar-experience.md).

If you set a nonzero value for [`maximumNumberOfTrackedImages`](arworldtrackingconfiguration/maximumnumberoftrackedimages.md), ARKit enables image , which continuously updates the transform for up to four of the reference image anchors as the session progresses. For an example, see [`Tracking and altering images`](tracking-and-altering-images.md).

##### Limit Reference Images for Performance

Image detection accuracy and performance may decline as the number of images in this set increases. For best results, limit your detection image count to no more than around 100.

To detect more than 100 images, your app can allocate a certain amount of time for the first 100 images before moving on to the next 100, and so on. When you update the contents of this property, call [`run(_:options:)`](arsession/run(_:options:).md) again with your app’s configuration to effect the change.

## See Also

- [var maximumNumberOfTrackedImages: Int](arworldtrackingconfiguration/maximumnumberoftrackedimages.md)
  The number of image anchors to monitor closely for position and orientation updates.
- [var automaticImageScaleEstimationEnabled: Bool](arworldtrackingconfiguration/automaticimagescaleestimationenabled.md)
  A flag that instructs the framework to estimate and set the scale of a detected or tracked image on your behalf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/detectionimages)*