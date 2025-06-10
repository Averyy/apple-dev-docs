# init()

**Framework**: ARKit  
**Kind**: init

Creates a world-tracking provider.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
init()
```

## See Also

- [var anchorUpdates: AnchorUpdateSequence<WorldAnchor>](worldtrackingprovider/anchorupdates.md)
  A sequence of updates to anchors a provider tracks.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](worldtrackingprovider/requiredauthorizations.md)
  The types of authorizations necessary for tracking world anchors.
- [static var isSupported: Bool](worldtrackingprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports world-tracking providers.
- [var allAnchors: [WorldAnchor]?](worldtrackingprovider/allanchors.md)
  An array of all known world anchors from the world-tracking provider.
- [func addAnchor(WorldAnchor) async throws](worldtrackingprovider/addanchor(_:).md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [WorldTrackingProvider.Error](worldtrackingprovider/error.md)
  An error that can occur during a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/init())*