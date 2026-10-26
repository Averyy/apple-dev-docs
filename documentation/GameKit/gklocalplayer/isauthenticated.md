# isAuthenticated

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a local player has signed in to Game Center.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isAuthenticated: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, getter=isAuthenticated) BOOL authenticated;
```

*macOS*

```objc
@property (atomic, readonly, getter=isAuthenticated) BOOL authenticated;
```

## Mentions

- [Authenticating a player](../authenticating-a-player.md)

## See Also

### Authenticating the Local Player
- [var authenticateHandler: ((UIViewController?, (any Error)?) -> Void)?](./authenticatehandler.md)
  A handler that GameKit calls while initializing the local player.
- [func fetchItems(forIdentityVerificationSignature: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](./fetchitems%28foridentityverificationsignature%29.md)
  Generates a signature that you can use to authenticate the local player on your own server.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gkplayerauthenticationdidchangenotificationname.md)
  A notification that posts after GameKit authenticates the local player.
- [GKPlayerAuthenticationDidChangeNotificationName](../gkplayerauthenticationdidchangenotificationname.md)
  A notification that posts after GameKit initializes the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/isauthenticated)*