# anchorUpdates

**Framework**: ARKit  
**Kind**: property

A sequence of updates to anchors a provider tracks.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var anchorUpdates: AnchorUpdateSequence<WorldAnchor> { get }
```

#### Discussion

An async sequence providing all anchor updates. The provider vends new or updated world anchors via the sequence as they become available.

Identify the anchors you want to react to by calling [`id`](anchor/id.md).

> **Note**: The provider also vends updates for persisted world anchors from previous runs of the app onto the sequence as soon as the world tracking provider is running. World anchors persist across device restarts until you explicitly remove them.

## See Also

- [init()](worldtrackingprovider/init.md)
  Creates a world-tracking provider.
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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/anchorupdates)*