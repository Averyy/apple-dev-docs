# AVPlayer

**Framework**: AVFoundation  
**Kind**: class

An object that provides the interface to control the player’s transport behavior.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
@MainActor
class AVPlayer
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
- [Supporting AirPlay in your app](supporting-airplay-in-your-app.md)
- [Presenting Chapter Markers](presenting-chapter-markers.md)
- [Implementing simple enhanced buffering for your content](implementing-simple-enhanced-buffering-for-your-content.md)
- [Monitoring playback progress in your app](monitoring-playback-progress-in-your-app.md)
- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)

#### Overview

A player is a controller object that manages the playback and timing of a media asset. Use an instance of [`AVPlayer`](avplayer.md) to play local and remote file-based media, such as QuickTime movies and MP3 audio files, as well as audiovisual media served using HTTP Live Streaming.

Use a player object to play a single media asset. You can reuse the player instance to play additional media assets using its [`replaceCurrentItem(with:)`](avplayer/replacecurrentitem(with:).md) method, but it manages the playback of only a single media asset at a time. The framework also provides a subclass called [`AVQueuePlayer`](avqueueplayer.md) that you can use to manage the playback of a queue of media assets.

You use an [`AVPlayer`](avplayer.md) to play media assets, which AVFoundation represents using the [`AVAsset`](avasset.md) class. [`AVAsset`](avasset.md) only models the  aspects of the media, such as its duration or creation date, and on its own, isn’t suitable for playback with an [`AVPlayer`](avplayer.md). To play an asset, you create an instance of its  counterpart found in [`AVPlayerItem`](avplayeritem.md). This object models the timing and presentation state of an asset played by an instance of [`AVPlayer`](avplayer.md). See the [`AVPlayerItem`](avplayeritem.md) reference for more details.

[`AVPlayer`](avplayer.md) is a dynamic object whose state continuously changes. There are two approaches you can use to observe a player’s state:

-  You can use key-value observing (KVO) to observe state changes to many of the player’s dynamic properties, such as its [`currentItem`](avplayer/currentitem.md) or its playback [`rate`](avplayer/rate.md).
-  KVO works well for general state observations, but isn’t intended for observing continuously changing state like the player’s time. [`AVPlayer`](avplayer.md) provides two methods to observe time changes:
- [`addPeriodicTimeObserver(forInterval:queue:using:)`](avplayer/addperiodictimeobserver(forinterval:queue:using:).md)
- [`addBoundaryTimeObserver(forTimes:queue:using:)`](avplayer/addboundarytimeobserver(fortimes:queue:using:).md)

These methods let you observe time changes either periodically or by boundary, respectively. As changes occur, invoke the callback block or closure you supply to these methods to give you the opportunity to take some action such as updating the state of your player’s user interface.

[`AVPlayer`](avplayer.md) and [`AVPlayerItem`](avplayeritem.md) are nonvisual objects, meaning that on their own they’re unable to present an asset’s video onscreen. There are two primary approaches you use to present your video content onscreen:

-  The best way to present your video content is with the AVKit framework’s [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) class in iOS and tvOS, or the [`AVPlayerView`](https://developer.apple.com/documentation/AVKit/AVPlayerView) class in macOS. These classes present the video content, along with playback controls and other media features giving you a full-featured playback experience.
-  When building a custom interface for your player, use [`AVPlayerLayer`](avplayerlayer.md). You can set this layer a view’s backing layer or add it directly to the layer hierarchy. Unlike [`AVPlayerView`](https://developer.apple.com/documentation/AVKit/AVPlayerView) and [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController), a player layer doesn’t present any playback controls—it only presents the visual content onscreen. It’s up to you to build the playback transport controls to play, pause, and seek through the media.

Alongside the visual content presented with AVKit or [`AVPlayerLayer`](avplayerlayer.md), you can also present animated content synchronized with the player’s timing using [`AVSynchronizedLayer`](avsynchronizedlayer.md). Use a synchronized layer pass along player timing to its layer subtree. You can use [`AVSynchronizedLayer`](avsynchronizedlayer.md) to build custom effects in Core Animation, such as animated lower thirds or video transitions, and have them play in sync with the timing of the player’s current [`AVPlayerItem`](avplayeritem.md).

## Topics

### Creating a Player
- [init(url: URL)](avplayer/init(url:).md)
  Creates a new player to play a single audiovisual resource referenced by a given URL.
- [init(playerItem: AVPlayerItem?)](avplayer/init(playeritem:).md)
  Creates a new player to play the specified player item.
- [init()](avplayer/init.md)
  Creates a player object.
### Managing the Player Item
- [var currentItem: AVPlayerItem?](avplayer/currentitem.md)
  The item for which the player is currently controlling playback.
- [func replaceCurrentItem(with: AVPlayerItem?)](avplayer/replacecurrentitem(with:).md)
  Replaces the current item with a new item.
### Determining Player Readiness
- [var status: AVPlayer.Status](avplayer/status-swift.property.md)
  A value that indicates the readiness of a player object for playback.
- [AVPlayer.Status](avplayer/status-swift.enum.md)
  Status values that indicate whether a player can successfully play media.
- [var error: (any Error)?](avplayer/error.md)
  An error that caused a failure.
### Controlling Playback
- [var defaultRate: Float](avplayer/defaultrate.md)
  A default rate at which to begin playback.
- [func play()](avplayer/play.md)
  Begins playback of the current item.
- [func pause()](avplayer/pause.md)
  Pauses playback of the current item.
- [var rate: Float](avplayer/rate.md)
  The current playback rate.
- [class let rateDidChangeNotification: NSNotification.Name](avplayer/ratedidchangenotification.md)
  A notification that a player posts when its rate changes.
### Observing Playback Time
- [func currentTime() -> CMTime](avplayer/currenttime.md)
  Returns the current time of the current player item.
- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](avplayer/addperiodictimeobserver(forinterval:queue:using:).md)
  Requests the periodic invocation of a given block during playback to report changing time.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](avplayer/addboundarytimeobserver(fortimes:queue:using:).md)
  Requests the invocation of a block when specified times are traversed during normal playback.
