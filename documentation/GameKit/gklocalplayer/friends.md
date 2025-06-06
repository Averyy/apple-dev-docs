# friends

**Framework**: GameKit  
**Kind**: property

The player identifiers for the local player’s friends.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var friends: [String]? { get }
```

#### Discussion

This property is invalid until a call to [`loadFriendsObsoleted(completionHandler:)`](gklocalplayer/loadfriendsobsoleted(completionhandler:).md) succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/friends)*