# requiredAuthorizations

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The types of authorizations necessary for tracking world anchors.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
static var requiredAuthorizations: [ARKitSession.AuthorizationType] { get }
```

## See Also

### Tracking objects
- [init()](./init%28%29.md)
  Creates a world-tracking provider.
- [var anchorUpdates: AnchorUpdateSequence<WorldAnchor>](./anchorupdates.md)
  A sequence of updates to anchors a provider tracks.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports world-tracking providers.
- [var allAnchors: [WorldAnchor]?](./allanchors.md)
  An array of all known world anchors from the world-tracking provider.
- [func addAnchor(WorldAnchor) async throws](./addanchor%28_%29.md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [WorldTrackingProvider.Error](./error.md)
  An error that can occur during a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/requiredauthorizations)*