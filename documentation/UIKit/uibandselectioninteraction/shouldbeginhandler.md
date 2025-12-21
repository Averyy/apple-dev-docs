# shouldBeginHandler

**Framework**: UIKit  
**Kind**: property

The handler that determines whether to start a band selection interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldBeginHandler: ((UIBandSelectionInteraction, CGPoint) -> Bool)? { get set }
```

#### Discussion

This property stores an optional handler block you use to selectively start the interaction. If you provide a handler, the [`UIBandSelectionInteraction`](uibandselectioninteraction.md) object calls your handler upon successful recognition of the appropriate event sequence, but before it starts the interaction. Use your handler to specify whether you want the interaction to proceed.

Your handler block returns a Boolean that indicates whether to start the interaction. Return [`true`](https://developer.apple.com/documentation/Swift/true) to start the interaction or [`false`](https://developer.apple.com/documentation/Swift/false) to ignore the interaction and return the [`UIBandSelectionInteraction`](uibandselectioninteraction.md) object to the [`UIBandSelectionInteraction.State.possible`](uibandselectioninteraction/state-swift.enum/possible.md) state. The interaction object passes the following points to your handler:


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/shouldbeginhandler)*