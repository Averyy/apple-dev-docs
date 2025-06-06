# CHHapticEvent

**Framework**: Core Haptics  
**Kind**: class

An object that describes a single haptic or audio event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class CHHapticEvent
```

#### Overview

Each event represents a single haptic or audio signal. The event [`type`](chhapticevent/type.md) determines whether it’s audio or haptic. Use a [`CHHapticPatternPlayer`](chhapticpatternplayer.md) object obtained through [`CHHapticEngine`](chhapticengine.md) factory methods to play events. Haptic events can be transient or continuous. Transient haptic patterns are brief impulses that occur at a specific point in time, such as the haptic feedback you feel from swiping through a picker or toggling a switch. Continuous haptic patterns, like the vibration from a ringtone, take the form of lengthier feedback over a period of time.

In the following graphic, transient haptic patterns on the left trigger at a specific time with a specific intensity. Continuous haptic patterns on the right sustain the haptic feedback over a specific duration of time, such as three seconds.

![A transient haptic pattern on the left, and a continuous haptic pattern on the right.](https://docs-assets.developer.apple.com/published/5457af395d15942b22d154ae7e7fa804/media-3235483%402x.png)

Specify when an event begins by setting its [`relativeTime`](chhapticevent/relativetime.md) property. Specify the length of the event by setting its [`duration`](chhapticevent/duration.md) property. Set optional parameters to customize event properties. For example, you can specify the intensity of a haptic event by creating an event parameter with ID [`hapticIntensity`](chhapticevent/parameterid/hapticintensity.md).

## Topics

### Categorizing Haptic Events
- [var type: CHHapticEvent.EventType](chhapticevent/type.md)
  The type of the haptic event.
- [CHHapticEvent.EventType](chhapticevent/eventtype.md)
  The types of audio and haptic event waveforms.
### Creating Haptic Events
- [init(audioResourceID: CHHapticAudioResourceID, parameters: [CHHapticEventParameter], relativeTime: TimeInterval)](chhapticevent/init(audioresourceid:parameters:relativetime:).md)
  Initializes a haptic event from a previously loaded audio resource, specifying event parameters and start time.
- [init(audioResourceID: CHHapticAudioResourceID, parameters: [CHHapticEventParameter], relativeTime: TimeInterval, duration: TimeInterval)](chhapticevent/init(audioresourceid:parameters:relativetime:duration:).md)
  Initializes a haptic event from a previously loaded audio resource, specifying event parameters, start time, and duration.
- [init(eventType: CHHapticEvent.EventType, parameters: [CHHapticEventParameter], relativeTime: TimeInterval)](chhapticevent/init(eventtype:parameters:relativetime:).md)
  Initializes a haptic event of the specified type, parameters, and start time.
- [init(eventType: CHHapticEvent.EventType, parameters: [CHHapticEventParameter], relativeTime: TimeInterval, duration: TimeInterval)](chhapticevent/init(eventtype:parameters:relativetime:duration:).md)
  Initializes a haptic event of the specified type, parameters, start time, and duration.
### Configuring Haptic Events
- [var eventParameters: [CHHapticEventParameter]](chhapticevent/eventparameters.md)
  An array of event parameters, possibly empty.
- [CHHapticEvent.ParameterID](chhapticevent/parameterid.md)
  An identifier for an event parameter.
- [var relativeTime: TimeInterval](chhapticevent/relativetime.md)
  The start time of the event, relative to other events in the same pattern.
- [var duration: TimeInterval](chhapticevent/duration.md)
  The duration of the haptic event.

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

- [Delivering Rich App Experiences with Haptics](delivering-rich-app-experiences-with-haptics.md)
  Enhance your app’s experience by incorporating haptic and sound feedback into key interactive moments.
- [Playing Collision-Based Haptic Patterns](playing-collision-based-haptic-patterns.md)
  Play a custom haptic pattern whose strength depends on an object’s collision speed.
- [Updating Continuous and Transient Haptic Parameters in Real Time](updating-continuous-and-transient-haptic-parameters-in-real-time.md)
  Generate continuous and transient haptic patterns in response to user touch.
- [class CHHapticEventParameter](chhapticeventparameter.md)
  A static parameter value that represents a single property of the haptic pattern.
- [class CHHapticDynamicParameter](chhapticdynamicparameter.md)
  A value that you send to a haptic pattern player to alter a property value during playback.
- [class CHHapticParameterCurve](chhapticparametercurve.md)
  A curve that you send to a haptic pattern player to alter a property value gradually during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent)*