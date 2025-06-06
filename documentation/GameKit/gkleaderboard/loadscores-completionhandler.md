# loadScores(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Retrieves a set of scores from Game Center.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)? = nil)
```

#### Discussion

When you call this method, it creates a new background task to handle the request. The method then returns control to your game. When the task completes, GameKit calls your completion handler on the main thread.

The code below shows an example leaderboard data query. The method for this query initializes a new leaderboard object and configures the [`playerScope`](gkleaderboard/playerscope-swift.property.md), [`timeScope`](gkleaderboard/timescope-swift.property.md), and [`range`](gkleaderboard/range.md) properties to retrieve the top ten scores for today.

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

- `completionHandler`: The block receives the following parameters:

## See Also

- [class func setDefault(String?, withCompletionHandler: (((any Error)?) -> Void)?)](gkleaderboard/setdefault(_:withcompletionhandler:).md)
  Sets the default leaderboard for the local player.
- [class func loadCategories(completionHandler: (([String]?, [String]?, (any Error)?) -> Void)?)](gkleaderboard/loadcategories(completionhandler:).md)
  Loads the list of leaderboard categories along with their corresponding localized titles.
- [class func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](gkleaderboard/loadleaderboards(completionhandler:).md)
  Loads a list of leaderboards from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadscores(completionhandler:))*