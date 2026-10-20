# match(_:didFailWithError:)

**Framework**: GameKit  
**Kind**: method

Handles the local player’s connection errors to a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func match(_ match: GKMatch, didFailWithError error: (any Error)?)
```

#### Discussion

GameKit calls this method when the local player can’t connect to any other players in the match.

## Parameters

- `match`: The match in which the error occurs.
- `error`: The error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:didfailwitherror:))*