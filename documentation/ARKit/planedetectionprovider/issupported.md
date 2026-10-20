# isSupported

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the current runtime environment supports plane detection providers.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static var isSupported: Bool { get }
```

## See Also

### Detecting planes
- [init(alignments: [PlaneAnchor.Alignment])](./init%28alignments%29.md)
  Creates a plane detection provider for the types of planes you want to detect.
- [var allAnchors: [PlaneAnchor]](./allanchors.md)
  An array that contains all the plane provider’s anchors.
- [var anchorUpdates: AnchorUpdateSequence<PlaneAnchor>](./anchorupdates.md)
  A sequence of updates to planes a provider detects.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The types of authorizations necessary for detecting planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planedetectionprovider/issupported)*