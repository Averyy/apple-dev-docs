# CHHapticPattern

**Framework**: Core Haptics  
**Kind**: class

An object representing a haptic waveform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class CHHapticPattern
```

## Mentions

- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)

#### Overview

A haptic pattern represents the waveform of a haptic through a hierarchical set of key-value pairs, starting at the topmost level with a [`CHHapticPattern.Key`](chhapticpattern/key.md). This key marks the beginning of an array of events and [`parameterID`](chhapticpattern/key/parameterid.md) definitions. Each event has an associated time that indicates when the system delivers the event to the haptic engine.

![A diagram showing the contents of a pattern: its keys, values, and subdictionaries.](https://docs-assets.developer.apple.com/published/34fa249208e0ab093d6f9cc9a6c29417/media-3163328%402x.png)

These key-value pairs represent not only events constituting the pattern, but also individual parameters of each event, which are characteristics of the haptic, such as sharpness and intensity. More complicated patterns also contain key-value pairs for parameter curves, which you can use to modulate parameters over time.

##### Haptic Patterns

To add haptics to your app, you create an instance of [`CHHapticEngine`](chhapticengine.md), load a pattern, and use the engine to create a player to play that pattern. You create a pattern in one of three ways:

- . Each entry in the dictionary defines a single characteristic of the haptic, like its intensity, start time, or duration. See [`Playing a single-tap haptic pattern`](playing-a-single-tap-haptic-pattern.md) to learn more about creating a dictionary inline.
- . The [`CHHapticEvent`](chhapticevent.md) class represents a haptic event as an object in code. The key-value pairs in a dictionary correspond to the properties and parameters associated with a [`CHHapticEvent`](chhapticevent.md). Haptic event objects are just another representation of the haptics dictionary.
- . This JSON-compliant file format specifies a haptic pattern through key-value pairs, analogous to a dictionary literal, except in a text file. Add this file to your Xcode project bundle.

You can produce the same kind of content with all forms of pattern creation.

##### Haptic Intensity and Sharpness

Regardless of the building block you choose to generate a custom haptic, you can control its intensity and sharpness. Intensity varies the haptic’s amplitude or strength. Sharpness lets you determine the character of the haptic experience. For example, you can use sharpness values to convey an experience that’s crisp, precise, and mechanical, or one that’s soft, rounded, and organic.

## Topics

### Creating a Haptic Pattern
- [init(contentsOf: URL) throws](chhapticpattern/init(contentsof:).md)
  Creates a haptic pattern with the contents of an AHAP file.
- [init(events: [CHHapticEvent], parameterCurves: [CHHapticParameterCurve]) throws](chhapticpattern/init(events:parametercurves:).md)
  Constructs a haptic pattern from a series of events and parameter curves.
- [init(events: [CHHapticEvent], parameters: [CHHapticDynamicParameter]) throws](chhapticpattern/init(events:parameters:).md)
  Constructs a haptic pattern from a series of events and parameters.
- [init(dictionary: [CHHapticPattern.Key : Any]) throws](chhapticpattern/init(dictionary:).md)
  Creates a haptic pattern from a property list dictionary.
- [CHHapticPattern.Key](chhapticpattern/key.md)
  Constants that define the keys you use to create a haptic pattern dictionary.
### Retrieving Haptic Pattern Duration
- [var duration: TimeInterval](chhapticpattern/duration.md)
  The duration of the haptic pattern, in seconds.
### Exporting a Haptic Pattern
- [func exportDictionary() throws -> [CHHapticPattern.Key : Any]](chhapticpattern/exportdictionary.md)
  Returns the dictionary representation of the haptic pattern.

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
- [class CHHapticEngine](chhapticengine.md)
  An object that represents the connection to the haptic server.
- [protocol CHHapticPatternPlayer](chhapticpatternplayer.md)
  A protocol that defines a standard pattern player capable of playing haptic patterns with fixed parameters.
- [protocol CHHapticAdvancedPatternPlayer](chhapticadvancedpatternplayer.md)
  A protocol that defines an advanced pattern player capable of looping, seeking, pausing, and resuming haptic playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpattern)*