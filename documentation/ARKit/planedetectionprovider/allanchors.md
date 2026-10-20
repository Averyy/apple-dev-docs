# allAnchors

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An array that contains all the plane provider’s anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final var allAnchors: [PlaneAnchor] { get }
```

## See Also

### Detecting planes
- [init(alignments: [PlaneAnchor.Alignment])](./init%28alignments%29.md)
  Creates a plane detection provider for the types of planes you want to detect.
- [var anchorUpdates: AnchorUpdateSequence<PlaneAnchor>](./anchorupdates.md)
  A sequence of updates to planes a provider detects.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The types of authorizations necessary for detecting planes.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports plane detection providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planedetectionprovider/allanchors)*