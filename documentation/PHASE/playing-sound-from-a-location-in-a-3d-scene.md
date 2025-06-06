# Playing sound from a location in a 3D scene

**Framework**: PHASE

Position sound from a specific direction and automatically raise or lower volume based on the environment.

#### Overview

Audio that adjusts its volume based on distance to a specific reference point is called . Spatial audio transmits sound from a particular location, or source, in a specific direction that you define by describing the sound’s 3D position and orientation. Your app can leverage spatial audio to define the point of reference, or define a listener as a player in a game. For example, to indicate that a horn resides on the left-hand side of a scene, PHASE outputs audio more through the left speaker.

PHASE spatial audio accommodates a scene layout in several ways: by observing objects in the scene, the shape of the sound’s source, obstructions, and the point of reference of a listener. To complement obstacles and indoor locations in your scene, you can use spatial audio to layer environmental effects, for example, a reflection or reverberation, on top of spatial sounds.

After describing your app’s scene, you queue sound to play by creating an event node asset that instructs PHASE on what to play and when. At runtime, PHASE checks your app’s state through the event node asset and plays sounds at the right moment that react in accordance to your app’s visual appearance.

##### Set an Objects Scene Position and Orientation

Before PHASE plays sound in 3D, you create several objects to model your app’s visual scene. Initialize and add the following classes to [`rootObject`](phaseengine/rootobject.md), the engine’s root object:

- [`PHASESource`](phasesource.md) for sound sources
- [`PHASEListener`](phaselistener.md) for a listener
- [`PHASEOccluder`](phaseoccluder.md) for optional occluders

Each class derives from [`PHASEObject`](phaseobject.md), which defines a transform to provide it with a unique 3D position and orientation in the scene.

