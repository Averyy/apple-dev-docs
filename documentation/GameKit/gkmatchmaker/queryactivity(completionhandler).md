# queryActivity(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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
func queryActivity(completionHandler: (@Sendable (Int, (any Error)?) -> Void)? = nil)
```

```swift
func queryActivity() async throws -> Int
```

```objc
- (void) queryActivityWithCompletionHandler:(void (^)(NSInteger activity, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  This block receives the following parameters:

  - **`activity`**: The number of match requests for all player groups during the previous 60 seconds.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Finding players who request matches
- [func queryPlayerGroupActivity(Int, withCompletionHandler: ((Int, (any Error)?) -> Void)?)](./queryplayergroupactivity%28_,withcompletionhandler%29.md)
  Finds the number of players in a player group who recently requested a match.
- [func queryQueueActivity(String, withCompletionHandler: ((Int, (any Error)?) -> Void)?)](./queryqueueactivity%28_,withcompletionhandler%29.md)
  Finds the number of players in a specific queue who recently requested a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/queryactivity(completionhandler:))*