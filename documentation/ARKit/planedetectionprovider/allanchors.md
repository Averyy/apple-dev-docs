# allAnchors

**Framework**: ARKit  
**Kind**: property

An array that contains all the plane provider’s anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final var allAnchors: [PlaneAnchor] { get }
```

## See Also

- [init(alignments: [PlaneAnchor.Alignment])](planedetectionprovider/init(alignments:).md)
  Creates a plane detection provider for the types of planes you want to detect.
- [var anchorUpdates: AnchorUpdateSequence<PlaneAnchor>](planedetectionprovider/anchorupdates.md)
  A sequence of updates to planes a provider detects.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](planedetectionprovider/requiredauthorizations.md)
  The types of authorizations necessary for detecting planes.
- [static var isSupported: Bool](planedetectionprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports plane detection providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planedetectionprovider/allanchors)*