- [func removeTimeObserver(Any)](avplayer/removetimeobserver(_:).md)
  Cancels a previously registered periodic or boundary time observer.
### Seeking Through Media
- [func seek(to: CMTime)](avplayer/seek(to:)-87h2r.md)
  Requests that the player seek to a specified time.
- [func seek(to: CMTime, completionHandler: (Bool) -> Void)](avplayer/seek(to:completionhandler:)-75bls.md)
  Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](avplayer/seek(to:tolerancebefore:toleranceafter:).md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (Bool) -> Void)](avplayer/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.
- [func seek(to: Date)](avplayer/seek(to:)-9h9qr.md)
  Requests that the player seek to a specified date.
- [func seek(to: Date, completionHandler: (Bool) -> Void)](avplayer/seek(to:completionhandler:)-wr1l.md)
  Requests that the player seek to a specified date, and to notify you when the seek is complete.
### Configuring Waiting Behavior
- [var automaticallyWaitsToMinimizeStalling: Bool](avplayer/automaticallywaitstominimizestalling.md)
  A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [var reasonForWaitingToPlay: AVPlayer.WaitingReason?](avplayer/reasonforwaitingtoplay.md)
  The reason the player is currently waiting for playback to begin or resume.
- [AVPlayer.WaitingReason](avplayer/waitingreason.md)
  The reasons a player is waiting to begin or resume playback.
- [var timeControlStatus: AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.property.md)
  A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.enum.md)
  Constants that indicate the state of playback control.
- [func playImmediately(atRate: Float)](avplayer/playimmediately(atrate:).md)
  Plays the available media data immediately, at the specified rate.
### Responding When Playback Ends
- [var actionAtItemEnd: AVPlayer.ActionAtItemEnd](avplayer/actionatitemend-swift.property.md)
  The action to perform when the current player item has finished playing.
- [AVPlayer.ActionAtItemEnd](avplayer/actionatitemend-swift.enum.md)
  The actions a player can take when it finishes playing.
### Configuring Media Selection Criteria
- [var appliesMediaSelectionCriteriaAutomatically: Bool](avplayer/appliesmediaselectioncriteriaautomatically.md)
  A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.
- [func mediaSelectionCriteria(forMediaCharacteristic: AVMediaCharacteristic) -> AVPlayerMediaSelectionCriteria?](avplayer/mediaselectioncriteria(formediacharacteristic:).md)
  Returns the automatic selection criteria for media items with the specified media characteristic.
- [func setMediaSelectionCriteria(AVPlayerMediaSelectionCriteria?, forMediaCharacteristic: AVMediaCharacteristic)](avplayer/setmediaselectioncriteria(_:formediacharacteristic:).md)
  Applies automatic selection criteria for media that has the specified media characteristic.
### Accessing Player Output
- [var videoOutput: AVPlayerVideoOutput?](avplayer/videooutput.md)
  The video output for this player.
### Configuring Audio Behavior
- [var volume: Float](avplayer/volume.md)
  The audio playback volume for the player.
- [var isMuted: Bool](avplayer/ismuted.md)
  A Boolean value that indicates whether the audio output of the player is muted.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [var isAudioSpatializationAllowed: Bool](avplayeritem/isaudiospatializationallowed.md)
  A Boolean value that indicates whether the player item allows spatialized audio playback.
### Configuring Background Playback
- [var audiovisualBackgroundPlaybackPolicy: AVPlayerAudiovisualBackgroundPlaybackPolicy](avplayer/audiovisualbackgroundplaybackpolicy.md)
  A policy that determines how playback of audiovisual media continues when the app transitions to the background.