An app can define the scene as a level in a game that’s composed of a detailed set of visual properties, for example, textured pixel data, lighting, and animation. However, to play sound in accordance with the visual scene, PHASE only needs to know the scene’s geometric shape. PHASE interprets the shape through a tranform (of type [`simd_float4x4`](https://developer.apple.com/documentation/simd/simd_float4x4)), and in particular, its array of four-column vectors. The following transform defines a zeroed orientation and position for a board-game piece:

```swift
var chessPiecePose: simd_float4x4 = matrix_identity_float4x4
```

##### Define the Location From Which Sound Plays

The first type of object you define in the PHASE scene describes a location from which sound originates, such as a chess piece that makes a shuffling noise as it slides to a location on the board. A source emanates sound from a single point in space, or a . To produce sound at a point in the scene, create a [`PHASESource`](phasesource.md) with the engine parameter, for example:

```swift
let chessPiecePointSource = PHASESource(engine: engine)
```

Then, add the source to the scene by handing it to the engine. You can add an object as a child to any other object by calling [`addChild(_:)`](phaseobject/addchild(_:).md) on the parent. The result models a scene as a connected graph of objects, or an . The following code adds the chess piece as child of the engine’s root:

```swift
do { try engine.rootObject.addChild(chessPiecePointSource) } 
catch { print ("Failed to add a child object to the scene.") }
```

PHASE interprets object positions in the coordinate space of the parent, which for the root object is the coordinate space of the scene, or the  space. Set an object’s position by assigning the transform’s first three elements of the last column. The following code sets a chess piece’s position to `(0,0,-6)`, which is 6 meters in front of the world origin `(0,0,0)`:

```swift
chessPiecePose.columns.3.z -= 6.0
chessPiecePointSource.transform = chessPiecePose
```

> 💡 **Tip**:  Set the [`unitsPerMeter`](phaseengine/unitspermeter.md) parameter to instruct PHASE to interpret [`transform`](phaseobject/transform.md) values in your app’s preferred unit of measurement.

 Set the [`unitsPerMeter`](phaseengine/unitspermeter.md) parameter to instruct PHASE to interpret [`transform`](phaseobject/transform.md) values in your app’s preferred unit of measurement.

##### Originate Sound From a Geometric Area

For spatial sounds, the framework requires a 3D position from which the sound originates. To emanate sound from an area larger than a point, for example, the full length of an electric fence in a game, describe the region by configuring a [`PHASEShape`](phaseshape.md) object. The following code models a fence by using a [`Model I/O`](https://developer.apple.com/documentation/ModelIO) plane:

```swift
let fenceMesh = MDLMesh(
   planeWithExtent: vector3(0.1, 0.1, 0.1), 
   segments: vector2(1, 1), 
   geometryType: .triangles, 
   allocator: nil)

let fenceShape = PHASEShape(engine: engine, mesh: fenceMesh)
let volumetricFenceSource = PHASESource(engine: engine, shapes: [fenceShape])

do { try engine.rootObject.addChild(volumetricFenceSource) } 
catch { print ("Failed to add a child object to the scene.") }
```

> **Note**:  You can supply high-resolution geometry to a [`PHASESource`](phasesource.md). For collision detection, games usually supply a low-resolution approximation that contains a detailed visual asset to maximize runtime performance. However, [`PHASEShape`](phaseshape.md) supports geometry of any resolution with little performance impact.

 You can supply high-resolution geometry to a [`PHASESource`](phasesource.md). For collision detection, games usually supply a low-resolution approximation that contains a detailed visual asset to maximize runtime performance. However, [`PHASEShape`](phaseshape.md) supports geometry of any resolution with little performance impact.

##### Create an Object That Hears Sound

A [`PHASEListener`](phaselistener.md) is an object within an app that hears sound; it’s the central position and orientation at which the user experiences spatial audio. The framework adjusts the volume of a sound source based on its unique position and orientation with respect to the listener. For example, a sound that plays far off in the distance from the listener plays quietly, and a closer sound plays more loudly. The following code creates a listener and defines its position and orientation in the scene:

```swift
let origin: simd_float4x4 = matrix_identity_float4x4
let listener = PHASEListener(engine: engine)
listener.transform = origin
```

Add the listener to the scene by inserting it into the object hierarchy. The following code adds the listener as a child of the engine’s root object:

```swift
do { try engine.rootObject.addChild(listener) } 
catch { print ("Failed to add child object to the scene.") }
```

##### Set Up Occluder Options for Obstructed Sound

The framework lowers the volume of a sound source when an obstacle blocks its path to the listener. The result creates a realistic effect in cases where, for example, the player takes cover behind a gallery pillar, which reduces the volume of commotion from the other side of the room.

To define an obstacle, create a [`PHASEOccluder`](phaseoccluder.md) with a shape and position that matches the pillar’s visual counterpart. The following code defines an occluder’s geometric shape using [`Model I/O`](https://developer.apple.com/documentation/ModelIO):

```swift
defaultOccluderSize: Float = 1.0

let pillarOccluderMesh = MDLMesh.newCylinder(withHeight: 10.0, 
    radii: vector_float2(defaultOccluderSize, defaultOccluderSize), 
    radialSegments: 9, 
    verticalSegments: 1, 
    geometryType: MDLGeometryType.triangles, 
    inwardNormals: false, 
    allocator: nil)
```

You can tweak the reflectivity of a particular occluder by choosing a physical material that makes up the occluder. The material you choose implements a blend between how much an occluder reflects sound and how much sound passes through it. To select a material, pass its corresponding preset, [`PHASEMaterialPreset`](phasematerialpreset.md), into a new [`PHASEMaterial`](phasematerial.md) object:

```swift
let occluderMaterial = PHASEMaterial(engine: engine, preset: .concrete)
let occluderShape = PHASEShape(engine: engine,
   mesh: pillarOccluderMesh,
   materials: [occluderMaterial])

let occluder = PHASEOccluder(engine: engine,
   shapes: [occluderShape])
```

Position an occluder in the scene by setting its [`transform`](phaseobject/transform.md). The following code places an occluder midway between the source and listener by dividing the custom `defaultSourceDistance` variable by two:

```swift
let defaultSourceDistance: Float = 10.0

var occluderTransform: simd_float4x4 = origin
occluderTransform.columns.3.z -= defaultSourceDistance / 2.0
occluder.transform = occluderTransform
```

Activate the occluder by adding it into the scene. The following code adds the occluder as a child of the root object:

```swift
do { try engine.rootObject.addChild(occluder) } 
catch { print ("Failed to add a child object to the scene.") }
```

##### Describe the Output Pipeline

As one of the final stages in audio playback configuration, the app specifies the particular object, or , that combines in-flight audio signals for transmission to the output device. For spatial audio, the app creates a spatial mixer, [`PHASESpatialMixerDefinition`](phasespatialmixerdefinition.md). The following code defines a spatial mixer for two sources:

```swift
let chessPieceSpatialMixer = PHASESpatialMixerDefinition(
    spatialPipeline: PHASESpatialPipeline(
        flags: .directPathTransmission)!)

let fenceSpatialMixer = PHASESpatialMixerDefinition(
    spatialPipeline: PHASESpatialPipeline(
        flags: .directPathTransmission)!)
```

The spatial mixer can add environmental layers to the output, such as reflections or reverb, by including the [`earlyReflections`](phasespatialpipeline/flags-swift.struct/earlyreflections.md) or [`lateReverb`](phasespatialpipeline/flags-swift.struct/latereverb.md) cases, in addition to [`directPathTransmission`](phasespatialpipeline/flags-swift.struct/directpathtransmission.md), to the `flags` argument.

##### Adjust Volume Based on Distance

PHASE attenuates sound over the distance between a source and a listener by observing the distance model you define on the spatial mixer. As a source emits sound, the spatial mixer adjusts its volume based on the distance from the listener. The farther away the source is from the listener, the more the volume attenuates and the quieter the sound gets with respect to the listener.

> ❗ **Important**:  Without a distance model, the spatial mixer plays sound at a constant level, disregarding the distance between the source and the listener.

 Without a distance model, the spatial mixer plays sound at a constant level, disregarding the distance between the source and the listener.

For more information about distance modeling and its various types,  and , see [`Spatial Mixing`](spatial-mixing.md).

[`PHASEGeometricSpreadingDistanceModelParameters`](phasegeometricspreadingdistancemodelparameters.md) is a model that simulates sound loss over distance realistically. The distance model [`rolloffFactor`](phasegeometricspreadingdistancemodelparameters/rollofffactor.md) emphasizes or deemphasizes this model. At `1.0`, sound that emanates between the source and listener loses 6 dB every time distance doubles. At `2.0`, the loss doubles. At `0.5`, the loss halves, and so on. The following code defines a geometric spatial model for the scene’s spatial mixers:

```swift
let simpleModel = PHASEGeometricSpreadingDistanceModelParameters()
simpleModel.rolloffFactor = 1.0

chessPieceSpatialMixer.distanceModelParameters = simpleModel
fenceSpatialMixer.distanceModelParameters = simpleModel
```

##### Generate a Sound Event

When PHASE understands the layout and configuration of the scene, sound reacts in accordance when your app plays a sound event by using [`PHASESoundEvent`](phasesoundevent.md). You generate a sound event from a sound-event node that describes your particular playback needs.

First, identify the sound assets for your sound events and register them with the engine’s asset registry. The following code loads two files bundled with the project titled “shuffling.wav” and “buzzing.wav”:

```swift
let shufflingSoundUrl = Bundle.main.url(forResource: "shuffling", withExtension: "wav")!
var shufflingSoundAsset:PHASESoundAsset!
do {
    shufflingSoundAsset = try engine.assetRegistry.registerSoundAsset(
    url: shufflingSoundUrl,
    identifier: "shufflingSound",
    assetType: PHASEAsset.AssetType.resident,
    channelLayout: nil,
    normalizationMode: .dynamic)
} catch {
    print("Failed to register the sound asset.")
}

let buzzingSoundUrl = Bundle.main.url(forResource: "buzzing", withExtension: "wav")!
var electricBuzzingSoundAsset:PHASESoundAsset!
do {
    electricBuzzingSoundAsset = try engine!.assetRegistry.registerSoundAsset(
    url: buzzingSoundUrl,
    identifier: "buzzingSound",
    assetType: .resident,
    channelLayout: nil,
    normalizationMode: .dynamic)
} catch {
    print("Failed to register the sound asset.")
}
```

The following code creates sampler nodes for both the shuffling chess piece and electrified fence:

```swift
// Define the shuffling chess piece one-shot sound.
let shufflingSamplerNode = PHASESamplerNodeDefinition(
    soundAssetIdentifier: shufflingSoundAsset.identifier,
    mixerDefinition: chessPieceSpatialMixer,
    identifier: shufflingSoundAsset.identifier + "_SamplerNode")

shufflingSamplerNode.playbackMode = .oneShot

// Define the buzzing electric fence looping sound.
let electricBuzzingSamplerNode = PHASESamplerNodeDefinition(
    soundAssetIdentifier: electricBuzzingSoundAsset.identifier,
    mixerDefinition: fenceSpatialMixer,
    identifier: electricBuzzingSoundAsset.identifier + "_SamplerNode")

electricBuzzingSamplerNode.playbackMode = .looping
```

Give PHASE information about the sound-event nodes by registering their assets with the engine:

```swift
var shufflingSoundEventAsset: PHASESoundEventNodeAsset!
do { shufflingSoundEventAsset = try 
    engine.assetRegistry.registerSoundEventAsset(  
    rootNode: shufflingSamplerNode,
    identifier: shufflingSoundAsset.identifier + "_SoundEventAsset")
} catch { print("Failed to register a sound event asset.") } 

var buzzingSoundEventAsset: PHASESoundEventNodeAsset!
do { buzzingSoundEventAsset = try 
    engine.assetRegistry.registerSoundEventAsset(  
    rootNode: electricBuzzingSamplerNode,
    identifier: electricBuzzingSoundAsset.identifier + "_SoundEventAsset")
} catch { print("Failed to register a sound event asset.") }
```

Define which sound source plays the audio and the listener that hears it by configuring a [`PHASEMixerParameters`](phasemixerparameters.md) object for each spatial mixer:

```swift
let chessPieceSpatialMixerParams = PHASEMixerParameters()
chessPieceSpatialMixerParams.addSpatialMixerParameters(
    identifier: chessPieceSpatialMixer.identifier,
    source: chessPiecePointSource,
    listener: listener)

let fenceSpatialMixerParams = PHASEMixerParameters()
fenceSpatialMixerParams.addSpatialMixerParameters(
    identifier: fenceSpatialMixer.identifier,
    source: volumetricFenceSource,
    listener: listener)
```

To play the sounds, generate a [`PHASESoundEvent`](phasesoundevent.md) instance for each node and call [`start(completion:)`](phasesoundevent/start(completion:).md) on the sound event. Associate the source to the sound event by passing its `spatialMixerParams` through the [`PHASESoundEvent`](phasesoundevent.md) initializer `mixerParameters` argument:

```swift
let buzzingSoundEvent = try! PHASESoundEvent(engine: engine,
    assetIdentifier: buzzingSoundEventAsset.identifier,
    mixerParameters: fenceSpatialMixerParams)

buzzingSoundEvent.start(completion: nil)

let shufflingSoundEvent = try! PHASESoundEvent(engine: engine,
    assetIdentifier: shufflingSoundEventAsset.identifier,
    mixerParameters: chessPieceSpatialMixerParams)

shufflingSoundEvent.start(completion: nil)
```

Because `electricBuzzingSamplerNode` and `shufflingSamplerNode` have no children, both `buzzingSoundEventAsset` and `shufflingSoundEventAsset` contain a node hierarchy of only one node. When the app invokes a sound event from these assets, the same audio plays consistently.

> 💡 **Tip**:  You can create a more sophisticated node hiearchy that plays different sounds based on your app’s state. By adding multiple nodes that sample varying audio as children to a control node, PHASE plays the right audio for the moment based on control logic that you define. For more information, see Audio Selection and Playback.

 You can create a more sophisticated node hiearchy that plays different sounds based on your app’s state. By adding multiple nodes that sample varying audio as children to a control node, PHASE plays the right audio for the moment based on control logic that you define. For more information, see Audio Selection and Playback.

## See Also

- [Personalizing spatial audio in your app](personalizing-spatial-audio-in-your-app.md)
  Enhance the realism of spatial audio output by tracking a person’s head movement and accounting for their personal spatial audio profile.
- [PHASE updates](../Updates/PHASE.md)
  Learn about important changes to PHASE.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/playing-sound-from-a-location-in-a-3d-scene)*