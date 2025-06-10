# HandTrackingProvider

**Framework**: ARKit  
**Kind**: class

A source of live data about the position of a person’s hands and hand joints.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final class HandTrackingProvider
```

## Topics

### Creating a hand-tracking provider
- [init()](handtrackingprovider/init.md)
  Creates a hand-tracking provider.
- [static var isSupported: Bool](handtrackingprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports hand-tracking providers.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](handtrackingprovider/requiredauthorizations.md)
  The types of authorizations necessary for tracking hands.
### Observing hand anchor data
- [var anchorUpdates: AnchorUpdateSequence<HandAnchor>](handtrackingprovider/anchorupdates.md)
  A sequence of updates for all hands that a provider tracks.
- [var latestAnchors: (leftHand: HandAnchor?, rightHand: HandAnchor?)](handtrackingprovider/latestanchors.md)
  The most recent hand anchors for each hand.
### Inspecting a hand-tracking provider
- [var state: DataProviderState](handtrackingprovider/state.md)
  The current status of data coming from a provider.
- [var description: String](handtrackingprovider/description.md)
  A textual representation of this hand tracking provider.
- [func handAnchors(at: TimeInterval) -> (leftHand: HandAnchor?, rightHand: HandAnchor?)](handtrackingprovider/handanchors(at:).md)
  Queries for hand anchors at the provided target timestamp.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Happy Beam](../visionOS/happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [struct HandAnchor](handanchor.md)
  A hand’s position in a person’s surroundings.
- [struct HandSkeleton](handskeleton.md)
  A collection of joints in a hand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handtrackingprovider)*