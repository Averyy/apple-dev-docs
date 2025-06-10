# PlaneDetectionProvider

**Framework**: ARKit  
**Kind**: class

A source of live data about planes in a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final class PlaneDetectionProvider
```

#### Overview

Use this provider to indicate to ARKit the types of plane anchors for your app to detect.

## Topics

### Detecting planes
- [init(alignments: [PlaneAnchor.Alignment])](planedetectionprovider/init(alignments:).md)
  Creates a plane detection provider for the types of planes you want to detect.
- [var allAnchors: [PlaneAnchor]](planedetectionprovider/allanchors.md)
  An array that contains all the plane provider’s anchors.
- [var anchorUpdates: AnchorUpdateSequence<PlaneAnchor>](planedetectionprovider/anchorupdates.md)
  A sequence of updates to planes a provider detects.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](planedetectionprovider/requiredauthorizations.md)
  The types of authorizations necessary for detecting planes.
- [static var isSupported: Bool](planedetectionprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports plane detection providers.
### Inspecting a plane detection provider
- [var alignments: [PlaneAnchor.Alignment]](planedetectionprovider/alignments.md)
  The plane alignments that you configure a provider to detect.
- [var state: DataProviderState](planedetectionprovider/state.md)
  The current status of data coming from a provider.
- [var description: String](planedetectionprovider/description.md)
  A textual representation of this plane detection provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Placing content on detected planes](../visionOS/placing-content-on-detected-planes.md)
  Detect horizontal surfaces like tables and floors, as well as vertical planes like walls and doors.
- [struct PlaneAnchor](planeanchor.md)
  An anchor that represents horizontal and vertical planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planedetectionprovider)*