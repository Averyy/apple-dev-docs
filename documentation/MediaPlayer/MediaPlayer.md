# Media Player

**Framework**: Media Player  
**Kind**: module

Find and play songs, audio podcasts, audio books, and more from within your app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.12.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

#### Overview

Use the Media Player framework, which is part of [`MusicKit`](https://developer.apple.comhttps://developer.apple.com/musickit/), to control playback of the user’s media from your app. If your app incorporates music, you can use this framework to search for audio content, such as songs, podcasts, and books, in the user’s library. You can then play that content directly or ask the system Music app to play it. For example, a game might give users the option to play their own music while completing a particular game level.

> ❗ **Important**:  To protect user privacy, users need to grant permission for your app to access their media library. Add the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key to your app’s `Info.plist` file, and include a description of how you intend to use the user’s library. If this key isn’t present, the system terminates your app when it tries to access the user’s library.

To play content from the user’s library using the Media Player framework, use one of the built-in [`MPMusicPlayerController`](mpmusicplayercontroller.md) objects:

- An  plays music locally within your app. Use this player when you want greater control over the audio you play for the user. This player doesn’t change the state of the built-in Music app.
- The  employs the Music app to play audio on your behalf. Use this player when you want audio to continue playing even when the user switches away from your app.

Use media queries to retrieve the items you want to play and to populate the queue for the media player you select. After a user gives your app permission to access their Apple Music account, it can add songs, create playlists, and play songs from Apple Music. If your app detects that the user isn’t an Apple Music subscriber, it can offer a trial.

You can’t play video media items directly using the Media Player framework. To play videos containing [`MPMediaItem`](mpmediaitem.md) objects, use an [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object from [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation). The system player also provides a way to play video items using the system apps.

> ❗ **Important**:  Only use this framework to facilitate playback of the user’s audio content within your app. Don’t gather information about the user’s audio content for any other purpose. For more information about accessing Apple Music content, see the [`App Store review guidelines`](https://developer.apple.comhttps://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services).

## Topics

### Essentials
- [NSAppleMusicUsageDescription](../BundleResources/Information-Property-List/NSAppleMusicUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s media library.
### Built-in music playback
- [Playing audio using the built-in music player](playing-audio-using-the-built-in-music-player.md)
  Create a media player inside your app to play audio from the user’s media library.
- [class MPMusicPlayerController](mpmusicplayercontroller.md)
  An object that plays audio media items from the device’s Music app library.
- [protocol MPMediaPlayback](mpmediaplayback.md)
  A protocol that defines the interface for controlling audio media playback.
- [protocol MPSystemMusicPlayerController](mpsystemmusicplayercontroller.md)
  A protocol for playing videos in the Music app.
### Media library synchronization
- [class MPMediaLibrary](mpmedialibrary.md)
  An object that represents the state of synced media items on a device.
### Media item queries
- [Using filters to create specialized queries](using-filters-to-create-specialized-queries.md)
  Add a filter set to a query before populating a music player queue.
- [class MPMediaQuery](mpmediaquery.md)
  A query that specifies a set of media items from the device’s media library using a filter and a grouping type.
- [class MPMediaQuerySection](mpmediaquerysection.md)
  A range of media items or media item collections from within a media query.
- [class MPMediaPropertyPredicate](mpmediapropertypredicate.md)
  A set of predicates for defining a filter in a media query.
- [class MPMediaPredicate](mpmediapredicate.md)
  An abstract class that defines classes for filtering media in a media query.
### Media player queues
- [class MPMusicPlayerControllerQueue](mpmusicplayercontrollerqueue.md)
  An immutable queue containing the media items to play.
- [class MPMusicPlayerControllerMutableQueue](mpmusicplayercontrollermutablequeue.md)
  A mutable queue containing the media items to play.
- [class MPMusicPlayerApplicationController](mpmusicplayerapplicationcontroller.md)
  A media player object that you use to revise the queue that’s currently playing.
- [class MPMusicPlayerMediaItemQueueDescriptor](mpmusicplayermediaitemqueuedescriptor.md)
  A set of properties and methods for modifying audio media items in the player’s media queue.
- [class MPMusicPlayerStoreQueueDescriptor](mpmusicplayerstorequeuedescriptor.md)
  A set of properties and methods for modifying items, based on their store identifier, in the player’s queue.
- [class MPMusicPlayerPlayParametersQueueDescriptor](mpmusicplayerplayparametersqueuedescriptor.md)
  A set of properties and methods for modifying how to play items, based on play parameters the framework returns.
- [class MPMusicPlayerQueueDescriptor](mpmusicplayerqueuedescriptor.md)
  The abstract base class for audio media item and store queue descriptors.
### Media items and playlists
- [class MPMediaItem](mpmediaitem.md)
  A collection of properties that represents a single item in the media library.
- [class MPMediaItemArtwork](mpmediaitemartwork.md)
  A graphical image, such as music album cover art, associated with a media item.
- [class MPMediaItemAnimatedArtwork](mpmediaitemanimatedartwork.md)
  An animated image, such as an animated music album cover art, for a media item.
- [class MPMediaItemCollection](mpmediaitemcollection.md)
  A sorted set of media items from the media library.
- [class MPMediaPlaylist](mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaPlaylistCreationMetadata](mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.
- [class MPMediaEntity](mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.
### Media player user interface
- [Displaying a media picker from your app](displaying-a-media-picker-from-your-app.md)
  Let users choose the music they want to play by displaying a media picker interface from within your app.
- [class MPMediaPickerController](mpmediapickercontroller.md)
  A specialized view controller that provides a graphical interface for selecting media items.
- [class MPVolumeView](mpvolumeview.md)
  A slider control for setting the system audio output volume, and a button for choosing the audio output route.
### Now Playing information
- [Becoming a now playable app](becoming-a-now-playable-app.md)
  Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- [class MPNowPlayingSession](mpnowplayingsession.md)
  An object that manages Now Playing information and remote commands for multiple players.
- [class MPNowPlayingInfoCenter](mpnowplayinginfocenter.md)
  An object for setting the Now Playing information for media that your app plays.
- [class MPNowPlayingInfoLanguageOption](mpnowplayinginfolanguageoption.md)
  A set of interfaces for setting the language option for the Now Playing item.
- [class MPNowPlayingInfoLanguageOptionGroup](mpnowplayinginfolanguageoptiongroup.md)
  A grouped set of language options where only a single language option can be active at a time.
- [Language option characteristic constants](language-option-characteristic-constants.md)
  The constants for defining language characteristics.
### External player and system event handling
- [Handling external player events notifications](handling-external-player-events-notifications.md)
  Handle events for external media players.
- [Remote command center events](remote-command-center-events.md)
  Set up the remote command center to handle media player events.
- [Track navigation events](track-navigation-events.md)
  Respond to requests to change which part of a media item plays.
- [Media playback mode events](media-playback-mode-events.md)
  Respond to changes in the way media items play.
- [Feedback and rating events](feedback-and-rating-events.md)
  Respond to incoming feedback and rating events.
### External media player items
- [class MPContentItem](mpcontentitem.md)
  An object that contains the information for a displayed media item.
### Media player errors
- [struct MPError](mperror.md)
  A structure that represents a framework error.
- [MPError.Code](mperror/code.md)
  An enumeration that represents error codes for framework operations.
- [let MPErrorDomain: String](mperrordomain.md)
  The Media Player framework error domain.
### Deprecated
- [Deprecated types](deprecated-types.md)
  Review deprecated symbols and avoid using them in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaPlayer)*