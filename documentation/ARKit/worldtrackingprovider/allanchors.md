# allAnchors

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An array of all known world anchors from the world-tracking provider.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final var allAnchors: [WorldAnchor]? { get async }
```

#### Discussion

Returns `nil` if the data provider isn’t running, and for other errors.

## See Also

### Tracking objects
- [init()](./init%28%29.md)
  Creates a world-tracking provider.
- [var anchorUpdates: AnchorUpdateSequence<WorldAnchor>](./anchorupdates.md)
  A sequence of updates to anchors a provider tracks.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The types of authorizations necessary for tracking world anchors.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports world-tracking providers.
- [func addAnchor(WorldAnchor) async throws](./addanchor%28_%29.md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [WorldTrackingProvider.Error](./error.md)
  An error that can occur during a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/allanchors)*