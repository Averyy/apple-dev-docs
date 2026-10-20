# isSupported

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the current runtime environment supports world-tracking providers.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
static var isSupported: Bool { get }
```

## See Also

### Tracking objects
- [init()](./init%28%29.md)
  Creates a world-tracking provider.
- [var anchorUpdates: AnchorUpdateSequence<WorldAnchor>](./anchorupdates.md)
  A sequence of updates to anchors a provider tracks.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The types of authorizations necessary for tracking world anchors.
- [var allAnchors: [WorldAnchor]?](./allanchors.md)
  An array of all known world anchors from the world-tracking provider.
- [func addAnchor(WorldAnchor) async throws](./addanchor%28_%29.md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [WorldTrackingProvider.Error](./error.md)
  An error that can occur during a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/issupported)*