# MPMusicPlayerController

**Framework**: Media Player  
**Kind**: class

An object that plays audio media items from the device’s Music app library.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMusicPlayerController
```

## Mentions

- [Playing audio using the built-in music player](playing-audio-using-the-built-in-music-player.md)

#### Overview

Create an instance of a music player to play media items in your app. There are two types of music players:

- An  plays music locally within your app. It isn’t aware of the Music app’s Now Playing item, nor does it affect the Music app’s state. There are two application music players: [`applicationMusicPlayer`](mpmusicplayercontroller/applicationmusicplayer.md) and [`applicationQueuePlayer`](mpmusicplayercontroller/applicationqueueplayer.md). The application queue player provides greater control over the contents of the queue and is the preferred player.
- The  employs the built-in Music app on your behalf. On instantiation, it takes on the current Music app state, such as the identification of the Now Playing item. If a user switches away from your app while music is playing, that music continues to play. The Music app then has your music player’s most recently-set repeat mode, shuffle mode, playback state, and Now Playing item.

Creating a new instance of `MPMusicPlayerController` and not specifying the player type returns a system music player.

> ❗ **Important**:  Only use a music player on the app’s main thread.

 Only use a music player on the app’s main thread.

##### Accessing Limited Playback Information While Using Home Sharing

The built-in Music and Videos apps can play media from shared libraries using Home Sharing. However, third-party apps using the Media Player framework only have access to the device music library. This means that your app can’t display the title of a home-shared song in your user interface. Specifically, if the Music app is playing a home-shared song, and you’re using a system music player, the value of the [`nowPlayingItem`](mpmusicplayercontroller/nowplayingitem.md) property of your music player is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0). However, other playback information is available when playing shared media. For example, the framework updates the value of the [`playbackState`](mpmusicplayercontroller/playbackstate.md) property when the system music player plays a home-shared item.

##### Choosing How the System Handles Remote Control Events

Users can initiate audio playback commands through an external headset or accessory.

- If you use an , the system sends these commands as remote control events to your app, but you don’t provide code to handle them. The framework receives and handles the remote control events.
- If you use the , your app uses the Music app to play audio, which means that the Music app is the Now Playing app. The Music app receives and handles the remote control events. For example, if your app plays audio using the system music player, and the user switches from your app to the iOS device’s Now Playing controls, the controls work as expected. That is, they can play or pause audio, or skip to the next and previous items.

## Topics

### Getting a music player
- [class var applicationMusicPlayer: MPMusicPlayerController](mpmusicplayercontroller/applicationmusicplayer.md)
  Returns the application music player.
- [class var applicationQueuePlayer: MPMusicPlayerApplicationController](mpmusicplayercontroller/applicationqueueplayer.md)
  Returns the application queue music player.
- [class var systemMusicPlayer: any MPMusicPlayerController & MPSystemMusicPlayerController](mpmusicplayercontroller/systemmusicplayer.md)
  Returns the system music player, which controls the Music app’s state.
### Setting up a playback queue
- [func setQueue(with: MPMediaQuery)](mpmusicplayercontroller/setqueue(with:)-5rii3.md)
  Sets a music player’s playback queue based on a media query.
- [func setQueue(with: MPMediaItemCollection)](mpmusicplayercontroller/setqueue(with:)-xlwk.md)
  Sets a music player’s playback queue using a media item collection.
- [func setQueue(with: [String])](mpmusicplayercontroller/setqueue(with:)-8x6xb.md)
  Sets a music player’s playback queue using with media items identified by the store identifiers.
- [func setQueue(with: MPMusicPlayerQueueDescriptor)](mpmusicplayercontroller/setqueue(with:)-1izmj.md)
  Set the music player’s playback queue using media items that fit the queue descriptor properties.
### Playing a media item
- [func prepareToPlay(completionHandler: ((any Error)?) -> Void)](mpmusicplayercontroller/preparetoplay(completionhandler:).md)
  Prepares a music player for playback.
### Managing playback mode and state
- [var nowPlayingItem: MPMediaItem?](mpmusicplayercontroller/nowplayingitem.md)
  The currently-playing media item, or the media item in a queue that you designated to begin playback with.
- [var indexOfNowPlayingItem: Int](mpmusicplayercontroller/indexofnowplayingitem.md)
  The index of the now playing item in the current playback queue.
- [var playbackState: MPMusicPlaybackState](mpmusicplayercontroller/playbackstate.md)
  The current playback state of the music player.
- [var repeatMode: MPMusicRepeatMode](mpmusicplayercontroller/repeatmode.md)
  The current repeat mode of the music player.
- [var shuffleMode: MPMusicShuffleMode](mpmusicplayercontroller/shufflemode.md)
  The current shuffle mode of the music player.
- [enum MPMusicPlaybackState](mpmusicplaybackstate.md)
  The music player playback state modes.
- [enum MPMusicRepeatMode](mpmusicrepeatmode.md)
  The repeat modes for the media player.
- [enum MPMusicShuffleMode](mpmusicshufflemode.md)
  The shuffle modes for the media player.
- [var volume: Float](mpmusicplayercontroller/volume.md)
  The audio playback volume for the music player, in the range from `0.0` (silent) through `1.0` (maximum volume).
### Controlling playback
- [func skipToNextItem()](mpmusicplayercontroller/skiptonextitem.md)
  Starts playback of the next media item in the playback queue, or if the music player isn’t playing, designates the next media item as the next item to play.
- [func skipToBeginning()](mpmusicplayercontroller/skiptobeginning.md)
  Restarts playback at the beginning of the currently playing media item.
- [func skipToPreviousItem()](mpmusicplayercontroller/skiptopreviousitem.md)
  Starts playback of the previous media item in the playback queue, or if the music player isn’t playing, designates the previous media item as the next to play.
- [func append(MPMusicPlayerQueueDescriptor)](mpmusicplayercontroller/append(_:).md)
  Inserts the media items defined by the queue descriptor after the last media item in the current queue.
- [func prepend(MPMusicPlayerQueueDescriptor)](mpmusicplayercontroller/prepend(_:).md)
  Inserts the media items defined by the queue descriptor into the current queue immediately after the currently playing media item.
### Using music player notifications
- [func beginGeneratingPlaybackNotifications()](mpmusicplayercontroller/begingeneratingplaybacknotifications.md)
  Starts the generation of playback notifications.
- [func endGeneratingPlaybackNotifications()](mpmusicplayercontroller/endgeneratingplaybacknotifications.md)
  Ends the generation of playback notifications.
### Type Properties
- [class var iPodMusicPlayer: MPMusicPlayerController](mpmusicplayercontroller/ipodmusicplayer.md)
  Returns the iPod music player, which controls the iPod app’s state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPMusicPlayerApplicationController](mpmusicplayerapplicationcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MPMediaPlayback](mpmediaplayback.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Playing audio using the built-in music player](playing-audio-using-the-built-in-music-player.md)
  Create a media player inside your app to play audio from the user’s media library.
- [protocol MPMediaPlayback](mpmediaplayback.md)
  A protocol that defines the interface for controlling audio media playback.
- [protocol MPSystemMusicPlayerController](mpsystemmusicplayercontroller.md)
  A protocol for playing videos in the Music app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller)*