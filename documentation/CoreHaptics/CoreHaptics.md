# Core Haptics

**Framework**: Core Haptics  
**Kind**: module

Compose and play haptic patterns to customize your iOS app’s haptic feedback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 14.0+
- visionOS 1.0+

#### Overview

Core Haptics lets you add customized haptic and audio feedback to your app. Use haptics to engage users physically, with tactile and audio feedback that gets attention and reinforces actions. Some system-provided interface elements—like pickers, switches, and sliders—automatically provide haptic feedback as users interact with them. With Core Haptics, you extend this functionality by composing and combining haptics beyond the default patterns.

Your app can play custom haptic patterns crafted from basic building blocks called haptic events ([`CHHapticEvent`](chhapticevent.md)). Events can be transient, like the feedback you get from toggling a switch, or continuous, like the vibration or sound from a ringtone. You can use transient and continuous patterns independently, or build your pattern from precise combinations of the two. Another type of haptic event allows you to play customized audio content as part of your pattern.

## Topics

### Essentials
- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)
  Set up your app to play haptics.
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
### Programmatic haptics
- [Delivering Rich App Experiences with Haptics](delivering-rich-app-experiences-with-haptics.md)
  Enhance your app’s experience by incorporating haptic and sound feedback into key interactive moments.
- [Playing Collision-Based Haptic Patterns](playing-collision-based-haptic-patterns.md)
  Play a custom haptic pattern whose strength depends on an object’s collision speed.
- [Updating Continuous and Transient Haptic Parameters in Real Time](updating-continuous-and-transient-haptic-parameters-in-real-time.md)
  Generate continuous and transient haptic patterns in response to user touch.
- [class CHHapticEvent](chhapticevent.md)
  An object that describes a single haptic or audio event.
- [class CHHapticEventParameter](chhapticeventparameter.md)
  A static parameter value that represents a single property of the haptic pattern.
- [class CHHapticDynamicParameter](chhapticdynamicparameter.md)
  A value that you send to a haptic pattern player to alter a property value during playback.
- [class CHHapticParameterCurve](chhapticparametercurve.md)
  A curve that you send to a haptic pattern player to alter a property value gradually during playback.
### File-based haptics
- [Playing a Custom Haptic Pattern from a File](playing-a-custom-haptic-pattern-from-a-file.md)
  Sample predesigned Apple Haptic Audio Pattern files, and learn how to play your own.
- [Representing haptic patterns in AHAP files](representing-haptic-patterns-in-ahap-files.md)
  Understand the Apple Haptic and Audio Pattern (AHAP) file format.
### Game controller haptics
- [Playing Haptics on Game Controllers](playing-haptics-on-game-controllers.md)
  Add haptic feedback to supported game controllers by using Core Haptics.
### Haptic errors
- [let CoreHapticsErrorDomain: String](corehapticserrordomain.md)
  A string representation of the haptic error domain.
- [struct CHHapticError](chhapticerror.md)
  A structure that represents a framework error.
- [CHHapticError.Code](chhapticerror/code.md)
  Error codes for framework operations.
### Variables
- [let CHHapticAudioResourceKeyLoopEnabled: String](chhapticaudioresourcekeyloopenabled.md)
  A key for a Boolean value that indicates whether to loop audio playback.
- [let CHHapticAudioResourceKeyUseVolumeEnvelope: String](chhapticaudioresourcekeyusevolumeenvelope.md)
  A key for a Boolean value that indicates whether audio file playback fades in and out using an envelope.
### Type Aliases
- [typealias CHHapticAudioResourceKey](chhapticaudioresourcekey.md)
  A type alias for a key that identifies the playback behavior of an audio resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreHaptics)*