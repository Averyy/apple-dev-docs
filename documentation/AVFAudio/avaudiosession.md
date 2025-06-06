# AVAudioSession

**Framework**: AVFAudio  
**Kind**: class

An object that communicates to the system how you intend to use audio in your app.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioSession
```

## Mentions

- [Handling audio interruptions](handling-audio-interruptions.md)
- [Responding to audio route changes](responding-to-audio-route-changes.md)

#### Overview

An audio session acts as an intermediary between your app and the operating system — and, in turn, the underlying audio hardware. You use an audio session to communicate to the operating system the general nature of your app’s audio without detailing the specific behavior or required interactions with the audio hardware. You delegate the management of those details to the audio session, which ensures that the operating system can best manage the user’s audio experience.

All iOS, tvOS, and watchOS apps have a default audio session that comes preconfigured with the following behavior:

- It supports audio playback, but disallows audio recording.
- When the app plays audio, it silences any other background audio.
- In iOS, setting the Ring/Silent switch to silent mode silences any audio the app is playing.
- In iOS, locking a device silences the app’s audio.

Although the default audio session provides useful behavior, it generally doesn’t provide the audio behavior a media app needs. To change the default behavior, you configure your app’s audio session category.

There are six possible categories you can use, but [`playback`](avaudiosession/category-swift.struct/playback.md) is the one that playback apps most commonly use. This category indicates that audio playback is a central feature of your app. When you specify this category, your app’s audio continues with the Ring/Silent switch set to silent mode (iOS only). Using this category, you can also play background audio if you’re using the Audio, AirPlay, and Picture in Picture background mode. For more information, see `Enabling Background Audio`.

You use an [`AVAudioSession`](avaudiosession.md) object to configure your app’s audio session. This class is a singleton object used to set the audio session’s category, mode, and other configurations. You can interact with the audio session throughout your app’s life cycle, but it’s often useful to perform this configuration at app launch, as shown in the following example.

```swift
func configureAudioSession() {
    // Retrieve the shared audio session.
    let audioSession = AVAudioSession.sharedInstance()
    do {
        // Set the audio session category and mode.
        try audioSession.setCategory(.playback, mode: .moviePlayback)
    } catch {
        print("Failed to set the audio session configuration")
    }
}
```

The audio session uses this configuration when you activate the session using the [`setActive:error:`](avaudiosession/setactive:error:.md) or [`setActive(_:options:)`](avaudiosession/setactive(_:options:).md) method.

> **Note**:  You can activate the audio session at any time after setting its category, but it’s generally preferable to defer this call until your app begins audio playback. Deferring the call ensures that you won’t prematurely interrupt any other background audio that may be in progress.

 You can activate the audio session at any time after setting its category, but it’s generally preferable to defer this call until your app begins audio playback. Deferring the call ensures that you won’t prematurely interrupt any other background audio that may be in progress.

## Topics

### Accessing the shared audio session
- [class func sharedInstance() -> AVAudioSession](avaudiosession/sharedinstance.md)
  Returns the shared audio session instance.
### Configuring standard audio behaviors
- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, policy: AVAudioSession.RouteSharingPolicy, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:mode:policy:options:).md)
  Sets the session category, mode, route-sharing policy, and options.
- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:mode:options:).md)
  Sets the audio session’s category, mode, and options.
- [func setCategory(AVAudioSession.Category, options: AVAudioSession.CategoryOptions) throws](avaudiosession/setcategory(_:options:).md)
  Sets the audio session’s category with the specified options.
- [func setCategory(AVAudioSession.Category) throws](avaudiosession/setcategory(_:).md)
  Sets the audio session’s category.
- [func setMode(AVAudioSession.Mode) throws](avaudiosession/setmode(_:).md)
  Sets the audio session’s mode.
### Configuring the spatial experience in visionOS
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](avaudiosession/setintendedspatialexperience(_:).md)
  Sets the spatial audio experience your app intends to provide the user.
- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](avaudiosession/intendedspatialexperience-1qwbe.md)
  The spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](../AVFoundation/AVAudioSessionSpatialExperience.md)
  A protocol that defines types of spatial audio experiences that the system supports.
- [AVAudioSession.HeadTrackedSpatialExperience](avaudiosession/headtrackedspatialexperience.md)
  An experience where the sound a size dictated by its sound stage and location dictated by its anchoring strategy.
- [AVAudioSession.FixedSpatialExperience](avaudiosession/fixedspatialexperience.md)
  An experience where the sound has a size dictated by its sound stage and is head-locked relative to the user.
- [AVAudioSession.BypassedSpatialExperience](avaudiosession/bypassedspatialexperience.md)
  An experience that bypasses system-provided audio spatialization.
- [AVAudioSession.AnchoringStrategy](avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [AVAudioSession.SoundStageSize](avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [var isNowPlayingCandidate: Bool](avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](avaudiosession/setisnowplayingcandidate(_:).md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
### Activating the audio configuration
- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](avaudiosession/setactive(_:options:).md)
  Activates or deactivates your app’s audio session using the specified options.
- [func activate(options: AVAudioSessionActivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](avaudiosession/activate(options:completionhandler:).md)
  Activates an audio session asynchronously on watchOS.
- [struct AVAudioSessionActivationOptions](avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.
### Inspecting the category configuration
- [var category: AVAudioSession.Category](avaudiosession/category-swift.property.md)
  The current audio session category.
- [var availableCategories: [AVAudioSession.Category]](avaudiosession/availablecategories.md)
  The audio session categories available on the current device.
- [AVAudioSession.Category](avaudiosession/category-swift.struct.md)
  Audio session category identifiers.
- [var categoryOptions: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.property.md)
  The set of options associated with the current audio session category.
- [AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.
### Inspecting mode configuration
- [var mode: AVAudioSession.Mode](avaudiosession/mode-swift.property.md)
  The current audio session’s mode.
- [var availableModes: [AVAudioSession.Mode]](avaudiosession/availablemodes.md)
  The audio session modes available on the device.
- [AVAudioSession.Mode](avaudiosession/mode-swift.struct.md)
  Audio session mode identifiers.
### Inspecting rendering mode and capabilities
- [var renderingMode: AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [class let renderingModeChangeNotification: NSNotification.Name](avaudiosession/renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](avaudiosession/supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.
### Inspecting the route sharing policy
- [var routeSharingPolicy: AVAudioSession.RouteSharingPolicy](avaudiosession/routesharingpolicy-swift.property.md)
  The active route-sharing policy.
- [AVAudioSession.RouteSharingPolicy](avaudiosession/routesharingpolicy-swift.enum.md)
  Cases that indicate the possible route-sharing policies for an audio session.
### Mixing with other audio
- [var isOtherAudioPlaying: Bool](avaudiosession/isotheraudioplaying.md)
  A Boolean value that indicates whether another app is playing audio.
- [var secondaryAudioShouldBeSilencedHint: Bool](avaudiosession/secondaryaudioshouldbesilencedhint.md)
  A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](avaudiosession/silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
- [var allowHapticsAndSystemSoundsDuringRecording: Bool](avaudiosession/allowhapticsandsystemsoundsduringrecording.md)
  A Boolean value that indicates whether system sounds and haptics play while recording from audio input.
- [func setAllowHapticsAndSystemSoundsDuringRecording(Bool) throws](avaudiosession/setallowhapticsandsystemsoundsduringrecording(_:).md)
  Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.
### Managing audio routing
- [Audio routing](audio-routing.md)
  Inspect and configure audio routes, ports, and data sources.
### Preparing for long-form video playback
- [func prepareRouteSelectionForPlayback(completionHandler: (Bool, AVAudioSession.RouteSelection) -> Void)](avaudiosession/preparerouteselectionforplayback(completionhandler:).md)
  Prepares the route selection for long-form video playback.
- [AVAudioSession.RouteSelection](avaudiosession/routeselection.md)
  Constants used to define the active route selection.
### Handling interruptions
- [var prefersNoInterruptionsFromSystemAlerts: Bool](avaudiosession/prefersnointerruptionsfromsystemalerts.md)
  A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [func setPrefersNoInterruptionsFromSystemAlerts(Bool) throws](avaudiosession/setprefersnointerruptionsfromsystemalerts(_:).md)
  Sets the preference for not interrupting the audio session with system alerts.
- [var prefersInterruptionOnRouteDisconnect: Bool](avaudiosession/prefersinterruptiononroutedisconnect.md)
  A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.
- [func setPrefersInterruptionOnRouteDisconnect(Bool) throws](avaudiosession/setprefersinterruptiononroutedisconnect(_:).md)
  Sets a preference to interrupt the audio session when the active route disconnects.
- [class let interruptionNotification: NSNotification.Name](avaudiosession/interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.
### Monitoring spatial capabilities
- [class let spatialPlaybackCapabilitiesChangedNotification: NSNotification.Name](avaudiosession/spatialplaybackcapabilitieschangednotification.md)
  A notification the system posts when its spatial playback capabilities change.
### Inspecting the audio prompt style
- [var promptStyle: AVAudioSession.PromptStyle](avaudiosession/promptstyle-swift.property.md)
  A hint to audio sessions that use voice prompt mode to alter the type of prompts they issue in response to other system audio, such as Siri and phone calls.
- [AVAudioSession.PromptStyle](avaudiosession/promptstyle-swift.enum.md)
  Constants that indicate the prompt style to use.
### Enabling stereo recording
- [var inputOrientation: AVAudioSession.StereoOrientation](avaudiosession/inputorientation.md)
  An orientation value that dictates which directions represent left and right when capturing audio from a built-in microphone configured for stereo recording.
- [var preferredInputOrientation: AVAudioSession.StereoOrientation](avaudiosession/preferredinputorientation.md)
  The audio session’s preferred stereo input orientation.
- [func setPreferredInputOrientation(AVAudioSession.StereoOrientation) throws](avaudiosession/setpreferredinputorientation(_:).md)
  Sets the audio session’s preferred stereo input orientation.
- [AVAudioSession.StereoOrientation](avaudiosession/stereoorientation.md)
  Constants that define the supported stereo orientations.
### Enabling adding audio to calls
- [var isMicrophoneInjectionAvailable: Bool](avaudiosession/ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode](avaudiosession/preferredmicrophoneinjectionmode.md)
  The preferred mode of injecting audio into another app’s input stream.
- [func setPreferredMicrophoneInjectionMode(AVAudioSession.MicrophoneInjectionMode) throws](avaudiosession/setpreferredmicrophoneinjectionmode(_:).md)
  Sets the preferred mode of injecting audio into another app’s input stream.
- [AVAudioSession.MicrophoneInjectionMode](avaudiosession/microphoneinjectionmode.md)
  The modes of injecting audio into another app’s input stream.
- [class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/microphoneinjectioncapabilitieschangenotification.md)
  A notification the system posts when its capability to inject audio into an input stream changes.
### Configuring echo cancellation
- [var isEchoCancelledInputAvailable: Bool](avaudiosession/isechocancelledinputavailable.md)
  A Boolean value that indicates whether the built-in microphone and speaker route supports echo cancellation.
- [var isEchoCancelledInputEnabled: Bool](avaudiosession/isechocancelledinputenabled.md)
  A Boolean value that indicates whether an echo-canceled input is in an enabled state.
- [func setPrefersEchoCancelledInput(Bool) throws](avaudiosession/setprefersechocancelledinput(_:).md)
  Sets a preference to enable echo-canceled input on supported hardware.
- [var prefersEchoCancelledInput: Bool](avaudiosession/prefersechocancelledinput.md)
  A Boolean value that indicates the audio session’s preference for using an echo-canceled input.
### Configuring device settings
- [Audio hardware](audio-hardware.md)
  Inspect and configure audio device settings including input gain, sample rate, and channel counts.
### Setting the aggregated I/O preference
- [func setAggregatedIOPreference(AVAudioSession.IOType) throws](avaudiosession/setaggregatediopreference(_:).md)
  Sets the audio session’s aggregated I/O configuration preference.
- [AVAudioSession.IOType](avaudiosession/iotype.md)
  Constant values used to specify the audio session’s aggregated I/O behavior.
### Handling a change of media services
- [class let mediaServicesWereResetNotification: NSNotification.Name](avaudiosession/mediaserviceswereresetnotification.md)
  A notification the system posts when the media server restarts.
- [class let mediaServicesWereLostNotification: NSNotification.Name](avaudiosession/mediaserviceswerelostnotification.md)
  A notification the system posts when it terminates the media server.
### Errors
- [AVAudioSession.ErrorCode](../CoreAudioTypes/AVAudioSession/ErrorCode.md)
  Codes that describe error conditions that may occur when performing audio session operations.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [Handling audio interruptions](handling-audio-interruptions.md)
  Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](responding-to-audio-route-changes.md)
  Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Adding synthesized speech to calls](adding-synthesized-speech-to-calls.md)
  Provide a more accessible experience by adding your app’s audio to a call.
- [Capturing stereo audio from built-In microphones](capturing-stereo-audio-from-built-in-microphones.md)
  Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [class AVAudioApplication](avaudioapplication.md)
  An object that manages one or more audio sessions that belong to an app.
- [class AVAudioRoutingArbiter](avaudioroutingarbiter.md)
  An object for configuring macOS apps to participate in AirPods Automatic Switching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession)*