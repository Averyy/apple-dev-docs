# queryPlayerGroupActivity(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Finds the number of players in a player group who recently requested a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func queryPlayerGroupActivity(_ playerGroup: Int) async throws -> Int
```

#### Discussion

Use this method to update your interface. For example, show players the relative activity in each player group. If one group is less active than others, you might display a warning so players are aware that finding a match in that group may take longer.

## Parameters

- `playerGroup`: A number that uniquely identifies a subset of players in your game.
- `completionHandler`: This block receives the following parameters:

## See Also

- [func queryActivity(completionHandler: ((Int, (any Error)?) -> Void)?)](gkmatchmaker/queryactivity(completionhandler:).md)
  Finds the number of players, across player groups, who recently requested a match.
- [func queryQueueActivity(String, withCompletionHandler: ((Int, (any Error)?) -> Void)?)](gkmatchmaker/queryqueueactivity(_:withcompletionhandler:).md)
  Finds the number of players in a specific queue who recently requested a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/queryplayergroupactivity(_:withcompletionhandler:))*