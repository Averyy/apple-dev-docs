# anchorUpdates

**Framework**: ARKit  
**Kind**: property

A sequence of updates to planes a provider detects.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var anchorUpdates: AnchorUpdateSequence<PlaneAnchor> { get }
```

#### Discussion

The system adds, updates, or removes plane anchors when this sequence provides updates.

## See Also

- [init(alignments: [PlaneAnchor.Alignment])](planedetectionprovider/init(alignments:).md)
  Creates a plane detection provider for the types of planes you want to detect.
- [var allAnchors: [PlaneAnchor]](planedetectionprovider/allanchors.md)
  An array that contains all the plane provider’s anchors.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](planedetectionprovider/requiredauthorizations.md)
  The types of authorizations necessary for detecting planes.
- [static var isSupported: Bool](planedetectionprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports plane detection providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planedetectionprovider/anchorupdates)*