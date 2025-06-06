# queryActivity(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Finds the number of players, across player groups, who recently requested a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func queryActivity() async throws -> Int
```

## Parameters

- `completionHandler`: This block receives the following parameters:

## See Also

- [func queryPlayerGroupActivity(Int, withCompletionHandler: ((Int, (any Error)?) -> Void)?)](gkmatchmaker/queryplayergroupactivity(_:withcompletionhandler:).md)
  Finds the number of players in a player group who recently requested a match.
- [func queryQueueActivity(String, withCompletionHandler: ((Int, (any Error)?) -> Void)?)](gkmatchmaker/queryqueueactivity(_:withcompletionhandler:).md)
  Finds the number of players in a specific queue who recently requested a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/queryactivity(completionhandler:))*