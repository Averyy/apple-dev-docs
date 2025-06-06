# remove(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Removes a match from Game Center that the local player participants in.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func remove() async throws
```

#### Discussion

If you don’t use the [`GKTurnBasedMatchmakerViewController`](gkturnbasedmatchmakerviewcontroller.md) interface, where players can delete their matches, use this method to delete a match that the local player no longer actively participants in. This method only removes the match from the local player’s Game Center data — it doesn’t impact other participants in the match.

## Parameters

- `completionHandler`: The block receives the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/remove(completionhandler:))*