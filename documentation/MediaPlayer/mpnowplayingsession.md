# MPNowPlayingSession

**Framework**: Media Player  
**Kind**: class

An object that manages Now Playing information and remote commands for multiple players.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPNowPlayingSession
```

#### Overview

An [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object can have only one Now Playing session. An [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) manages its own player and Now Playing session, so you can’t add your own Now Playing session.

> ❗ **Important**:  If you create an `MPNowPlayingSession` object, don’t attempt to use it with the `AVPlayer` that an `AVPlayerViewController` presents. Create your own `AVPlayer` instance with custom playback controls to use with your Now Playing session.

## Topics

### Creating a session
- [init(players: [AVPlayer])](mpnowplayingsession/init(players:).md)
  Creates a Now Playing session object.
### Accessing the delegate object
- [var delegate: (any MPNowPlayingSessionDelegate)?](mpnowplayingsession/delegate.md)
  The Now Playing session’s delegate object.
- [protocol MPNowPlayingSessionDelegate](mpnowplayingsessiondelegate.md)
  A protocol that defines the delegate interface for a Now Playing session.
### Managing players
- [var players: [AVPlayer]](mpnowplayingsession/players.md)
  The array of players associated with the session.
- [func addPlayer(AVPlayer)](mpnowplayingsession/addplayer(_:).md)
  Adds a player to the session.
- [func removePlayer(AVPlayer)](mpnowplayingsession/removeplayer(_:).md)
  Removes a player from the session.
### Managing the active state
- [var isActive: Bool](mpnowplayingsession/isactive.md)
  A Boolean value that indicates whether the session is the app’s active Now Playing session.
- [var canBecomeActive: Bool](mpnowplayingsession/canbecomeactive.md)
  A Boolean value that indicates whether the session can become the app’s active Now Playing session.
- [func becomeActiveIfPossible(completion: ((Bool) -> Void)?)](mpnowplayingsession/becomeactiveifpossible(completion:).md)
  Tells the system to make the session the active Now Playing session if possible.
### Configuring Now Playing information
- [var automaticallyPublishesNowPlayingInfo: Bool](mpnowplayingsession/automaticallypublishesnowplayinginfo.md)
  A Boolean that indicates whether Now Playing info automatically publishes.
- [var nowPlayingInfoCenter: MPNowPlayingInfoCenter](mpnowplayingsession/nowplayinginfocenter.md)
  The Now Playing information center associated with the session.
### Handling remote commands
- [var remoteCommandCenter: MPRemoteCommandCenter](mpnowplayingsession/remotecommandcenter.md)
  The remote command center associated with the session.

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

- [Becoming a now playable app](becoming-a-now-playable-app.md)
  Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- [class MPNowPlayingInfoCenter](mpnowplayinginfocenter.md)
  An object for setting the Now Playing information for media that your app plays.
- [class MPNowPlayingInfoLanguageOption](mpnowplayinginfolanguageoption.md)
  A set of interfaces for setting the language option for the Now Playing item.
- [class MPNowPlayingInfoLanguageOptionGroup](mpnowplayinginfolanguageoptiongroup.md)
  A grouped set of language options where only a single language option can be active at a time.
- [Language option characteristic constants](language-option-characteristic-constants.md)
  The constants for defining language characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession)*