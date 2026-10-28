# loadScores(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Retrieves a set of scores from Game Center.

**Availability**:
- iOS 4.0+ - Deprecated in 14.0
- iPadOS 4.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use the [`loadEntries(for:timeScope:range:completionHandler:)`](./loadentries%28for,timescope,range,completionhandler%29.md) method instead.

## Declaration

```swift
func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)? = nil)
```

```objc
- (void) loadScoresWithCompletionHandler:(void (^)(NSArray<GKScore *> *scores, NSError *error)) completionHandler;
```

## Discussion

When you call this method, it creates a new background task to handle the request. The method then returns control to your game. When the task completes, GameKit calls your completion handler on the main thread.

The code below shows an example leaderboard data query. The method for this query initializes a new leaderboard object and configures the [`playerScope`](./playerscope-swift.property.md), [`timeScope`](./timescope-swift.property.md), and [`range`](./range.md) properties to retrieve the top ten scores for today.

```objc
- (void) retrieveTopTenScores
{
    GKLeaderboard *leaderboardRequest = [[GKLeaderboard alloc] init];
    if (leaderboardRequest != nil)
    {
        leaderboardRequest.playerScope = GKLeaderboardPlayerScopeGlobal;
        leaderboardRequest.timeScope = GKLeaderboardTimeScopeToday;
        leaderboardRequest.identifier = @"Combined.LandMaps"
        leaderboardRequest.range = NSMakeRange(1,10);
        [leaderboardRequest loadScoresWithCompletionHandler: ^(NSArray *scores, NSError *error) {
            if (error != nil)
            {
                // Handle the error.
            }
            if (scores != nil)
            {
                // Process the score information.
            }
            }];
    }
}
```

You can create a leaderboard request that retrieves scores for a specific list of players.

```objc
- (void) receiveMatchBestScores: (GKMatch*) match
{
    GKLeaderboard *leaderboardRequest = [[GKLeaderboard alloc] initWithPlayers: match.players];
        leaderboardRequest.timeScope = GKLeaderboardTimeScopeAllTime;
        leaderboardRequest.identifier = @"Combined.LandMaps"
        leaderboardRequest.range = NSMakeRange(1,10);
    if (query != nil)
    {
        [query loadScoresWithCompletionHandler: ^(NSArray *scores, NSError *error) {
            if (error != nil)
            {
                // Handle the error.
            }
            if (scores != nil)
            {
                // Process the score information.
            }
        }];
    }
}
```

You can call this method multiple times. Each call represents a different query against the scores stored in Game Center. If you post multiple load operations using the same leaderboard object, any properties that update by loading scores reflect the most recent query that completes. The order that achievement queries process is arbitrary.

## Parameters

- `completionHandler`: A block to call after retrieving the scores from the server.

  The block receives the following parameters:

  - ***scores***: An array of `GKScore` objects that holds the requested scores. If an error occurs, this value may be non-`nil`. In this case, the array holds whatever score data GameKit retrieves from Game Center before the error occurs.
  - ***error***: If an error occurs, this error object describes the error. If the operation completes successfully, the value is `nil`.

## See Also

### Deprecated methods
- [class func setDefault(String?, withCompletionHandler: (((any Error)?) -> Void)?)](./setdefault%28_,withcompletionhandler%29.md)
  Sets the default leaderboard for the local player.
- [class func loadCategories(completionHandler: (([String]?, [String]?, (any Error)?) -> Void)?)](./loadcategories%28completionhandler%29.md)
  Loads the list of leaderboard categories along with their corresponding localized titles.
- [class func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](./loadleaderboards%28completionhandler%29.md)
  Loads a list of leaderboards from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadscores(completionhandler:))*