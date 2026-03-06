# ImageTrackingProvider

**Framework**: ARKit  
**Kind**: class

A source of live data about a 2D image’s position in a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final class ImageTrackingProvider
```

## Topics

### Creating an image-tracking provider
- [init(referenceImages: [ReferenceImage])](imagetrackingprovider/init(referenceimages:).md)
  Creates an image-tracking provider that tracks the reference images you supply.
- [static var isSupported: Bool](imagetrackingprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports image-tracking providers.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](imagetrackingprovider/requiredauthorizations.md)
  The types of authorizations necessary for tracking images.
### Tracking images
- [var anchorUpdates: AnchorUpdateSequence<ImageAnchor>](imagetrackingprovider/anchorupdates.md)
  A sequence of updates that provide information about images a provider tracks.
### Inspecting an image-tracking provider
- [var state: DataProviderState](imagetrackingprovider/state.md)
  The current status of data coming from a provider.
- [var description: String](imagetrackingprovider/description.md)
  A textual representation of this image tracking provider.
- [var allAnchors: [ImageAnchor]](imagetrackingprovider/allanchors.md)
  An array of all the image anchors the provider is tracking.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Tracking and altering images](tracking-and-altering-images.md)
  Create images from rectangular shapes found in the user’s environment, and augment their appearance.
- [Detecting Images in an AR Experience](detecting-images-in-an-ar-experience.md)
  React to known 2D images in the user’s environment, and use their positions to place AR content.
- [Tracking preregistered images in 3D space](../visionOS/tracking-images-in-3d-space.md)
  Place content based on the current position of a known image in a person’s surroundings.
- [struct ImageAnchor](imageanchor.md)
  A 2D image’s position in a person’s surroundings.
- [struct ReferenceImage](referenceimage.md)
  A 2D image the system uses as a reference to find the same image in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/imagetrackingprovider)*