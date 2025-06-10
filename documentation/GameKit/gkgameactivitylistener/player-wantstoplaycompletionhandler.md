# player(_:wantsToPlay:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Called when a player intends to play for a specific game activity. A completion handler block is provided to indicate whether the activity was successfully handled.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
optional func player(_ player: GKPlayer, wantsToPlay activity: GKGameActivity) async -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitylistener/player(_:wantstoplay:completionhandler:))*