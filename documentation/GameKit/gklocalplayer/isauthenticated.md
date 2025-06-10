# isAuthenticated

**Framework**: GameKit  
**Kind**: property

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

## Mentions

- [Authenticating a player](authenticating-a-player.md)

## See Also

- [var authenticateHandler: ((UIViewController?, (any Error)?) -> Void)?](gklocalplayer/authenticatehandler.md)
  A handler that GameKit calls while initializing the local player.
- [func fetchItems(forIdentityVerificationSignature: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](gklocalplayer/fetchitems(foridentityverificationsignature:).md)
  Generates a signature that you can use to authenticate the local player on your own server.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GKPlayerAuthenticationDidChangeNotificationName.md)
  A notification that posts after GameKit authenticates the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/isauthenticated)*