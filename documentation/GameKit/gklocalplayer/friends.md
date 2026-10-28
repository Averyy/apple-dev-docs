# friends

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The player identifiers for the local player’s friends.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use [`loadFriendPlayers(completionHandler:)`](./loadfriendplayers%28completionhandler%29.md) instead.

## Declaration

```swift
var friends: [String]? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSArray<NSString *> * friends;
```

## Discussion

This property is invalid until a call to [`loadFriendsObsoleted(completionHandler:)`](./loadfriendsobsoleted%28completionhandler%29.md) succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/friends)*