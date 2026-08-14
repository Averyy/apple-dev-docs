# Representing haptic patterns in AHAP files

**Framework**: Core Haptics

Understand the Apple Haptic and Audio Pattern (AHAP) file format.

#### Overview

AHAP is a JSON-like file format that specifies a haptic pattern through key-value pairs, analogous to a dictionary literal, except in a text file. You add an AHAP file to your Xcode project bundle like any other file resource, such as an audio file or an image.

![A diagram showing n’t structure of an AHAP file representing a haptic pattern.](/images/com.apple.corehaptics/media-3261350@2x.png)

An AHAP file doesn’t need an entry for every key. When Core Haptics loads an AHAP file, it sets missing entries to their default value and clamps out-of-range values to their minimum or maximum values, whichever is closer. The framework ignores unsupported keys. Indentation of nested levels is also not required; you don’t need to indent the various subdictionaries, but doing so helps you visually distinguish the levels. You can create these files in Xcode or another text editor, like TextEdit. For several example AHAP files and guidance for playing them, see [`Playing a Custom Haptic Pattern from a File`](playing-a-custom-haptic-pattern-from-a-file.md).

This document lists the various keys and describes their effect on the resulting haptic pattern. Where applicable, this document also lists the default value for each parameter. The subsections cover keys at different levels of nesting, from top to bottom.

##### Define Patterns at the Top Level

The only top-level keys are `Pattern` and `Version`. The value for `Pattern` is an array of subdictionaries. Each AHAP file can contain a single pattern. `Version` indicates the lowest version of Core Haptics that can support loading and playing the file. Later versions, indicated by a higher version number, may contain keys that aren’t supported in older versions of the framework.

- **`Pattern`**: Array of `Event` dictionaries representing a segment of the haptic to play.
- **`Version`**: The Core Haptics version that supports the file.

##### Build a Pattern From Events

Each pattern contains one or more events, defined by the `Event` key at the top level of the pattern dictionary. An event is a segment of the pattern with some duration and a set of properties, such as intensity or sharpness. Each event starts at its own time and can overlap other events.

- **`Event`**: Dictionary of event type, start time, duration, and optional event parameters.

You can define two other keys in the pattern dictionary:

- **`Parameter`**: A key in the pattern dictionary that you use to define a dynamic parameter.
- **`ParameterCurve`**: A key in the pattern dictionary that you use to define a parameter curve.

