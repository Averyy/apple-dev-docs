# PHASEEngine

**Framework**: PHASE  
**Kind**: class

An object that manages audio assets, controls playback, and configures environmental effects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEEngine
```

#### Overview

Before using PHASE, an app creates an instance of this object. Apps access all of the framework’s functionality through engine functions or properties, or through other PHASE classes into which you pass the engine object.

> ❗ **Important**:  You can create multiple engine instances, but normally, apps create only one.

 You can create multiple engine instances, but normally, apps create only one.

##### Create and Start the Engine

To create an engine object, choose a value for the [`init(updateMode:)`](phaseengine/init(updatemode:).md) argument that selects the desired control over scene setup and playback timing.

```swift
// Apps that need precise audio synchronization and 
// synchronized dynamic mix control pass in `.manual`.
engine = PHASEEngine(updateMode: .automatic) 
```

Then, load your sound assets, sound event assets, and shapes for sound occlusion. Before your app attempts to play sounds, start the engine object.

```swift
do { try engine.start() } 
catch { /* Handle the error. */ }
```

To stop audio playback and enable the engine to deallocate system resources, call the [`stop()`](phaseengine/stop().md) function.

```swift
engine.stop()
```

## Topics

### Creating an Engine
- [init(updateMode: PHASEEngine.UpdateMode)](phaseengine/init(updatemode:).md)
  Creates an engine updated by the app or framework.
- [PHASEEngine.UpdateMode](phaseengine/updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
### Registering Audio Resources
- [var assetRegistry: PHASEAssetRegistry](phaseengine/assetregistry.md)
  An object that loads and unloads audio resources.
### Accessing Scene Hierarchy
- [var rootObject: PHASEObject](phaseengine/rootobject.md)
  The main object to which the app adds child objects.
### Defining Environmental Effects
- [var defaultReverbPreset: PHASEReverbPreset](phaseengine/defaultreverbpreset.md)
  The environmental surroundings that determine how sound resonates.
- [var defaultMedium: PHASEMedium](phaseengine/defaultmedium.md)
  The physical matter through which sound travels.
- [var outputSpatializationMode: PHASESpatializationMode](phaseengine/outputspatializationmode.md)
  The mode the engine implements to create a 3D sound experience.
### Controlling and Inspecting Playback State
- [func pause()](phaseengine/pause.md)
  Pauses all audio playback.
- [func start() throws](phaseengine/start.md)
  Starts or resumes all audio playback.
- [func stop()](phaseengine/stop.md)
  Stops all audio playback.
- [func update()](phaseengine/update.md)
  Processes app commands and increments framework processing.
- [var renderingState: PHASESoundEvent.RenderingState](phaseengine/renderingstate.md)
  The status of the engine’s audio playback.
### Managing Groups of Sounds
- [var groups: [String : PHASEGroup]](phaseengine/groups.md)
  A list of named groups that contain sounds the app operates on collectively.
- [var activeGroupPreset: PHASEGroupPreset?](phaseengine/activegrouppreset.md)
  The settings that define playback for a group of sounds.
- [var duckers: [PHASEDucker]](phaseengine/duckers.md)
  An array of objects that reduce the volume of simultaneously playing sounds.
### Accessing In-Flight Audio
- [var soundEvents: [PHASESoundEvent]](phaseengine/soundevents.md)
  A collection of the sounds that play under various runtime circumstances.
### Measuring Units
- [var unitsPerMeter: Double](phaseengine/unitspermeter.md)
  A conversion factor from meters to your app’s preferred unit of measurement.
- [var unitsPerSecond: Double](phaseengine/unitspersecond.md)
  A conversion factor from seconds to your app’s preferred unit of time.

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

- [PHASEEngine.UpdateMode](phaseengine/updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [class PHASEAssetRegistry](phaseassetregistry.md)
  A central repository of audio assets.
- [enum PHASENormalizationMode](phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASESpatializationMode](phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine)*