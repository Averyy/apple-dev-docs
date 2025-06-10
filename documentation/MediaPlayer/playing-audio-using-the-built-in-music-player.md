# Playing audio using the built-in music player

**Framework**: Media Player

Create a media player inside your app to play audio from the user’s media library.

#### Overview

There are many reasons you might want to let users play music from their music library inside your app. For example, you might want them to listen to their own music while playing a particular level in your game. Add a built-in music player to quickly play audio tracks from the user’s music library while your app is running.

> **Note**:  To follow these steps, you must have a provisioned iOS device. Simulator has no access to a device’s music library.

##### Specify a Usage Description String

To give the user control over their personal data, apps must obtain permission to access the person’s music library. The first time your app tries to access someone’s media library, the system displays an alert that prompts them to grant or deny access to their music. The alert message includes your app’s usage-description string, which is a text description of how you plan to use the music.

To specify the usage-description string for your app, add the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key to your app’s `Info.plist` file. Set the value of the key to your description of how you intend to use the music. Make your description as concise as possible, and no more than one or two sentences. For example, the usage-description string for a game might explain that its soundtrack incorporates the person’s music at different points in the gameplay.

> ❗ **Important**:  If your app’s `Info.plist` file doesn’t include the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key, the system forces your app to exit when it attempts to access the current music library. To fix the problem, add the key to your `Info.plist` file, and set the key’s value to an appropriate description.

Users can deny access to their media library, so design your app to run even without that access. If your app requires music, devise a backup plan that doesn’t involve asking the person to reconsider their decision. For example, include some default music in your app’s bundle.

##### Configure the Media Player Contents

To play the user’s music, your app needs an [`MPMusicPlayerController`](mpmusicplayercontroller.md) object. The Media Player framework defines several player controllers, each of which serves a different purpose. To manage a queue of songs that’s specific to your app, create an application queue player, and fill it with one or more songs.

To access the songs in the user’s music library, construct an [`MPMediaQuery`](mpmediaquery.md) object for the items you want. The class has constructors that let you request the user’s playlists, podcasts, songs, and other media content. To get the current songs, use the [`songs()`](mpmediaquery/songs().md) constructor, as shown in the following example.

```swift
// Get the music player.
let musicPlayer = MPMusicPlayerApplicationController.applicationQueuePlayer
// Add a playback queue containing all songs on the device.
musicPlayer.setQueue(with: .songs())
```

If you don’t want all the items in a collection, filter the list by adding one or more predicates to your [`MPMediaQuery`](mpmediaquery.md). For example, you might specify a predicate to match only songs with a specific word in the title. For more information about configuring media queries, see [`MPMediaQuery`](mpmediaquery.md).

##### Play and Pause the Music

After you add one or more songs to your music player, begin playback by calling the [`play()`](mpmediaplayback/play().md) method. Media players adopt the [`MPMediaPlayback`](mpmediaplayback.md) protocol and support all of the normal methods to play, pause, and stop playback. You can also use the methods of that protocol to change the playback speed and seek within a media item.

For more information about controlling the playback of your items, see [`MPMediaPlayback`](mpmediaplayback.md).

## See Also

- [Displaying a media picker from your app](displaying-a-media-picker-from-your-app.md)
  Let users choose the music they want to play by displaying a media picker interface from within your app.
- [class MPMusicPlayerController](mpmusicplayercontroller.md)
  An object that plays audio media items from the device’s Music app library.
- [protocol MPMediaPlayback](mpmediaplayback.md)
  A protocol that defines the interface for controlling audio media playback.
- [protocol MPSystemMusicPlayerController](mpsystemmusicplayercontroller.md)
  A protocol for playing videos in the Music app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/playing-audio-using-the-built-in-music-player)*