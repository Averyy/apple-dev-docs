# WorldTrackingProvider

**Framework**: ARKit  
**Kind**: class

A source of live data about the device pose and anchors in a person’s surroundings.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
final class WorldTrackingProvider
```

## Topics

### Tracking objects
- [init()](worldtrackingprovider/init.md)
  Creates a world-tracking provider.
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
### Stopping object tracking
- [func removeAnchor(WorldAnchor) async throws](worldtrackingprovider/removeanchor(_:).md)
  Removes a world anchor from a world-tracking provider.
- [func removeAnchor(forID: UUID) async throws](worldtrackingprovider/removeanchor(forid:).md)
  Removes a world anchor from a world-tracking provider based on its ID.
### Predicting device pose
- [func queryDeviceAnchor(atTimestamp: TimeInterval) -> DeviceAnchor?](worldtrackingprovider/querydeviceanchor(attimestamp:).md)
  The predicted pose of the current device at a given time.
### Inspecting a world-tracking provider
- [var state: DataProviderState](worldtrackingprovider/state.md)
  The current status of data coming from a provider.
- [var description: String](worldtrackingprovider/description.md)
  A textual description of a world-tracking provider.
### Instance Properties
- [var worldAnchorSharingAvailability: some AsyncSequence<WorldTrackingProvider.WorldAnchorSharingAvailability, Never>](worldtrackingprovider/worldanchorsharingavailability-swift.property.md)
  A sequence of world anchor sharing availability changes.
### Instance Methods
- [func removeAllAnchors() async throws](worldtrackingprovider/removeallanchors.md)
  Removes all known world anchors from world tracking.
### Enumerations
- [WorldTrackingProvider.WorldAnchorSharingAvailability](worldtrackingprovider/worldanchorsharingavailability-swift.enum.md)
  Enumeration indicating the availability of world anchor sharing.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Tracking specific points in world space](../visionOS/tracking-points-in-world-space.md)
  Retrieve the position and orientation of anchors your app stores in ARKit.
- [struct WorldAnchor](worldanchor.md)
  A fixed location in a person’s surroundings.
- [struct DeviceAnchor](deviceanchor.md)
  The position and orientation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider)*