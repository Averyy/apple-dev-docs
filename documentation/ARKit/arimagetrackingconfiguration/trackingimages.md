# trackingImages

**Framework**: ARKit  
**Kind**: property

A set of images that ARKit searches for and tracks in the user’s environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var trackingImages: Set<ARReferenceImage> { get set }
```

#### Discussion

Add members to this set for each image that ARKit searches for in the user’s environment. When ARKit observes a matching image, the framework creates an [`ARImageAnchor`](arimageanchor.md) object and adds it to the session. If you set [`maximumNumberOfTrackedImages`](arworldtrackingconfiguration/maximumnumberoftrackedimages.md) to a value greater than `1`, ARKit tracks multiple images as the session progresses, up to a maximum of four.

To define the reference images that this property contains, create an asset catalog in Xcode or create [`ARReferenceImage`](arreferenceimage.md) objects programmatically. For an example, see [`Tracking and altering images`](tracking-and-altering-images.md).

## See Also

- [var maximumNumberOfTrackedImages: Int](arimagetrackingconfiguration/maximumnumberoftrackedimages.md)
  The number of image anchors to monitor closely for position and orientation updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arimagetrackingconfiguration/trackingimages)*