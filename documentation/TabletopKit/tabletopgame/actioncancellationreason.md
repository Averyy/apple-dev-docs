# TabletopGame.ActionCancellationReason

**Framework**: TabletopKit  
**Kind**: enum

The possible reasons for cancelling an action or an interaction.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum ActionCancellationReason
```

## Topics

### Cancellation reasons
- [TabletopGame.ActionCancellationReason.actionInvalidated](tabletopgame/actioncancellationreason/actioninvalidated.md)
  The action became invalid due to other cancelled actions
- [TabletopGame.ActionCancellationReason.interactionCancelled](tabletopgame/actioncancellationreason/interactioncancelled.md)
  The action was cancelled back because the interaction that generated it got cancelled

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TabletopGame.Observer](tabletopgame/observer.md)
  A protocol for objects that progress gameplay when players take actions.
- [func addObserver(some TabletopGame.Observer)](tabletopgame/addobserver(_:).md)
- [func removeObserver(some TabletopGame.Observer)](tabletopgame/removeobserver(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/actioncancellationreason)*