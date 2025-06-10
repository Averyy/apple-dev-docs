# AVPlayerItem

**Framework**: AVFoundation  
**Kind**: class

An object that models the timing and presentation state of an asset during playback.

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
class AVPlayerItem
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
- [Implementing simple enhanced buffering for your content](implementing-simple-enhanced-buffering-for-your-content.md)
- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md)
- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)

#### Overview

A player item stores a reference to an [`AVAsset`](avasset.md) object, which represents the media to play. If you require inspecting an asset before you enqueue it for playback, call its `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the values of one or more properties. Alternatively, you can tell the player item to automatically load the required properties by passing them to its [`init(asset:automaticallyLoadedAssetKeys:)`](avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh.md) initializer. When the player item is ready to play, the asset properties you request are ready to use.

## Topics

### Creating a Player Item
- [convenience init(url: URL)](avplayeritem/init(url:).md)
  Creates a player item with a specified URL.
- [convenience init(asset: AVAsset)](avplayeritem/init(asset:)-87rjl.md)
  Creates a player item for a specified asset.
- [convenience init(asset: any AVAsset & Sendable)](avplayeritem/init(asset:)-1nme9.md)
- [convenience init(asset: AVAsset, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh.md)
  Creates a player item for the asset, and automatically loads values for the specified properties.
- [convenience init(asset: any AVAsset & Sendable, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-85hal.md)
- [init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)](avplayeritem/init(asset:automaticallyloadedassetkeys:)-8x4.md)
  Creates a player item with the specified asset and the asset keys to automatically load.
### Accessing Tracks
- [var tracks: [AVPlayerItemTrack]](avplayeritem/tracks.md)
  An array of player item track objects.
### Accessing Metadata
- [var externalMetadata: [AVMetadataItem]](avplayeritem/externalmetadata.md)
  An array of additional metadata for the player item to supplement or replace an asset’s embedded metadata.
### Determining Readiness
- [var status: AVPlayerItem.Status](avplayeritem/status-swift.property.md)
  The status of the player item.
- [AVPlayerItem.Status](avplayeritem/status-swift.enum.md)
  The statuses for a player item.
- [var error: (any Error)?](avplayeritem/error.md)
  The error that caused the player item to fail.
### Determining Playback Capabilities
- [var canPlayReverse: Bool](avplayeritem/canplayreverse.md)
  A Boolean value that indicates whether the item can play in reverse.
- [var canPlayFastForward: Bool](avplayeritem/canplayfastforward.md)
  A Boolean value that indicates whether the item can be fast forwarded.
- [var canPlayFastReverse: Bool](avplayeritem/canplayfastreverse.md)
  A Boolean value that indicates whether the item can be quickly reversed.
- [var canPlaySlowForward: Bool](avplayeritem/canplayslowforward.md)
  A Boolean value that indicates whether the item can play slower than normal.
- [var canPlaySlowReverse: Bool](avplayeritem/canplayslowreverse.md)
  A Boolean value that indicates whether the item can play slowly backward.
### Setting Playback Boundaries
- [var forwardPlaybackEndTime: CMTime](avplayeritem/forwardplaybackendtime.md)
  The time at which forward playback ends.
- [var reversePlaybackEndTime: CMTime](avplayeritem/reverseplaybackendtime.md)
  The time at which reverse playback ends.
### Stepping Through Media
- [var canStepForward: Bool](avplayeritem/canstepforward.md)
  A Boolean value that indicates whether the item supports stepping forward.
- [var canStepBackward: Bool](avplayeritem/canstepbackward.md)
  A Boolean value that indicates whether the item supports stepping backward.
- [func step(byCount: Int)](avplayeritem/step(bycount:).md)
  Moves the player item’s current time forward or backward by a specified number of steps.
### Seeking Through Media
- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:completionhandler:)-91gnw.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [func seek(to: Date, completionHandler: ((Bool) -> Void)?) -> Bool](avplayeritem/seek(to:completionhandler:)-1dibq.md)
  Sets the current playback time to the time specified by the date object.
- [func cancelPendingSeeks()](avplayeritem/cancelpendingseeks.md)
  Cancels any pending seek requests and invokes the corresponding completion handlers if present.
### Selecting Media Options
- [var currentMediaSelection: AVMediaSelection](avplayeritem/currentmediaselection.md)
  The current media selections for each of the receiver’s media selection groups.
- [func select(AVMediaSelectionOption?, in: AVMediaSelectionGroup)](avplayeritem/select(_:in:).md)
  Selects a media option in a given media selection group and deselects all other options in that group.
- [func selectMediaOptionAutomatically(in: AVMediaSelectionGroup)](avplayeritem/selectmediaoptionautomatically(in:).md)
  Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.
### Setting Variant Behavior
- [var variantPreferences: AVVariantPreferences](avplayeritem/variantpreferences.md)
  The preferences the player item uses when selecting variant playlists.
- [struct AVVariantPreferences](avvariantpreferences.md)
  Defines the preferences the player item uses when selecting variant playlists.
- [var startsOnFirstEligibleVariant: Bool](avplayeritem/startsonfirsteligiblevariant.md)
  A Boolean value that indicates whether playback starts with the first eligible variant that appears in the stream’s main playlist.
### Configuring Interstitial Events
- [var integratedTimeline: AVPlayerItemIntegratedTimeline](avplayeritem/integratedtimeline.md)
  An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [var automaticallyHandlesInterstitialEvents: Bool](avplayeritem/automaticallyhandlesinterstitialevents.md)
  A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [var interstitialTimeRanges: [AVInterstitialTimeRange]](avplayeritem/interstitialtimeranges.md)
  An array of time ranges that identify interstitial content.
- [var template: AVPlayerItem?](avplayeritem/template.md)
  The template player item that initializes this instance.
### Accessing Timing Information
- [func currentTime() -> CMTime](avplayeritem/currenttime.md)
  Returns the current time of the item.
- [func currentDate() -> Date?](avplayeritem/currentdate.md)
  Returns the current time of the item as a date.
- [var duration: CMTime](avplayeritem/duration.md)
  The duration of the item.
- [var timebase: CMTimebase?](avplayeritem/timebase.md)
  The timebase information for the item.
### Determining Available Time Ranges
- [var loadedTimeRanges: [NSValue]](avplayeritem/loadedtimeranges.md)
  An array of time ranges indicating media data that is readily available.
- [var seekableTimeRanges: [NSValue]](avplayeritem/seekabletimeranges.md)
  An array of time ranges within which it is possible to seek.
### Determining Buffering Status
- [var isPlaybackLikelyToKeepUp: Bool](avplayeritem/isplaybacklikelytokeepup.md)
  A Boolean value that indicates whether the item will likely play through without stalling.
- [var isPlaybackBufferFull: Bool](avplayeritem/isplaybackbufferfull.md)
  A Boolean value that indicates whether the internal media buffer is full and that further I/O is suspended.
- [var isPlaybackBufferEmpty: Bool](avplayeritem/isplaybackbufferempty.md)
  A Boolean value that indicates whether playback has consumed all buffered media and that playback will stall or end.
### Configuring Expensive Network Behavior
- [var preferredPeakBitRateForExpensiveNetworks: Double](avplayeritem/preferredpeakbitrateforexpensivenetworks.md)
  A limit of network bandwidth consumption by the item when connecting over expensive networks.
- [var preferredMaximumResolutionForExpensiveNetworks: CGSize](avplayeritem/preferredmaximumresolutionforexpensivenetworks.md)
  An upper limit on the resolution of video to download when connecting over expensive networks.
### Accessing Text Style Rules
- [var textStyleRules: [AVTextStyleRule]?](avplayeritem/textstylerules.md)
  An array of text style rules that specify the formatting and presentation of Web Video Text Tracks (WebVTT) subtitles.
- [class AVTextStyleRule](avtextstylerule.md)
  An object that represents the text styling rules to apply to a media item’s textual content.
### Accessing Logging Information
- [func accessLog() -> AVPlayerItemAccessLog?](avplayeritem/accesslog.md)
  Returns an object that represents a snapshot of the network access log.
- [class AVPlayerItemAccessLog](avplayeritemaccesslog.md)
  An object used to retrieve the access log associated with a player item.
- [class AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md)
  A single entry in a player item’s access log.
- [func errorLog() -> AVPlayerItemErrorLog?](avplayeritem/errorlog.md)
  Returns an object that represents a snapshot of the error log.
- [class AVPlayerItemErrorLog](avplayeritemerrorlog.md)
  The error log associated with a player item.
- [class AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md)
  A single item in a player item’s error log.
### Observing Notifications
- [class let didPlayToEndTimeNotification: NSNotification.Name](avplayeritem/didplaytoendtimenotification.md)
  A notification the system posts when a player item plays to its end time.
- [class let failedToPlayToEndTimeNotification: NSNotification.Name](avplayeritem/failedtoplaytoendtimenotification.md)
  A notification that the system posts when a player item fails to play to its end time.
- [class let timeJumpedNotification: NSNotification.Name](avplayeritem/timejumpednotification.md)
  A notification the system posts when a player item’s time changes discontinuously.
- [class let playbackStalledNotification: NSNotification.Name](avplayeritem/playbackstallednotification.md)
  A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [class let mediaSelectionDidChangeNotification: NSNotification.Name](avplayeritem/mediaselectiondidchangenotification.md)
  A notification the player item posts when its media selection changes.
- [class let recommendedTimeOffsetFromLiveDidChangeNotification: NSNotification.Name](avplayeritem/recommendedtimeoffsetfromlivedidchangenotification.md)
  A notification the player item posts when its offset from the live time changes.
- [class let newAccessLogEntryNotification: NSNotification.Name](avplayeritem/newaccesslogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its access log.
- [class let newErrorLogEntryNotification: NSNotification.Name](avplayeritem/newerrorlogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its error log.
### Managing Time Offsets
- [var automaticallyPreservesTimeOffsetFromLive: Bool](avplayeritem/automaticallypreservestimeoffsetfromlive.md)
  A Boolean value that indicates whether the player preserves its time offset from the live time after a buffering operation.
- [var recommendedTimeOffsetFromLive: CMTime](avplayeritem/recommendedtimeoffsetfromlive.md)
  A recommended time offset from the live time based on observed network conditions.
- [var configuredTimeOffsetFromLive: CMTime](avplayeritem/configuredtimeoffsetfromlive.md)
  A time value that indicates the offset from the live time to start playback, or resume playback after a seek to positive infinity.
### Configuring Presentation
- [var presentationSize: CGSize](avplayeritem/presentationsize.md)
  The size at which the visual portion of the item is presented by the player.
- [var preferredMaximumResolution: CGSize](avplayeritem/preferredmaximumresolution.md)
  The desired maximum resolution of a video that is to be downloaded.
- [var videoApertureMode: AVVideoApertureMode](avplayeritem/videoaperturemode.md)
  The video aperture mode to apply during playback.
- [struct AVVideoApertureMode](avvideoaperturemode.md)
  A value that describes how a video is scaled or cropped.
### Accessing Now Playing Information
- [var nowPlayingInfo: [String : Any]?](avplayeritem/nowplayinginfo.md)
  The current now playing information for the player item.
### Configuring HDR Settings
- [var appliesPerFrameHDRDisplayMetadata: Bool](avplayeritem/appliesperframehdrdisplaymetadata.md)
  A Boolean value that indicates whether the player item applies per-frame HDR display metadata during playback.
### Configuring Video Compositing
- [var videoComposition: AVVideoComposition?](avplayeritem/videocomposition.md)
  The video composition settings to be applied during playback.
- [var customVideoCompositor: (any AVVideoCompositing)?](avplayeritem/customvideocompositor.md)
  The custom video compositor.
- [var seekingWaitsForVideoCompositionRendering: Bool](avplayeritem/seekingwaitsforvideocompositionrendering.md)
  A Boolean value that indicates whether the item’s timing follows the displayed video frame when seeking with a video composition.
### Configuring Audio
- [var audioMix: AVAudioMix?](avplayeritem/audiomix.md)
  The audio mix parameters to be applied during playback.
- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](avplayeritem/audiotimepitchalgorithm.md)
  The processing algorithm used to manage audio pitch for scaled audio edits.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [struct AVAudioSpatializationFormats](avaudiospatializationformats.md)
  A structure that defines the spatialization formats that a player item supports.
- [var isAudioSpatializationAllowed: Bool](avplayeritem/isaudiospatializationallowed.md)
  A Boolean value that indicates whether the player item allows spatialized audio playback.
### Managing Player Item Outputs
- [var outputs: [AVPlayerItemOutput]](avplayeritem/outputs.md)
  An array of outputs associated with the player item.
- [func add(AVPlayerItemOutput)](avplayeritem/add(_:)-16ctk.md)
  Adds the specified player item output object to the receiver.
- [func remove(AVPlayerItemOutput)](avplayeritem/remove(_:)-46b1r.md)
  Removes the specified player item output object from the receiver.
### Managing Player Item Data Collectors
- [var mediaDataCollectors: [AVPlayerItemMediaDataCollector]](avplayeritem/mediadatacollectors.md)
  The collection of associated media data collectors.
- [func add(AVPlayerItemMediaDataCollector)](avplayeritem/add(_:)-9l3to.md)
  Adds the specified media data collector to the player item’s collection of media collectors.
- [func remove(AVPlayerItemMediaDataCollector)](avplayeritem/remove(_:)-29iuz.md)
  Removes the specified media data collector from the player item’s collection of media collectors.
### Configuring Network Behavior
- [var preferredPeakBitRate: Double](avplayeritem/preferredpeakbitrate.md)
  The desired limit, in bits per second, of network bandwidth consumption for this item.
- [var preferredForwardBufferDuration: TimeInterval](avplayeritem/preferredforwardbufferduration.md)
  The duration the player should buffer media from the network ahead of the playhead to guard against playback disruption.
- [var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool](avplayeritem/canusenetworkresourcesforlivestreamingwhilepaused.md)
  A Boolean value that indicates whether the player item can use network resources to keep the playback state up to date while paused.
### Managing Playback Authorization in macOS
- [var isContentAuthorizedForPlayback: Bool](avplayeritem/iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isAuthorizationRequiredForPlayback: Bool](avplayeritem/isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [var isApplicationAuthorizedForPlayback: Bool](avplayeritem/isapplicationauthorizedforplayback.md)
  A Boolean value that indicates whether the application can be used to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:).md)
  Presents the user the opportunity to authorize the content for playback.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](avplayeritem/contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [enum AVContentAuthorizationStatus](avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.
- [func cancelContentAuthorizationRequest()](avplayeritem/cancelcontentauthorizationrequest.md)
  Cancels the currently outstanding content authorization request.
### Accessing Initialization Parameters
- [var asset: AVAsset](avplayeritem/asset.md)
  The asset provided during initialization.
- [var automaticallyLoadedAssetKeys: [String]](avplayeritem/automaticallyloadedassetkeys.md)
  The array of asset keys to be automatically loaded before the player item is ready to play.
### Copying an Player Item
- [func copy() -> Any](avplayeritem/copy.md)
  Creates a copy of the object.
- [func copy(with: NSZone?) -> Any](avplayeritem/copy(with:).md)
  Creates a copy of the object with the specified zone.
### Deprecated
- [Deprecated Symbols](avplayeritem-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var preferredCustomMediaSelectionSchemes: [AVCustomMediaSelectionScheme]](avplayeritem/preferredcustommediaselectionschemes.md)
  Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
### Instance Methods
- [func effectiveMediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]](avplayeritem/effectivemediapresentationsettings(for:).md)
  Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.
- [func select(AVMediaPresentationSetting, for: AVMediaSelectionGroup)](avplayeritem/select(_:for:).md)
  When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
- [func selectMediaPresentationLanguage(String, for: AVMediaSelectionGroup)](avplayeritem/selectmediapresentationlanguage(_:for:).md)
  When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.
- [func selectedMediaPresentationLanguage(for: AVMediaSelectionGroup) -> String?](avplayeritem/selectedmediapresentationlanguage(for:).md)
  Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.
- [func selectedMediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]](avplayeritem/selectedmediapresentationsettings(for:).md)
  Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md)
  Keep your user interface in sync with state changes from playback objects.
- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
  Play, pause, and seek through a media presentation.
- [Creating a seamless multiview playback experience](creating-a-seamless-multiview-playback-experience.md)
  Build advanced multiview playback experiences with the AVFoundation and AVRouting frameworks.
- [class AVPlayer](avplayer.md)
  An object that provides the interface to control the player’s transport behavior.
- [class AVPlayerItemTrack](avplayeritemtrack.md)
  An object that represents the presentation state of an asset track during playback.
- [class AVQueuePlayer](avqueueplayer.md)
  An object that plays a sequence of player items.
- [class AVPlayerLooper](avplayerlooper.md)
  An object that loops media content using a queue player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem)*