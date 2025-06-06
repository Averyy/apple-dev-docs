# requiredAuthorizations

**Framework**: ARKit  
**Kind**: property

The types of authorizations necessary for detecting planes.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static var requiredAuthorizations: [ARKitSession.AuthorizationType] { get }
```

#### Discussion

You can use this property to pass plane detection requirements to the [`requestAuthorization(for:)`](arkitsession/requestauthorization(for:).md) method.

## See Also

- [init(alignments: [PlaneAnchor.Alignment])](planedetectionprovider/init(alignments:).md)
  Creates a plane detection provider for the types of planes you want to detect.
- [var allAnchors: [PlaneAnchor]](planedetectionprovider/allanchors.md)
  An array that contains all the plane provider’s anchors.
- [var anchorUpdates: AnchorUpdateSequence<PlaneAnchor>](planedetectionprovider/anchorupdates.md)
  A sequence of updates to planes a provider detects.
- [static var isSupported: Bool](planedetectionprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports plane detection providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planedetectionprovider/requiredauthorizations)*