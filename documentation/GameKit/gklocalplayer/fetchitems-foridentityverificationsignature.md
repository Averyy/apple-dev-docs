# fetchItems(forIdentityVerificationSignature:)

**Framework**: GameKit  
**Kind**: method

Generates a signature that you can use to authenticate the local player on your own server.

**Availability**:
- iOS 13.5+
- iPadOS 13.5+
- Mac Catalyst 13.5+
- macOS 10.15.5+
- tvOS 13.4.8+
- visionOS 1.0+
- watchOS 6.5+

## Declaration

```swift
func fetchItemsForIdentityVerificationSignature() async throws -> (URL, Data, Data, UInt64)
```

#### Discussion

To generate a signature for your authentication server, you perform steps in the game and pass data to the server, which completes the process.

In your game, follow these steps:

1. Call the [`fetchItems(forIdentityVerificationSignature:)`](gklocalplayer/fetchitems(foridentityverificationsignature:).md) method.
2. Send the completion handler `publicKeyURL`, `signature`, `salt`, and `timestamp` parameters to your authentication server.
3. Share the [`teamPlayerID`](gkplayer/teamplayerid.md) and the bundle ID (see [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier)) with the server. For Apple Arcade games, share the [`gamePlayerID`](gkplayer/gameplayerid.md) instead of the [`teamPlayerID`](gkplayer/teamplayerid.md).

On the server, perform these steps:

1. To mitigate replay attacks, make sure the `timestamp` parameter is recent, and to avoid high network overhead, respect the cache expiration headers.
2. Download the public key using the `publicKeyURL` parameter.
3. Verify with the appropriate signing authority that Apple signed the public key.
4. Concatenate the following information into a data buffer in this order: the [`teamPlayerID`](gkplayer/teamplayerid.md) (or [`gamePlayerID`](gkplayer/gameplayerid.md) for Apple Arcade) property in UTF-8 format, the bundle ID in UTF-8 format, the `timestamp` parameter in big-endian UInt64 format, and the `salt` parameter.
5. Use the public key to verify the signature of the concatenated data buffer using the [`RSASSA-PKCS1-v1_5`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc8017#section-8.2) algorithm.

If the generated and retrieved signatures match, GameKit authenticates the local player.

> ❗ **Important**:  Trust only the fields in the signed payload. Consider other data, such as nicknames, as player-provided information.

 Trust only the fields in the signed payload. Consider other data, such as nicknames, as player-provided information.

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [var authenticateHandler: ((UIViewController?, (any Error)?) -> Void)?](gklocalplayer/authenticatehandler.md)
  A handler that GameKit calls while authenticating the local player.
- [var isAuthenticated: Bool](gklocalplayer/isauthenticated.md)
  A Boolean value that indicates whether a local player has signed in to Game Center.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../foundation/nsnotification/name/1515396-gkplayerauthenticationdidchangen.md)
  A notification that posts after GameKit authenticates the local player. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/fetchitems(foridentityverificationsignature:))*