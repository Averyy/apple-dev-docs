# requiredAuthorizations

**Framework**: ARKit  
**Kind**: property

The types of authorizations necessary for tracking world anchors.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
static var requiredAuthorizations: [ARKitSession.AuthorizationType] { get }
```

## See Also

- [init()](worldtrackingprovider/init.md)
  Creates a world-tracking provider.
- [var anchorUpdates: AnchorUpdateSequence<WorldAnchor>](worldtrackingprovider/anchorupdates.md)
  A sequence of updates to anchors a provider tracks.
- [static var isSupported: Bool](worldtrackingprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports world-tracking providers.
- [var allAnchors: [WorldAnchor]?](worldtrackingprovider/allanchors.md)
  An array of all known world anchors from the world-tracking provider.
- [func addAnchor(WorldAnchor) async throws](worldtrackingprovider/addanchor(_:).md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [WorldTrackingProvider.Error](worldtrackingprovider/error.md)
  An error that can occur during a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/requiredauthorizations)*