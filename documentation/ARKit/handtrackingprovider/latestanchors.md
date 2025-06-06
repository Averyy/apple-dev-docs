# latestAnchors

**Framework**: ARKit  
**Kind**: property

The most recent hand anchors for each hand.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var latestAnchors: (leftHand: HandAnchor?, rightHand: HandAnchor?) { get }
```

#### Discussion

Accessing this tuple consumes its values and sets them to `nil` until the next anchor update. Both elements of this tuple are `nil` when the associated [`HandTrackingProvider`](handtrackingprovider.md) isn’t running.

## See Also

- [var anchorUpdates: AnchorUpdateSequence<HandAnchor>](handtrackingprovider/anchorupdates.md)
  A sequence of updates for all hands that a provider tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handtrackingprovider/latestanchors)*