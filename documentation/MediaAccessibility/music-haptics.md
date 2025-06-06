# Music Haptics

**Framework**: Media Accessibility

Play haptic tracks along with known music tracks.

#### Overview

Music Haptics is an accessibility feature that allows a person to indicate that they want to play haptic tracks along with known music tracks. This feature allows people who are deaf or hard of hearing to enjoy music through tactile feedback. A person can turn on this feature in Settings > Accessibility > Music Haptics. If you play music in your app, you can support haptic feedback for known songs.

##### Support Music Haptics

To support Music Haptics in your app:

- Add the [`MusicHapticsSupported`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/MusicHapticsSupported) key to your app’s `Info.plist` and set its value to `YES`.
- Check whether Music Haptics is on using [`isActive`](mamusichapticsmanager/isactive.md) on the [`shared`](mamusichapticsmanager/shared.md) instance of [`MAMusicHapticsManager`](mamusichapticsmanager.md).
- Register for the [`activeStatusDidChangeNotification`](mamusichapticsmanager/activestatusdidchangenotification.md) notification to listen for changes in the Music Haptics setting.
- Supply a known song’s International Standard Recording Code (ISRC) as part of the [`nowPlayingInfo`](https://developer.apple.com/documentation/MediaPlayer/MPNowPlayingInfoCenter/nowPlayingInfo) dictionary of [`MPNowPlayingInfoCenter`](https://developer.apple.com/documentation/MediaPlayer/MPNowPlayingInfoCenter), using the key [`MPNowPlayingInfoPropertyInternationalStandardRecordingCode`](https://developer.apple.com/documentation/MediaPlayer/MPNowPlayingInfoPropertyInternationalStandardRecordingCode). For more information about becoming the Now Playing app, refer to [`Becoming a now playable app`](https://developer.apple.com/documentation/MediaPlayer/becoming-a-now-playable-app).

##### Indicate Haptic Playback Status

To indicate the status of haptic playback for Music Haptics, you can use the following symbols:

| Symbol name | Status | API |
| --- | --- | --- |
| `"apple.haptics.and.music.note"` | Active | [`isActive`](mamusichapticsmanager/isactive.md) is `true` |
| `"apple.haptics.and.music.note.slash"` | Paused | [`isActive`](mamusichapticsmanager/isactive.md) is `false` |
| `"apple.haptics.and.exclamationmark.triangle"` | Unavailable | [`checkHapticTrackAvailabilityForMedia(matchingCode:completionHandler:)`](mamusichapticsmanager/checkhaptictrackavailabilityformedia(matchingcode:completionhandler:).md) is `false` |

For more details about using these symbols, refer to the [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/sf-symbols/) app.

## Topics

### Music Haptics
- [class MAMusicHapticsManager](mamusichapticsmanager.md)
  A class that reports information about the Music Haptics feature.

## See Also

- [Captions](captions.md)
  Coordinate the presentation of closed-captioned data for your app’s media files.
- [Flashing lights](flashing-lights.md)
  Detect, mitigate, and inform people about flashing lights in media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/music-haptics)*