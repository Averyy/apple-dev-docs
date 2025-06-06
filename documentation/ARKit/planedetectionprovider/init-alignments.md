# init(alignments:)

**Framework**: ARKit  
**Kind**: init

Creates a plane detection provider for the types of planes you want to detect.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(alignments: [PlaneAnchor.Alignment] = [.horizontal, .vertical])
```

## Parameters

- `alignments`: The types of planes you want to detect — horizontal, vertical, or both.

## See Also

- [var allAnchors: [PlaneAnchor]](planedetectionprovider/allanchors.md)
  An array that contains all the plane provider’s anchors.
- [var anchorUpdates: AnchorUpdateSequence<PlaneAnchor>](planedetectionprovider/anchorupdates.md)
  A sequence of updates to planes a provider detects.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](planedetectionprovider/requiredauthorizations.md)
  The types of authorizations necessary for detecting planes.
- [static var isSupported: Bool](planedetectionprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports plane detection providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planedetectionprovider/init(alignments:))*