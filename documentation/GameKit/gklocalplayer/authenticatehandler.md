# authenticateHandler

**Framework**: GameKit  
**Kind**: property

A handler that GameKit calls while authenticating the local player.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var authenticateHandler: ((UIViewController?, (any Error)?) -> Void)? { get set }
```

## Mentions

- [Authenticating a player](authenticating-a-player.md)

#### Discussion

Before you can access any Game Center data and use GameKit features, you need to authenticate the local player to ensure the player signs in to Game Center on the device running your game. Set this property to a method that GameKit invokes during the authentication process. If `viewController` is `nil`, Game Center authenticates the player and the player can start your game. Otherwise, present the view controller so the player can perform any additional actions to complete authentication.

For more information about the authentication of the local player, see [`Authenticating a player`](authenticating-a-player.md).

## Parameters

- `viewController`: A view controller that your game presents to the local player so they can perform any necessary actions to finish authentication, or   if the authentication process is complete.
- `error`: Describes an error if it occurs, or   if the operation completes.

## See Also

- [var isAuthenticated: Bool](gklocalplayer/isauthenticated.md)
  A Boolean value that indicates whether a local player has signed in to Game Center.
- [func fetchItems(forIdentityVerificationSignature: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](gklocalplayer/fetchitems(foridentityverificationsignature:).md)
  Generates a signature that you can use to authenticate the local player on your own server.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../foundation/nsnotification/name/1515396-gkplayerauthenticationdidchangen.md)
  A notification that posts after GameKit authenticates the local player. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/authenticatehandler)*