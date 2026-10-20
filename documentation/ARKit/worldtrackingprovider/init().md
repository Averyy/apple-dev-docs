# init()

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a world-tracking provider.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

## See Also

### Tracking objects
- [var anchorUpdates: AnchorUpdateSequence<WorldAnchor>](./anchorupdates.md)
  A sequence of updates to anchors a provider tracks.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The types of authorizations necessary for tracking world anchors.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports world-tracking providers.
- [var allAnchors: [WorldAnchor]?](./allanchors.md)
  An array of all known world anchors from the world-tracking provider.
- [func addAnchor(WorldAnchor) async throws](./addanchor%28_%29.md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [WorldTrackingProvider.Error](./error.md)
  An error that can occur during a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/init())*