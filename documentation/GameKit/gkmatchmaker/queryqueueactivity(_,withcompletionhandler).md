# queryQueueActivity(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Finds the number of players in a specific queue who recently requested a match.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+

## Declaration

```swift
func queryQueueActivity(_ queueName: String, withCompletionHandler completionHandler: (@Sendable (Int, (any Error)?) -> Void)? = nil)
```

```swift
func queryQueueActivity(_ queueName: String) async throws -> Int
```

```objc
- (void) queryQueueActivity:(NSString *) queueName withCompletionHandler:(void (^)(NSInteger activity, NSError *error)) completionHandler;
```

## Discussion

To specify a queue name when requesting a match, set the `GKMatchRequest` [`queueName`](../gkmatchrequest/queuename.md) property. For more information, see [Matchmaking rules](../matchmaking-rules.md).

## Parameters

- `queueName`: The name of the queue that Game Center places the match requests in, which it uses for finding players when using matchmaking rules. This uniform type identifier (UTI) contains  only alphanumeric characters (A-Z, a-z, 0-9), hyphens (-), or periods (.).

  The string should be in reverse-DNS format and queue names are case sensitive.
- `completionHandler`: The block that GameKit calls when it completes the request.

  This block receives the following parameters:

  - **`activity`**: The number of match requests in the queue during the previous 60 seconds.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Finding players who request matches
- [func queryActivity(completionHandler: ((Int, (any Error)?) -> Void)?)](./queryactivity%28completionhandler%29.md)
  Finds the number of players, across player groups, who recently requested a match.
- [func queryPlayerGroupActivity(Int, withCompletionHandler: ((Int, (any Error)?) -> Void)?)](./queryplayergroupactivity%28_,withcompletionhandler%29.md)
  Finds the number of players in a player group who recently requested a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/queryqueueactivity(_:withcompletionhandler:))*