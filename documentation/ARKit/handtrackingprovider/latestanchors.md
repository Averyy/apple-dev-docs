# latestAnchors

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The most recent hand anchors for each hand.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var latestAnchors: (leftHand: HandAnchor?, rightHand: HandAnchor?) { get }
```

## Discussion

Both elements of this tuple are `nil` when the associated [`HandTrackingProvider`](../handtrackingprovider.md) isn’t running.

> **Note**: For apps compiled against the visionOS 1.0 SDK, accessing this tuple consumes its values and sets them to `nil` until the next anchor update.

## See Also

### Observing hand anchor data
- [var anchorUpdates: AnchorUpdateSequence<HandAnchor>](./anchorupdates.md)
  A sequence of updates for all hands that a provider tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handtrackingprovider/latestanchors)*