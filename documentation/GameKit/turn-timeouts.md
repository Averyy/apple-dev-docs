# Turn Timeouts

**Framework**: GameKit

A timeout for a player to take their turn.

## Topics

### Timeouts
- [var GKTurnTimeoutDefault: TimeInterval](gkturntimeoutdefault.md)
  A one-week time limit to take a turn.
- [var GKTurnTimeoutNone: TimeInterval](gkturntimeoutnone.md)
  No timeout to take a turn.

## See Also

- [func endTurn(withNextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endturn(withnextparticipants:turntimeout:match:completionhandler:).md)
  Passes the turn from the current participant to the next participant.
- [func saveCurrentTurn(withMatch: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/savecurrentturn(withmatch:completionhandler:).md)
  Saves your match data in Game Center without ending the turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/turn-timeouts)*