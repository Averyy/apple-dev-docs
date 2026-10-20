# GKTurnBasedExchangeStatus.complete

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

All recipients of the exchange request replied.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case complete
```

```c
GKTurnBasedExchangeStatusComplete
```

## Mentions

- [Exchanging data between players in turn-based games](../exchanging-data-between-players-in-turn-based-games.md)

## See Also

### Statuses
- [GKTurnBasedExchangeStatus.unknown](./unknown.md)
  The state of the exchange request is unknown.
- [GKTurnBasedExchangeStatus.active](./active.md)
  GameKit sent the exchange request to recipients but not all recipients replied.
- [GKTurnBasedExchangeStatus.resolved](./resolved.md)
  The current participant saved the exchange request.
- [GKTurnBasedExchangeStatus.canceled](./canceled.md)
  The sender canceled the exchange request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/complete)*