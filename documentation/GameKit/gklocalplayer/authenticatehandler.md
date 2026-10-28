# authenticateHandler

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A handler that GameKit calls while initializing the local player.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var authenticateHandler: ((UIViewController?, (any Error)?) -> Void)? { get set }
```

*macOS*

```swift
var authenticateHandler: ((NSViewController?, (any Error)?) -> Void)? { get set }
```

*watchOS*

```swift
var authenticateHandler: (((any Error)?) -> Void)? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) void (^authenticateHandler)(UIViewController *viewController, NSError *error);
```

*macOS*

```objc
@property (atomic, copy, nullable) void (^)(NSViewController *, NSError *) authenticateHandler;
```

*watchOS*

```objc
@property (atomic, copy, nullable) void (^)(NSError *) authenticateHandler;
```

## Mentions

- [Authenticating a player](../authenticating-a-player.md)
- [Initializing and configuring Game Center](../initializing-and-configuring-game-center.md)

## Discussion

Before you can access any Game Center data and use GameKit features, you need to initialize the local player to ensure the player signs in to Game Center on the device running your game. Set this property to a method that GameKit invokes during the initialization process. If `viewController` is `nil`, Game Center initializes the player and the player can start your game. Otherwise, present the view controller so the player can perform any additional actions to complete the process.

Game Center may show a brief initialization screen if the player isn’t already signed into Game Center.

For more information about initializing Game Center with a local player, see [Authenticating a player](../authenticating-a-player.md).

## Parameters

- `viewController`: A view controller that your game presents to the local player so they can perform any necessary actions to finish initialization, or `nil` if the initialization process is complete.
- `error`: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Authenticating the Local Player
- [var isAuthenticated: Bool](./isauthenticated.md)
  A Boolean value that indicates whether a local player has signed in to Game Center.
- [func fetchItems(forIdentityVerificationSignature: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](./fetchitems%28foridentityverificationsignature%29.md)
  Generates a signature that you can use to authenticate the local player on your own server.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gkplayerauthenticationdidchangenotificationname.md)
  A notification that posts after GameKit authenticates the local player.
- [GKPlayerAuthenticationDidChangeNotificationName](../gkplayerauthenticationdidchangenotificationname.md)
  A notification that posts after GameKit initializes the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/authenticatehandler)*