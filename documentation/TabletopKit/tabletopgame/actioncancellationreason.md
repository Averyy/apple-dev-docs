# TabletopGame.ActionCancellationReason

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

The possible reasons for cancelling an action or an interaction.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum ActionCancellationReason
```

## Topics

### Cancellation reasons
- [TabletopGame.ActionCancellationReason.actionInvalidated](./actioncancellationreason/actioninvalidated.md)
  The action became invalid due to other cancelled actions
- [TabletopGame.ActionCancellationReason.interactionCancelled](./actioncancellationreason/interactioncancelled.md)
  The action was cancelled back because the interaction that generated it got cancelled

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing actions
- [TabletopGame.Observer](./observer.md)
  A protocol for objects that progress gameplay when players take actions.
- [func addObserver(some TabletopGame.Observer)](./addobserver%28_%29.md)
- [func removeObserver(some TabletopGame.Observer)](./removeobserver%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/actioncancellationreason)*