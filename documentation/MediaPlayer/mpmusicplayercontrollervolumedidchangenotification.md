# MPMusicPlayerControllerVolumeDidChangeNotification

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

Posted when the audio playback volume for the music player has changed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```c
extern NSNotificationName const MPMusicPlayerControllerVolumeDidChangeNotification;
```

## Discussion

The object associated with the notification is the music player whose playback volume changed. The notification has no `userInfo` dictionary.

## See Also

### Using music player notifications
- [func beginGeneratingPlaybackNotifications()](./mpmusicplayercontroller/begingeneratingplaybacknotifications%28%29.md)
  Starts the generation of playback notifications.
- [func endGeneratingPlaybackNotifications()](./mpmusicplayercontroller/endgeneratingplaybacknotifications%28%29.md)
  Ends the generation of playback notifications.
- [MPMusicPlayerControllerPlaybackStateDidChangeNotification](./mpmusicplayercontrollerplaybackstatedidchangenotification.md)
  Posted when the playback state changes programmatically or by user action.
- [MPMusicPlayerControllerNowPlayingItemDidChangeNotification](./mpmusicplayercontrollernowplayingitemdidchangenotification.md)
  Posted when the currently playing media item has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollervolumedidchangenotification)*