- [enum AVPlayerAudiovisualBackgroundPlaybackPolicy](avplayeraudiovisualbackgroundplaybackpolicy.md)
  Policies that describe playback behavior when an app transitions to the background while playing video.
### Managing External Playback
- [var allowsExternalPlayback: Bool](avplayer/allowsexternalplayback.md)
  A Boolean value that indicates whether the player allows switching to external playback mode.
- [var isExternalPlaybackActive: Bool](avplayer/isexternalplaybackactive.md)
  A Boolean value that indicates whether the player is currently playing video in external playback mode.
- [var usesExternalPlaybackWhileExternalScreenIsActive: Bool](avplayer/usesexternalplaybackwhileexternalscreenisactive.md)
  A Boolean value that indicates whether the player should automatically switch to external playback mode while the external screen mode is active.
- [var externalPlaybackVideoGravity: AVLayerVideoGravity](avplayer/externalplaybackvideogravity.md)
  The video gravity of the player for external playback mode only.
### Determining HDR Playback Eligibility
- [class var eligibleForHDRPlayback: Bool](avplayer/eligibleforhdrplayback.md)
  A Boolean value that indicates whether the current device can present content to an HDR display.
- [class var availableHDRModes: AVPlayer.HDRMode](avplayer/availablehdrmodes.md)
  The HDR modes that are available for playback.
- [AVPlayer.HDRMode](avplayer/hdrmode.md)
  A bitfield type that specifies an HDR mode.
- [class let eligibleForHDRPlaybackDidChangeNotification: NSNotification.Name](avplayer/eligibleforhdrplaybackdidchangenotification.md)
  A notification that’s posted whenever HDR playback eligibility changes.
### Coordinating Playback
- [var playbackCoordinator: AVPlayerPlaybackCoordinator](avplayer/playbackcoordinator.md)
  The playback coordinator for the player.
### Synchronizing Multiple Players
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](avplayer/setrate(_:time:athosttime:).md)
  Synchronizes the playback rate and time of the current item with an external source.
- [func preroll(atRate: Float, completionHandler: ((Bool) -> Void)?)](avplayer/preroll(atrate:completionhandler:).md)
  Begins loading media data to prime the media pipelines for playback.
- [func cancelPendingPrerolls()](avplayer/cancelpendingprerolls.md)
  Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [var sourceClock: CMClock?](avplayer/sourceclock.md)
  A clock the player uses for item time bases.
- [var masterClock: CMClock?](avplayer/masterclock.md)
  The host clock for item time bases.
### Preventing Sleep and Backgrounding
- [var preventsDisplaySleepDuringVideoPlayback: Bool](avplayer/preventsdisplaysleepduringvideoplayback.md)
  A Boolean value that indicates whether video playback prevents display and device sleep.
- [var preventsAutomaticBackgroundingDuringVideoPlayback: Bool](avplayer/preventsautomaticbackgroundingduringvideoplayback.md)
  A Boolean value that indicates whether video playback prevents the system from automatically backgrounding the app.
### Determining Content Protections
- [var isOutputObscuredDueToInsufficientExternalProtection: Bool](avplayer/isoutputobscuredduetoinsufficientexternalprotection.md)
  A Boolean value that indicates whether output is being obscured because of insufficient external protection.
### Configuring Audio and Video Devices
- [var audioOutputDeviceUniqueID: String?](avplayer/audiooutputdeviceuniqueid.md)
  Specifies the unique ID of the Core Audio output device used to play audio.
- [var preferredVideoDecoderGPURegistryID: UInt64](avplayer/preferredvideodecodergpuregistryid.md)
  The registry identifier for the GPU used for video decoding.
### Configuring AirPlay Behavior
- [var allowsAirPlayVideo: Bool](avplayer/allowsairplayvideo.md)
  A Boolean value that indicates whether the player allows AirPlay video playback.
- [var isAirPlayVideoActive: Bool](avplayer/isairplayvideoactive.md)
  A Boolean value that indicates whether the player is playing video through AirPlay.
- [var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool](avplayer/usesairplayvideowhileairplayscreenisactive.md)
  A Boolean value that indicates whether the player automatically switches to AirPlay Video while AirPlay Screen is active.
### Displaying Closed Captions
- [var isClosedCaptionDisplayEnabled: Bool](avplayer/isclosedcaptiondisplayenabled.md)
  A Boolean value that indicates whether the player uses closed captioning.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVQueuePlayer](avqueueplayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
  Play, pause, and seek through a media presentation.
- [class AVPlayerItem](avplayeritem.md)
  An object that models the timing and presentation state of an asset during playback.
- [class AVPlayerItemTrack](avplayeritemtrack.md)
  An object that represents the presentation state of an asset track during playback.
- [class AVQueuePlayer](avqueueplayer.md)
  An object that plays a sequence of player items.
- [class AVPlayerLooper](avplayerlooper.md)
  An object that loops media content using a queue player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer)*