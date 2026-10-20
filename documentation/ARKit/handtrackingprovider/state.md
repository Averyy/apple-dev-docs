# state

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The current status of data coming from a provider.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var state: DataProviderState { get }
```

## See Also

### Inspecting a hand-tracking provider
- [var description: String](./description.md)
  A textual representation of this hand tracking provider.
- [func handAnchors(at: TimeInterval) -> (leftHand: HandAnchor?, rightHand: HandAnchor?)](./handanchors%28at%29.md)
  Queries for hand anchors at the provided target timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handtrackingprovider/state)*