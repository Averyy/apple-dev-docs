# CHHapticEngine

**Framework**: Core Haptics  
**Kind**: class

An object that represents the connection to the haptic server.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class CHHapticEngine
```

## Mentions

- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)
- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)

#### Overview

If you want your app to play custom haptics, you need to create a haptic engine. The haptic engine establishes the connection between your app and the underlying device hardware. Even though you can define a haptic pattern without an engine, you need the engine to play that pattern.

![A dictionary defines a pattern, from which the haptic engine creates a pattern player for playing the haptic.](https://docs-assets.developer.apple.com/published/66a613deacd96bc7ac01d5a15e3eae73/media-3242669%402x.png)

Even though your app makes a request through the haptic engine, the operating system could still override the request with system services, like haptics from system notifications.

##### Prepare Your App to Play Haptics

To prepare your app to play haptics, follow these steps, as demonstrated in the code below:

1. Create a haptic engine instance. Maintain a strong reference to it so it doesn’t go out of scope while the haptic is playing.
2. Call the haptic engine’s [`start(completionHandler:)`](chhapticengine/start(completionhandler:).md) for an asynchronous start, or [`start()`](chhapticengine/start().md) to start the engine synchronously (immediately).
3. Stop the engine by calling [`stop(completionHandler:)`](chhapticengine/stop(completionhandler:).md) when your app finishes haptic playback.

Although it’s possible to create content—[`CHHapticPattern`](chhapticpattern.md) instances—independent of a CHHapticEngine, your app must use an engine to play that content.

## Topics

### Initializing a Haptic Engine
- [init() throws](chhapticengine/init.md)
  Creates an instance of the haptic engine.
- [init(audioSession: AVAudioSession?) throws](chhapticengine/init(audiosession:).md)
  Creates a haptic engine from an audio session.
### Starting and Stopping the Haptic Engine
- [func start() throws](chhapticengine/start.md)
  Synchronously starts the haptic engine.
- [func start(completionHandler: (((any Error)?) -> Void)?)](chhapticengine/start(completionhandler:).md)
  Asynchronously starts the haptic engine.
- [func stop(completionHandler: (((any Error)?) -> Void)?)](chhapticengine/stop(completionhandler:).md)
  Asynchronously stops the haptic engine and executes the completion handler once the engine has stopped.
- [CHHapticEngine.CompletionHandler](chhapticengine/completionhandler.md)
  A typealias for a completion handler that the engine calls after starting or stopping.
### Creating Haptic Pattern Players
- [func makePlayer(with: CHHapticPattern) throws -> any CHHapticPatternPlayer](chhapticengine/makeplayer(with:).md)
  Creates a standard haptic pattern player from a haptic pattern.
- [func makeAdvancedPlayer(with: CHHapticPattern) throws -> any CHHapticAdvancedPatternPlayer](chhapticengine/makeadvancedplayer(with:).md)
  Creates an advanced haptic pattern player from a haptic pattern.
### Modifying Playback Properties
- [var playsAudioOnly: Bool](chhapticengine/playsaudioonly.md)
  A Boolean value that indicates whether the engine ignores haptic events and plays audio events only.
- [var playsHapticsOnly: Bool](chhapticengine/playshapticsonly.md)
  A Boolean value that indicates whether the engine ignores audio events.
- [var isMutedForAudio: Bool](chhapticengine/ismutedforaudio.md)
  A Boolean value that indicates whether the engine mutes audio.
- [var isMutedForHaptics: Bool](chhapticengine/ismutedforhaptics.md)
  A Boolean value that indicates whether the engine mutes haptics.
### Playing a Pattern
- [func playPattern(from: URL) throws](chhapticengine/playpattern(from:)-6m9m5.md)
  Plays a pattern that’s defined in a file at the specified URL.
- [func playPattern(from: Data) throws](chhapticengine/playpattern(from:)-7u8se.md)
  Plays a pattern from the specified data.
### Registering Audio Resources
- [func registerAudioResource(URL, options: [AnyHashable : Any]) throws -> CHHapticAudioResourceID](chhapticengine/registeraudioresource(_:options:).md)
  Registers an external audio to use as a custom waveform.
- [func unregisterAudioResource(CHHapticAudioResourceID) throws](chhapticengine/unregisteraudioresource(_:).md)
  Unregisters an external audio file that you previously registered with the engine.
- [typealias CHHapticAudioResourceID](chhapticaudioresourceid.md)
  A type that identifies a custom audio resource.
### Monitoring Finished Playback
- [func notifyWhenPlayersFinished(finishedHandler: CHHapticEngine.FinishedHandler)](chhapticengine/notifywhenplayersfinished(finishedhandler:).md)
  Notifies you when all haptic pattern players have finished playing their haptic patterns.
- [CHHapticEngine.FinishedHandler](chhapticengine/finishedhandler.md)
  A type alias for a completion handler to execute after finishing haptic playback.
- [CHHapticEngine.FinishedAction](chhapticengine/finishedaction.md)
  Possible actions to take after the haptic engine finishes execution.
### Handling Haptic Engine Resets
- [var resetHandler: CHHapticEngine.ResetHandler](chhapticengine/resethandler-swift.property.md)
  A block that the haptic engine calls after recovering from a haptic server error.
- [CHHapticEngine.ResetHandler](chhapticengine/resethandler-swift.typealias.md)
  A typealias for the block that the haptic engine calls after being reset.
### Handling Haptic Engine Stoppages
- [var stoppedHandler: CHHapticEngine.StoppedHandler](chhapticengine/stoppedhandler-swift.property.md)
  A closure the haptic engine calls when it stops due to external causes.
- [CHHapticEngine.StoppedHandler](chhapticengine/stoppedhandler-swift.typealias.md)
  A typealias for the block that the haptic engine calls after it stops due to an external cause.
- [CHHapticEngine.StoppedReason](chhapticengine/stoppedreason.md)
  The enumeration of reasons the haptic engine stopped running.
### Getting the Current Media Time
- [var currentTime: TimeInterval](chhapticengine/currenttime.md)
  The absolute time, in seconds, to use for scheduling haptic and audio events.
- [var CHHapticTimeImmediate: TimeInterval](chhaptictimeimmediate.md)
  A time constant used to schedule a command immediately.
### Querying System Capabilities
- [class func capabilitiesForHardware() -> any CHHapticDeviceCapability](chhapticengine/capabilitiesforhardware.md)
  Returns a device capability object that describes the device’s haptic support and limitations.
- [protocol CHHapticDeviceCapability](chhapticdevicecapability.md)
  A protocol that defines haptics and audio capabilities of a device.
- [protocol CHHapticParameterAttributes](chhapticparameterattributes.md)
  A protocol for providing default, mininum, and maximum values of a parameter.
- [func attributes(forDynamicParameter: CHHapticDynamicParameter.ID) throws -> any CHHapticParameterAttributes](chhapticdevicecapability/attributes(fordynamicparameter:).md)
  Requests the haptic device’s attributes for a dynamic parameter.
### Managing Power
- [var isAutoShutdownEnabled: Bool](chhapticengine/isautoshutdownenabled.md)
  A Boolean value that indicates whether the haptic engine starts and stops automatically on request from one of its pattern players, or when idle.
### Instance Properties
- [var intendedSpatialExperience: any SpatialAudioExperience](chhapticengine/intendedspatialexperience-55ca0.md)
  The CHHapticEngine’s intended spatial experience.

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

- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)
  Set up your app to play haptics.
- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)
  Create and play a transient haptic pattern from a dictionary literal inline.
- [class CHHapticPattern](chhapticpattern.md)
  An object representing a haptic waveform.
- [protocol CHHapticPatternPlayer](chhapticpatternplayer.md)
  A protocol that defines a standard pattern player capable of playing haptic patterns with fixed parameters.
- [protocol CHHapticAdvancedPatternPlayer](chhapticadvancedpatternplayer.md)
  A protocol that defines an advanced pattern player capable of looping, seeking, pausing, and resuming haptic playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine)*