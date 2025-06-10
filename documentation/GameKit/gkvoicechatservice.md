# GKVoiceChatService

**Framework**: GameKit  
**Kind**: class

The [`GKVoiceChatService`](gkvoicechatservice.md) class allows your application to connect two iOS devices into a voice chat.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class GKVoiceChatService
```

#### Overview

Before you can use voice chat, your application must configure an audio session that allows for both play and recording ([`kAudioSessionCategory_PlayAndRecord`](https://developer.apple.com/documentation/AudioToolbox/kAudioSessionCategory_PlayAndRecord)). For more information on audio sessions, see [`Audio Session Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875).

The voice chat service uses a [`client`](gkvoicechatservice/client.md) implemented by your application to find and connect to other participants. Each participant in the chat is identified by a unique  string. The client provides a participant identifier for the local user and translates other participant identifiers into connections to other users.  The format and mechanism used to translate participant identifiers into network connections is defined by the client.

Your application can configure the voice chat service to control the volume level of both local and remote participants and to detect when someone is speaking.

To use the voice chat service, your application retrieves the default service and attaches a client to it, then either connects to another participant or waits for them to start a connection.

## Topics

### Determining Whether Voice Chat Is Available
- [class func isVoIPAllowed() -> Bool](gkvoicechatservice/isvoipallowed.md)
  Returns whether voice chat is allowed to be used on the device.
### Getting the Shared Voice Chat Service
- [class func `default`() -> GKVoiceChatService!](gkvoicechatservice/default.md)
  Retrieves the singleton chat service.
### Setting the Client
- [var client: (any GKVoiceChatClient)!](gkvoicechatservice/client.md)
  An object that the voice chat service uses to communicate with remote participants.
### Establishing a Voice Chat
- [func startVoiceChat(withParticipantID: String!) throws](gkvoicechatservice/startvoicechat(withparticipantid:).md)
  Sends a request to another participant to join the voice chat.
### Adjusting Audio Properties
- [var isMicrophoneMuted: Bool](gkvoicechatservice/ismicrophonemuted.md)
  A Boolean value that determines whether the user’s microphone is muted.
- [var remoteParticipantVolume: Float](gkvoicechatservice/remoteparticipantvolume.md)
  A float that scales the volume of all remote participants.
### Monitoring the Audio Level
- [var isInputMeteringEnabled: Bool](gkvoicechatservice/isinputmeteringenabled.md)
  A Boolean value that indicates whether the microphone’s sound level is being monitored.
- [var inputMeterLevel: Float](gkvoicechatservice/inputmeterlevel.md)
  The volume, in decibels (db), being received by the microphone.
- [var isOutputMeteringEnabled: Bool](gkvoicechatservice/isoutputmeteringenabled.md)
  A Boolean value that indicates whether the voice level of remote participants is monitored.
- [var outputMeterLevel: Float](gkvoicechatservice/outputmeterlevel.md)
  The volume, in decibels (db), being received from all other participants.
### Ending a Voice Chat
- [func stopVoiceChat(withParticipantID: String!)](gkvoicechatservice/stopvoicechat(withparticipantid:).md)
  Ends a previously established voice chat.
### Methods Called by the Client
- [func acceptCallID(Int) throws](gkvoicechatservice/acceptcallid(_:).md)
  Accepts a request from a remote user to establish a voice chat.
- [func denyCallID(Int)](gkvoicechatservice/denycallid(_:).md)
  Rejects a request to establish a voice chat.
- [func receivedData(Data!, fromParticipantID: String!)](gkvoicechatservice/receiveddata(_:fromparticipantid:).md)
  Called by the client to deliver new data received from a remote participant.
- [func receivedRealTime(Data!, fromParticipantID: String!)](gkvoicechatservice/receivedrealtime(_:fromparticipantid:).md)
  Called by the client to deliver voice data received from a remote participant..
### Constants
- [Voice Chat Service Error Domain](voice-chat-service-error-domain.md)
  The [`GKVoiceChatService`](gkvoicechatservice.md) error domain.
- [GKVoiceChatServiceError.Code](gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](gkvoicechatserviceerror-swift.struct.md)

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
- [class GKChallenge](gkchallenge.md)
  A challenge issued by the local player to another player.
- [class GKScoreChallenge](gkscorechallenge.md)
  A type of challenge where a player must beat the leaderboard score of another player.
- [class GKAchievementChallenge](gkachievementchallenge.md)
  A type of challenge where a player must earn another player’s achievement.
- [class GKCloudPlayer](gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameCenterViewController](gkgamecenterviewcontroller.md)
  The dashboard that allows players to access their Game Center data in your game.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice)*