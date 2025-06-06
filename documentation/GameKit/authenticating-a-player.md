# Authenticating a player

**Framework**: GameKit

Confirm player credentials and device capabilities and check for account restrictions.

#### Overview

To identify themselves and access their game data from all their devices, players create a Game Center account that includes a profile with an avatar and nickname. A single account allows players to sign in to Game Center once and use the same credentials for all Game Center games on their device.

In the GameKit framework, you use player objects to post scores, award achievements, build leaderboards, and start multiplayer games. The  ([`GKLocalPlayer`](gklocalplayer.md)) represents the user playing your game and other  ([`GKPlayer`](gkplayer.md)) may be friends, recent matches, or global players of your and other games.

Before you access any Game Center data, you must verify that the local player signed in to Game Center on the device. Check if the player has any account restrictions and adjust your game accordingly. On Apple TV, your game can also support the ability to switch between user accounts.

##### Authenticate the Local Player

In your game, you need to authenticate the local player before you can use any GameKit APIs and Game Center services. Game Center verifies the credentials of the player and ensures their account is ready for use. Game Center also checks whether you configured your game for Game Center.

To authenticate the user, set the authentication handler ([`authenticateHandler`](gklocalplayer/authenticatehandler.md)) on the shared instance of [`GKLocalPlayer`](gklocalplayer.md) that represents the player of your game as in:

```swift
GKLocalPlayer.local.authenticateHandler = { viewController, error in
   // Handle the authorization callbacks.
}
```

GameKit calls the authentication handler, possibly several times, for the following cases:

- If the local player needs to perform some action, GameKit passes a view controller that you must present to the player to complete the authentication.
- If the player successfully signs in, GameKit sets the local player’s [`isAuthenticated`](gklocalplayer/isauthenticated.md) property to [`true`](https://developer.apple.com/documentation/swift/true) and calls the handler again, this time passing `nil` for both the view controller and error parameters. You can then start the game.
- If the player decides not to sign in or create a Game Center account, GameKit sets the local player’s [`isAuthenticated`](gklocalplayer/isauthenticated.md) property to [`false`](https://developer.apple.com/documentation/swift/false) and calls the handler again by passing an error that indicates the reason the player isn’t authenticated. In this case, disable Game Center in your game.
- If the local player previously signed in on the device when you set the authentication handler, GameKit sets the local player’s [`isAuthenticated`](gklocalplayer/isauthenticated.md) property to [`true`](https://developer.apple.com/documentation/swift/true) and passes `nil` for both the view controller and error parameters, and you can start the game.

##### Check for Restrictions

Before starting a game, check the local player’s account for restrictions and disable or hide features and content accordingly.

Check if there are any restrictions in the authentication handler when the player signs in to Game Center. In addition to checking whether the player is underage ([`isUnderage`](gklocalplayer/isunderage.md)) or not allowed to play multiplayer games ([`isMultiplayerGamingRestricted`](gklocalplayer/ismultiplayergamingrestricted.md)), check for any communication restrictions ([`isPersonalizedCommunicationRestricted`](gklocalplayer/ispersonalizedcommunicationrestricted.md)).

```swift
GKLocalPlayer.local.authenticateHandler = { viewController, error in
    if let viewController = viewController {
        // Present the view controller so the player can sign in.
        return
    }
    if error != nil {
        // Player could not be authenticated.
        // Disable Game Center in the game.
        return        
    }
    
    // Player was successfully authenticated.
    // Check if there are any player restrictions before starting the game.
            
    if GKLocalPlayer.local.isUnderage {
        // Hide explicit game content.
    }

    if GKLocalPlayer.local.isMultiplayerGamingRestricted {
        // Disable multiplayer game features.
    } 

    if GKLocalPlayer.local.isPersonalizedCommunicationRestricted {
        // Disable in game communication UI.
    }
    
    // Perform any other configurations as needed (for example, access point).
}
```

If the `isPersonalizedCommunicationRestricted` property is [`true`](https://developer.apple.com/documentation/swift/true), then the player isn’t allowed to use voice or messaging features during a multiplayer game. If your game includes any custom communication features, you should disable them. Note that if the player is underage, this property is always [`true`](https://developer.apple.com/documentation/swift/true).

##### Support User Switching

Multiple people can sign in to their accounts on a single Apple TV and you can allow players to run your game on Apple TV using their individual Game Center account. After you configure your app, add code to support user switching; otherwise, the system runs your game as the default user.

To support user switching, add the User Management capability to your app in Xcode. In the project editor, select the target, click the Signing & Capabilities tab, click the Library button (+), and then double-click the User Management capability or drag it to the Signing & Capabilities pane. Under User Management in the Signing & Capabilities pane, select Run as Current User. This entitlement grants your game access to the current user’s Game Center data.

![Screenshot of the Capabilities library showing the User Managment capability selected.](https://docs-assets.developer.apple.com/published/50ca2f7141843853063e74f6bbea9b23/media-3678701%402x.png)

When the user switches on Apple TV, the system relaunches your game. To save game data if the users switch while your game is in the foreground, implement the [`applicationWillTerminate(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationWillTerminate(_:)) method. To save data when the user switches to another app, implement the [`applicationWillResignActive(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationWillResignActive(_:)) method.

When the system relaunches your game, GameKit passes the new user to the authentication handler. For more information on user switching, see [`Personalizing Your App for Each User on Apple TV`](https://developer.apple.com/documentation/TVServices/personalizing-your-app-for-each-user-on-apple-tv).

## See Also

- [Enabling and configuring Game Center](enabling-and-configuring-game-center.md)
  Enable Game Center in your Xcode project and configure features in App Store Connect.
- [Improving the player experience for games with large downloads](improving-the-player-experience-for-games-with-large-downloads.md)
  Provide ample content in your base installation and then use on-demand resources and the Background Assets API to handle additional content.
- [Game Center Entitlement](../BundleResources/Entitlements/com.apple.developer.game-center.md)
  A Boolean value that indicates whether users of the app may see and compare achievements on a leaderboard, invite friends, and start multiplayer games.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/authenticating-a-player)*