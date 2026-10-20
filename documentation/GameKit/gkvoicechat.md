# GKVoiceChat

**Framework**: GameKit  
**Kind**: class  
**Role**: Class

A voice channel that allows players to speak with each other in a multiplayer game.

**Availability**:
- iOS 4.1+ - Deprecated in 18.0
- iPadOS 4.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use SharePlay instead. See [Enable the local player to choose other players](./finding-multiple-players-for-a-game.md#Enable-the-local-player-to-choose-other-players) and [`startGroupActivity(playerHandler:)`](./gkmatchmaker/startgroupactivity%28playerhandler%29.md).

## Declaration

```swift
class GKVoiceChat
```

```objc
@interface GKVoiceChat : NSObject
```

## Mentions

- [Adding voice chat to multiplayer games](./adding-voice-chat-to-multiplayer-games.md)

#### Overview

GameKit provides the underlying mechanism to implement voice chat between players in a multiplayer game. It’s your responsibility to provide player controls and display feedback during the chat.

First, configure voice chat by adding the [`NSMicrophoneUsageDescription`](../BundleResources/information-property-list/nsmicrophoneusagedescription.md) key to the Information Property List and creating an audio session. Then, create a `GKVoiceChat` object using the `GKMatch` [`voiceChat(withName:)`](./gkmatch/voicechat%28withname%29.md) method passing a string that identifies the voice channel. Use the [`start()`](./gkvoicechat/start%28%29.md) method to connect players to the channel. Use the [`isActive`](./gkvoicechat/isactive.md) property to activate the microphone or switch the microphone between channels.

Provide a handler using the [`playerVoiceChatStateDidChangeHandler`](./gkvoicechat/playervoicechatstatedidchangehandler.md) property to update the interface when a player connects, speaks, or disconnects from a chat. You can also add controls that mute and set the volume using the [`setPlayer(_:muted:)`](./gkvoicechat/setplayer%28_,muted%29.md) method and [`volume`](./gkvoicechat/volume.md) property.

Note that if there’s insufficient bandwidth over Wi-Fi to maintain a voice chat, GameKit may disconnect players from the channel or disband a channel.

## Topics

### Determining Whether Voice Chat Is Available
- [class func isVoIPAllowed() -> Bool](./gkvoicechat/isvoipallowed%28%29.md)
  Returns whether voice chat is available on the device.
### Starting and Stopping Voice Chat
- [func start()](./gkvoicechat/start%28%29.md)
  Starts communication with other players in a channel.
- [func stop()](./gkvoicechat/stop%28%29.md)
  Ends communication with other players in a channel.
- [var isActive: Bool](./gkvoicechat/isactive.md)
  A Boolean value that indicates whether the channel is sampling the microphone.
### Receiving Updates About Other Participants
- [var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChat.PlayerState) -> Void](./gkvoicechat/playervoicechatstatedidchangehandler.md)
  A method that handles when a player’s voice chat changes state.
- [GKVoiceChat.PlayerState](./gkvoicechat/playerstate.md)
  The state of a player in a voice chat.
### Controlling Chat Volume
- [func setPlayer(GKPlayer, muted: Bool)](./gkvoicechat/setplayer%28_,muted%29.md)
  Mutes a player in the chat, including the local player.
- [var volume: Float](./gkvoicechat/volume.md)
  The volume level for the channel.
### Accessing Properties
- [var name: String](./gkvoicechat/name.md)
  The name of the voice chat channel.
- [var players: [GKPlayer]](./gkvoicechat/players.md)
  The players connected to the channel.
### Deprecated Methods and Properties
- [var playerIDs: [String]?](./gkvoicechat/playerids.md)
  An array of strings containing the player identifiers for the players connected to the channel.
- [var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void](./gkvoicechat/playerstateupdatehandler.md)
  Handles when a player in the chat changes state.
- [func setMute(Bool, forPlayer: String)](./gkvoicechat/setmute%28_,forplayer%29.md)
  Mutes a player in a voice chat.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated classes
- [class GKAchievementViewController](./gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](./gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengeEventHandler](./gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](./gkchallengesviewcontroller.md)
- [class GKChallenge](./gkchallenge.md)
  A challenge issued by the local player to another player.
- [class GKScoreChallenge](./gkscorechallenge.md)
  A type of challenge where a player must beat the leaderboard score of another player.
- [class GKAchievementChallenge](./gkachievementchallenge.md)
  A type of challenge where a player must earn another player’s achievement.
- [class GKCloudPlayer](./gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameCenterViewController](./gkgamecenterviewcontroller.md)
  The dashboard that allows players to access their Game Center data in your game.
- [class GKGameSession](./gkgamesession.md)
  A game session you can use to save game data, invite other players, and create turn-based and real-time game apps.
- [class GKGameSessionSharingViewController](./gkgamesessionsharingviewcontroller.md)
  A user interface you can use to invite other users into a tvOS game session.
- [class GKFriendRequestComposeViewController](./gkfriendrequestcomposeviewcontroller.md)
  Your game uses the `GKFriendRequestComposeViewController` class to present a screen that allows the local player to send friend requests to other players.
- [class GKLeaderboardViewController](./gkleaderboardviewcontroller.md)
  The `GKLeaderboardViewController` class provides a standard user interface that displays leaderboard scores to the player. If the [`GKGameCenterViewController`](./gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKPeerPickerController](./gkpeerpickercontroller.md)
  Provides a standard user interface to allow one iOS device to discover and connect to another.
- [class GKScore](./gkscore.md)
  An object containing information for a score that was earned by the player.
- [class GKSession](./gksession.md)
  A [`GKSession`](./gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat)*