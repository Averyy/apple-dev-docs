# rematch(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Creates a new match with the players from an existing match.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func rematch() async throws -> GKMatch
```

#### Discussion

This method uses automatching to recreate a previous match. If you use this method to create a match, each instance of your game on each device should call this same method.

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [func disconnect()](gkmatch/disconnect.md)
  Disconnects the local player from the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/rematch(completionhandler:))*