See [`Add dynamic parameters to change the pattern during playback`](representing-haptic-patterns-in-ahap-files#Add-dynamic-parameters-to-change-the-pattern-during-playback.md) for more information on dynamic parameters, and [`Define parameter curves to automate dynamic parameter changes`](representing-haptic-patterns-in-ahap-files#Define-parameter-curves-to-automate-dynamic-parameter-changes.md) for more information on parameter curves.

##### Define Events By Their Type Start Time and Parameters

Each pattern can have several events, which can overlap. For example, an AHAP file could describe a series of transient haptics that build in intensity, with each transient represented as an event. Likewise, an AHAP file that describes audio playing alongside the haptic could consist of an event of type `AudioCustom` along with an event of type `HapticContinuous`. Each event starts at a specific time, with its own specific parameters, like haptic intensity and sharpness for haptic events, or audio volume and pitch for audio events.

- **`EventType`**: The type of event described in the subdictionary, corresponding to its [`CHHapticEvent.EventType`](chhapticevent/eventtype.md) object. This string determines whether the pattern is a `HapticTransient`, `HapticContinuous`, `AudioContinuous`, or `AudioCustom` pattern.
- **`Time`**: The floating-point start time, relative to the beginning of the pattern.
- **`Duration`**: The floating-point duration of the pattern.
- **`EventParameters`**: An array of parameter dictionaries, each with `ParameterID` and `Value`.
- **`EventWaveformPath`**: The path string for the custom audio file, relative to the top of your bundle, such as `MyAudioContent/Explosion.caf` or its direct filename.

`EventWaveformPath` is specific to audio events. When your app designates an audio file to play alongside a haptic, use an audio event with a waveform path and audio-specific properties:

![A diagram showing the structure of an audio event in an AHAP file.](/images/com.apple.corehaptics/media-3558816@2x.png)

##### Define an Event Parameter

The `EventParameters` key leads to an array of parameter subdictionaries. Each parameter describes one property of the event, like its haptic intensity or haptic sharpness. All parameters are optional. If you don’t include a parameter, the Core Haptics engine assumes its default value for that event.

- **`ParameterID`**: A [`CHHapticEvent.ParameterID`](chhapticevent/parameterid.md) string constant that indicates the type of parameter being defined.
- **`ParameterValue`**: The numeric value of the associated parameter. These values are normalized to a range between 0 and 1 to represent the minimum and maximum the system supports.

##### Specify the Parameter By Id

Each parameter has a `ParameterID` string and an associated value. The range of possible values may vary from parameter to parameter.

- **`HapticIntensity`**: The strength of the haptic event. The value is between 0 and 1.
- **`HapticSharpness`**: The degree to which the haptic event feels tingly, or persistent. The value is between 0 and 1.
- **`AttackTime`**: The amount of time it takes for the event’s intensity envelope to reach its full strength. The value is between 0 and 1.
- **`DecayTime`**: The amount of time it takes for the event’s intensity envelope to reach zero. The value is between 0 and 1. This applies only to events without sustained envelopes.
- **`ReleaseTime`**: The amount of time it takes for a sustained intensity envelope to reach zero after the event finishes. The value is between 0 and 1.
- **`Sustained`**: A value of 1 to indicate a sustained intensity envelope, or 0 to indicate an unsustained intensity envelope.
- **`AudioBrightness`**: The high-frequency content of the sound. This value is between 0 and 1.
- **`AudioPan`**: The distribution of the audio signal. This value is between -1 and 1.
- **`AudioPitch`**: The pitch of the audio signal. This value is between -1 and 1.
- **`AudioVolume`**: The volume or loudness of the sound. This value is between 0 and 1.

> **Note**:  A value of 0 doesn’t mean that the parameter has no effect, or that the absolute value of the parameter is zero. It’s a normalized value that maps to the minimum value the system supports. Likewise, a value of 1 doesn’t indicate 1 second; rather, it maps to the maximum supported value.

##### Add Dynamic Parameters to Change the Pattern During Playback

Like event parameters, each dynamic parameter has a `ParameterID` string and an associated value. Unlike event parameters, dynamic parameters affect the entire pattern, across all events. You indicate a dynamic parameter in the AHAP file with an entry labeled `Parameter` at the same level as `Event`.

- **`HapticIntensityControl`**: The factor by which to modulate the intensity of the haptic. The value is between 0 and 1 and is applied multiplicatively.
- **`HapticSharpnessControl`**: The amount by which to increase or decrease the sharpness of the haptic. The value is between -1 and 1. This dynamic parameter affects only continuous haptics and is applied additively.
- **`HapticAttackTimeControl`**: The amount by which to increase or decrease the attack time of the haptic pattern’s events. The value is between -1 and 1 and is applied additively.
- **`HapticDecayTimeControl`**: The amount by which to increase or decrease the decay time of the haptic pattern’s events. The value is between -1 and 1 and is applied additively.
- **`HapticReleaseTimeControl`**: The amount by which to increase or decrease the release time of the haptic pattern’s events. The value is between -1 and 1 and is applied additively.
- **`AudioBrightnessControl`**: The factor by which to increase or decrease the audio brightness (high-frequency content) of the sound. The value is between -1 and 1 and is applied additively.
- **`AudioPanControl`**: The amount by which to increase or decrease the audio signal’s pan. The value is between -1 and 1 and is applied additively.
- **`AudioPitchControl`**: The amount by which to increase or decrease the audio signal’s pitch. The value is between -1 and 1 and is applied additively.
- **`AudioVolumeControl`**: The factor by which to modulate the volume of the sound. The value is between 0 and 1 and is applied multiplicatively.
- **`AudioAttackTimeControl`**: The amount by which to increase or decrease the attack time of the audio pattern’s events. The value is between -1 and 1 and is applied additively.
- **`AudioDecayTimeControl`**: The amount by which to increase or decrease the decay time of the audio pattern’s event. The value is between -1 and 1 and is applied additively.
- **`AudioReleaseTimeControl`**: The amount by which to increase or decrease the release time of the audio pattern’s event. The value is between -1 and 1 and is applied additively.

##### Define Parameter Curves to Automate Dynamic Parameter Changes

Like dynamic parameters, parameter curves change the parameter values of the haptic pattern during its playback. Unlike with dynamic parameters, the changes are scheduled over time, and each value transitions to the next one linearly. You indicate a parameter curve in the AHAP file with an entry labeled `ParameterCurve` at the same level as `Event`. Parameter curves modify the same parameters as dynamic parameters modify, and they share all of the same `ParameterID` strings.

- **`ParameterID`**: A string constant that indicates the parameter that the curve changes.
- **`Time`**: The time at which to begin applying the parameter curve.
- **`ParameterCurveControlPoints`**: Control points that define the shape of the curve. Each point takes the form (*time*, *value*). Time is relative to the start of the curve.

For more information about parameter curves, see [`CHHapticParameterCurve`](chhapticparametercurve.md).

## See Also

- [Playing a Custom Haptic Pattern from a File](playing-a-custom-haptic-pattern-from-a-file.md)
  Sample predesigned Apple Haptic Audio Pattern files, and learn how to play your own.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/representing-haptic-patterns-in-ahap-files)*