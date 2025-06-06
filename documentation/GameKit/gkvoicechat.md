# GKVoiceChat

**Framework**: GameKit  
**Kind**: class

A voice channel that allows players to speak with each other in a multiplayer game.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKVoiceChat
```

## Mentions

- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)

#### Overview

GameKit provides the underlying mechanism to implement voice chat between players in a multiplayer game. It’s your responsibility to provide player controls and display feedback during the chat.

First, configure voice chat by adding the [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) key to the Information Property List and creating an audio session. Then, create a `GKVoiceChat` object using the `GKMatch` [`voiceChat(withName:)`](gkmatch/voicechat(withname:).md) method passing a string that identifies the voice channel. Use the [`start()`](gkvoicechat/start().md) method to connect players to the channel. Use the [`isActive`](gkvoicechat/isactive.md) property to activate the microphone or switch the microphone between channels.

Provide a handler using the [`playerVoiceChatStateDidChangeHandler`](gkvoicechat/playervoicechatstatedidchangehandler.md) property to update the interface when a player connects, speaks, or disconnects from a chat. You can also add controls that mute and set the volume using the [`setPlayer(_:muted:)`](gkvoicechat/setplayer(_:muted:).md) method and [`volume`](gkvoicechat/volume.md) property.

Note that if there’s insufficient bandwidth over Wi-Fi to maintain a voice chat, GameKit may disconnect players from the channel or disband a channel.

## Topics

### Determining Whether Voice Chat Is Available
- [class func isVoIPAllowed() -> Bool](gkvoicechat/isvoipallowed.md)
  Returns whether voice chat is available on the device.
### Starting and Stopping Voice Chat
- [func start()](gkvoicechat/start.md)
  Starts communication with other players in a channel.
- [func stop()](gkvoicechat/stop.md)
  Ends communication with other players in a channel.
- [var isActive: Bool](gkvoicechat/isactive.md)
  A Boolean value that indicates whether the channel is sampling the microphone.
### Receiving Updates About Other Participants
- [var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChat.PlayerState) -> Void](gkvoicechat/playervoicechatstatedidchangehandler.md)
  A method that handles when a player’s voice chat changes state.
- [GKVoiceChat.PlayerState](gkvoicechat/playerstate.md)
  The state of a player in a voice chat.
### Controlling Chat Volume
- [func setPlayer(GKPlayer, muted: Bool)](gkvoicechat/setplayer(_:muted:).md)
  Mutes a player in the chat, including the local player.
- [var volume: Float](gkvoicechat/volume.md)
  The volume level for the channel.
### Accessing Properties
- [var name: String](gkvoicechat/name.md)
  The name of the voice chat channel.
- [var players: [GKPlayer]](gkvoicechat/players.md)
  The players connected to the channel.
### Deprecated Methods and Properties
- [var playerIDs: [String]?](gkvoicechat/playerids.md)
  An array of strings containing the player identifiers for the players connected to the channel.
- [var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void](gkvoicechat/playerstateupdatehandler.md)
  Handles when a player in the chat changes state.
- [func setMute(Bool, forPlayer: String)](gkvoicechat/setmute(_:forplayer:).md)
  Mutes a player in a voice chat.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKAchievementViewController](gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengeEventHandler](gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](gkchallengesviewcontroller.md)
- [class GKCloudPlayer](gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameSession](gkgamesession.md)
  A game session you can use to save game data, invite other players, and create turn-based and real-time game apps.
- [class GKGameSessionSharingViewController](gkgamesessionsharingviewcontroller.md)
  A user interface you can use to invite other users into a tvOS game session.
- [class GKFriendRequestComposeViewController](gkfriendrequestcomposeviewcontroller.md)
  Your game uses the `GKFriendRequestComposeViewController` class to present a screen that allows the local player to send friend requests to other players.
- [class GKLeaderboardViewController](gkleaderboardviewcontroller.md)
  The `GKLeaderboardViewController` class provides a standard user interface that displays leaderboard scores to the player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKPeerPickerController](gkpeerpickercontroller.md)
  Provides a standard user interface to allow one iOS device to discover and connect to another.
- [class GKScore](gkscore.md)
  An object containing information for a score that was earned by the player.
- [class GKSession](gksession.md)
  A [`GKSession`](gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.
- [class GKTurnBasedEventHandler](gkturnbasedeventhandler.md)
  The [`GKTurnBasedEventHandler`](gkturnbasedeventhandler.md) class is used to respond to important messages related to turn-based matches. To use it, call the [`shared()`](gkturnbasedeventhandler/shared().md) class method to get the singleton instance and assign an object that implements the [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol to its [`delegate`](gkturnbasedeventhandler/delegate.md) property. All methods are called on the main thread.
- [class GKVoiceChatService](gkvoicechatservice.md)
  The [`GKVoiceChatService`](gkvoicechatservice.md) class allows your application to connect two iOS devices into a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat)*