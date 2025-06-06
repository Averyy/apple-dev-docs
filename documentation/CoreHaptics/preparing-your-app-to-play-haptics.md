# Preparing your app to play haptics

**Framework**: Core Haptics

Set up your app to play haptics.

#### Overview

This article describes the process of setting up your app to play haptics. You’ll check for device compatibility, create a haptic engine, and then configure the engine’s handler properties.

> **Note**:  Make sure you set the engine’s handler properties before starting it to play a haptic.

 Make sure you set the engine’s handler properties before starting it to play a haptic.

##### Check for Device Compatibility

Before you create and configure a haptic engine, check the hardware capabilities to see what type of feedback the device supports. Some devices don’t support haptic feedback, including iPad, iPod touch, and Apple Vision Pro. Checking the hardware capabilities lets you adjust your app’s behavior to provide alternative types of feedback as needed. For example, you might play stronger audio or multimedia, or you might provide visual feedback instead.

The following example fetches the hardware capabilities and checks the value of the [`supportsHaptics`](chhapticdevicecapability/supportshaptics.md) property to determine whether haptic feedback is available. The app then saves the result to a variable, which it uses later to determine what type of feedback to provide.

For an example of conditioning haptic playback, see [`Playing a Custom Haptic Pattern from a File`](playing-a-custom-haptic-pattern-from-a-file.md).

##### Create a Haptic Engine

The [`CHHapticEngine`](chhapticengine.md) is your app’s interface to the haptic device. Use an instance of a haptic engine to perform these key tasks:

- Create players to play those haptic and audio patterns.
- Play haptic patterns directly from a file URL.
- Modulate haptic patterns during playback.

Create this engine early in your app’s life cycle—for example, in your main view controller’s [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad())—and store it in an instance variable or property so it doesn’t go out of scope during playback.

> **Note**:  The haptic engine isn’t a singleton; you can create multiple instances in different parts of your app or game, like different view controllers or levels. Each instance of the haptic engine behaves independently. Core Haptics is thread-safe, meaning you can execute player operations on separate threads.

 The haptic engine isn’t a singleton; you can create multiple instances in different parts of your app or game, like different view controllers or levels. Each instance of the haptic engine behaves independently. Core Haptics is thread-safe, meaning you can execute player operations on separate threads.

##### Set the Reset Handler to Recover From Failure

Core Haptics calls the reset handler after the media server has recovered from failure. When this occurs, inside the reset handler, your app should do the following:

- Restart the haptic engine, if it was running at the time reset happened, by calling [`start()`](chhapticengine/start().md).
- Reregister any custom audio resources you had registered, using [`registerAudioResource(_:options:)`](chhapticengine/registeraudioresource(_:options:).md).
- Recreate all haptic pattern players you had created, using [`makePlayer(with:)`](chhapticengine/makeplayer(with:).md).

Your app could attempt to restart the engine inside the handler, allowing it to recover on its own. However, as shown in the code listing above, a restart may still fail if the external reason for the reset hasn’t subsided.

##### Receive Notification of Haptic Engine Stoppage Due to Outside Causes

When external factors cause the haptic engine to stop, like audio interruptions from a phone call or because the user has put your app in the background, Core Haptics calls the [`stoppedHandler`](chhapticengine/stoppedhandler-swift.property.md). The reason for the stoppage is passed into the handler. Because stopping is a normal part of the life cycle, you need to restart the engine before it can play the next haptic.

As you’re testing your app, set the [`stoppedHandler`](chhapticengine/stoppedhandler-swift.property.md) to debug the precise cause of the engine stoppage, as shown below.

In production, your app can handle each cause in a different way. For example, you could handle the case [`CHHapticEngine.StoppedReason.systemError`](chhapticengine/stoppedreason/systemerror.md) by continuing the app without haptics, or by throwing a fatal error to terminate the app.

> **Note**:  The stopped handler defined in the code above is called only when external causes trigger an engine stoppage. The stopped handler isn’t called if you manually stop the engine through an explicit [`stop(completionHandler:)`](chhapticengine/stop(completionhandler:).md) call. Instead, Core Haptics calls the completion handler passed as input to the explicit stop call.

 The stopped handler defined in the code above is called only when external causes trigger an engine stoppage. The stopped handler isn’t called if you manually stop the engine through an explicit [`stop(completionHandler:)`](chhapticengine/stop(completionhandler:).md) call. Instead, Core Haptics calls the completion handler passed as input to the explicit stop call.

##### Define and Play Haptics

Once you’ve set up your app to play haptics, you can incorporate haptic patterns. See:

- Simple haptic patterns defined inline as dictionaries: [`Playing a single-tap haptic pattern`](playing-a-single-tap-haptic-pattern.md)
- Custom file-based haptic patterns: [`Playing a Custom Haptic Pattern from a File`](playing-a-custom-haptic-pattern-from-a-file.md)
- Programmatic haptics tied to real-time physics: [`Playing Collision-Based Haptic Patterns`](playing-collision-based-haptic-patterns.md)

## See Also

- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)
  Create and play a transient haptic pattern from a dictionary literal inline.
- [class CHHapticEngine](chhapticengine.md)
  An object that represents the connection to the haptic server.
- [class CHHapticPattern](chhapticpattern.md)
  An object representing a haptic waveform.
- [protocol CHHapticPatternPlayer](chhapticpatternplayer.md)
  A protocol that defines a standard pattern player capable of playing haptic patterns with fixed parameters.
- [protocol CHHapticAdvancedPatternPlayer](chhapticadvancedpatternplayer.md)
  A protocol that defines an advanced pattern player capable of looping, seeking, pausing, and resuming haptic playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/preparing-your-app-to-play-haptics)*