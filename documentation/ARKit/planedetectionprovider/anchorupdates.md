# anchorUpdates

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

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

### Detecting planes
- [init(alignments: [PlaneAnchor.Alignment])](./init%28alignments%29.md)
  Creates a plane detection provider for the types of planes you want to detect.
- [var allAnchors: [PlaneAnchor]](./allanchors.md)
  An array that contains all the plane provider’s anchors.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The types of authorizations necessary for detecting planes.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports plane detection providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planedetectionprovider/anchorupdates)*