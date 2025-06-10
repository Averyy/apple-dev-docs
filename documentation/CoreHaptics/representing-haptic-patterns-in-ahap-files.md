# Representing haptic patterns in AHAP files

**Framework**: Core Haptics

Understand the Apple Haptic and Audio Pattern (AHAP) file format.

#### Overview

AHAP is a JSON-like file format that specifies a haptic pattern through key-value pairs, analogous to a dictionary literal, except in a text file. You add an AHAP file to your Xcode project bundle like any other file resource, such as an audio file or an image.

![A diagram showing n’t structure of an AHAP file representing a haptic pattern.](https://docs-assets.developer.apple.com/published/ef5e2bacc8ae9eda11fc8d34ce578651/media-3261350%402x.png)

An AHAP file doesn’t need an entry for every key. When Core Haptics loads an AHAP file, it sets missing entries to their default value and clamps out-of-range values to their minimum or maximum values, whichever is closer. The framework ignores unsupported keys. Indentation of nested levels is also not required; you don’t need to indent the various subdictionaries, but doing so helps you visually distinguish the levels. You can create these files in Xcode or another text editor, like TextEdit. For several example AHAP files and guidance for playing them, see [`Playing a Custom Haptic Pattern from a File`](playing-a-custom-haptic-pattern-from-a-file.md).

This document lists the various keys and describes their effect on the resulting haptic pattern. Where applicable, this document also lists the default value for each parameter. The subsections cover keys at different levels of nesting, from top to bottom.

##### Define Patterns at the Top Level

The only top-level keys are `Pattern` and `Version`. The value for `Pattern` is an array of subdictionaries. Each AHAP file can contain a single pattern. `Version` indicates the lowest version of Core Haptics that can support loading and playing the file. Later versions, indicated by a higher version number, may contain keys that aren’t supported in older versions of the framework.

##### Build a Pattern From Events

Each pattern contains one or more events, defined by the `Event` key at the top level of the pattern dictionary. An event is a segment of the pattern with some duration and a set of properties, such as intensity or sharpness. Each event starts at its own time and can overlap other events.

You can define two other keys in the pattern dictionary:

See [`Add dynamic parameters to change the pattern during playback`](representing-haptic-patterns-in-ahap-files#Add-dynamic-parameters-to-change-the-pattern-during-playback.md) for more information on dynamic parameters, and [`Define parameter curves to automate dynamic parameter changes`](representing-haptic-patterns-in-ahap-files#Define-parameter-curves-to-automate-dynamic-parameter-changes.md) for more information on parameter curves.

##### Define Events By Their Type Start Time and Parameters

Each pattern can have several events, which can overlap. For example, an AHAP file could describe a series of transient haptics that build in intensity, with each transient represented as an event. Likewise, an AHAP file that describes audio playing alongside the haptic could consist of an event of type `AudioCustom` along with an event of type `HapticContinuous`. Each event starts at a specific time, with its own specific parameters, like haptic intensity and sharpness for haptic events, or audio volume and pitch for audio events.

`EventWaveformPath` is specific to audio events. When your app designates an audio file to play alongside a haptic, use an audio event with a waveform path and audio-specific properties:

![A diagram showing the structure of an audio event in an AHAP file.](https://docs-assets.developer.apple.com/published/47226d969747c0a2fa290b94a3402417/media-3558816%402x.png)

##### Define an Event Parameter

The `EventParameters` key leads to an array of parameter subdictionaries. Each parameter describes one property of the event, like its haptic intensity or haptic sharpness. All parameters are optional. If you don’t include a parameter, the Core Haptics engine assumes its default value for that event.

##### Specify the Parameter By Id

Each parameter has a `ParameterID` string and an associated value. The range of possible values may vary from parameter to parameter.

> **Note**:  A value of 0 doesn’t mean that the parameter has no effect, or that the absolute value of the parameter is zero. It’s a normalized value that maps to the minimum value the system supports. Likewise, a value of 1 doesn’t indicate 1 second; rather, it maps to the maximum supported value.

##### Add Dynamic Parameters to Change the Pattern During Playback

Like event parameters, each dynamic parameter has a `ParameterID` string and an associated value. Unlike event parameters, dynamic parameters affect the entire pattern, across all events. You indicate a dynamic parameter in the AHAP file with an entry labeled `Parameter` at the same level as `Event`.

##### Define Parameter Curves to Automate Dynamic Parameter Changes

Like dynamic parameters, parameter curves change the parameter values of the haptic pattern during its playback. Unlike with dynamic parameters, the changes are scheduled over time, and each value transitions to the next one linearly. You indicate a parameter curve in the AHAP file with an entry labeled `ParameterCurve` at the same level as `Event`. Parameter curves modify the same parameters as dynamic parameters modify, and they share all of the same `ParameterID` strings.

For more information about parameter curves, see [`CHHapticParameterCurve`](chhapticparametercurve.md).

## See Also

- [Playing a Custom Haptic Pattern from a File](playing-a-custom-haptic-pattern-from-a-file.md)
  Sample predesigned Apple Haptic Audio Pattern files, and learn how to play your own.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/representing-haptic-patterns-in-ahap-files)*