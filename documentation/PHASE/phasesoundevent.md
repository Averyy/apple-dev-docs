# PHASESoundEvent

**Framework**: PHASE  
**Kind**: class

An object that determines which audio to play.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESoundEvent
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

A sound event represents a logic tree, or hierarchy, that defines what, when, and how the framework plays a sound at runtime. You configure the tree with conditions based on your app’s state. When you invoke a sound event’s root node at runtime, the framework navigates the tree by branching based on the logic, landing on a playable node that sends the right audio to the output device:

- To invoke a specific one-time sound, create a sound event from a single sampler node.
- To invoke a sound event that tailors its sound based on your app’s state, define a sound event hierarchy containing one or more control nodes; see [`Sound Event Nodes`](sound-event-nodes.md). For example, to play either footsteps or a jumping noise depending on the hero’s state, you configure a switch node that navigates based on the hero’s hypothetical `isJumping` metaparameter.

For sound event nodes that play audio, the asset’s [`playbackMode`](phasesamplernodedefinition/playbackmode.md) determines whether the audio loops. One-time sound events stop automatically at the end of the audio data. Looping sound events (those with [`playbackMode`](phasesamplernodedefinition/playbackmode.md) `=` [`PHASEPlaybackMode.looping`](phaseplaybackmode/looping.md)) require you to explicitly call [`stopAndInvalidate()`](phasesoundevent/stopandinvalidate().md) to stop the audio.

##### Playing a One Shot Channel Based Sound

Apps create a sound event by requesting one from a sound event node asset. To create a sound event node asset, combine a sound asset (the source audio data) with a mixer object (which combines sound layers for output) to create a node, and add the node to the asset registry. By creating a sound event from a sampler node ([`PHASESamplerNodeDefinition`](phasesamplernodedefinition.md)), the following code plays an audio file once before discarding it.

```swift
// Create a channel layout for audio types that contain no channel metadata. 
let stereoLayout = AVAudioChannelLayout(layoutTag: kAudioChannelLayoutTag_Stereo)    

// Load an audio file from the bundle.
let bangSoundURL = Bundle.main.url(forResource: "bangSound", withExtension: "wav")!

// Create and register a sound asset.
var bangSoundAsset:PHASESoundAsset!
do { 
    bangSoundAsset = try engine.assetRegistry.registerSoundAsset(
        url: bangSoundURL, 
        identifier: "bangSound", 
        assetType: .resident, 
        channelLayout: stereoLayout,
        normalizationMode: .dynamic)
} catch { print("Failed to register the sound asset.") }

// Create a mixer that routes sound directly to the output.
let stereoMixer = PHASEChannelMixerDefinition(channelLayout:stereoLayout!)

// Create a sound event node.
let bangSoundSamplerNode = PHASESamplerNodeDefinition(
    soundAssetIdentifier: bangSoundAsset.identifier, 
    mixerDefinition: stereoMixer, identifier:"bangSoundNode")

// Add the sound event node to the asset registry and retrieve the asset object.
var bangSoundSoundEventAsset: PHASESoundEventNodeAsset! 
do {
    bangSoundEventAsset = try engine.assetRegistry.registerSoundEventAsset(
        rootNode: bangSoundSamplerNode, identifier:"bangSoundTree")
} catch { print ("Failed to register the sound event node.") }
```

The resulting node asset represents a template for audio that’s ready for playback. To play the audio, spawn a sound event off of the node asset and call [`start(completion:)`](phasesoundevent/start(completion:).md) to invoke the sound event.

```swift
// Create a playable sound event from the template sound event asset.
var bangSoundEvent: PHASESoundEvent!
do {
        bangSoundEvent = try PHASESoundEvent(engine:engine, 
        assetIdentifier: bangSoundEventAsset.identifier)
} catch { print ("Failed to create the sound event.") }

// Play the one-shot sound event.
bangSoundEvent.start()
```

> ❗ **Important**:  To play the same sound asset again, create another sound event object. After the first [`start(completion:)`](phasesoundevent/start(completion:).md) call on a particular `PHASESoundEvent` instance, subsequent calls have no effect.

 To play the same sound asset again, create another sound event object. After the first [`start(completion:)`](phasesoundevent/start(completion:).md) call on a particular `PHASESoundEvent` instance, subsequent calls have no effect.

## Topics

### Creating a Sound Event
- [init(engine: PHASEEngine, assetIdentifier: String) throws](phasesoundevent/init(engine:assetidentifier:).md)
  Creates a sound event node with the given asset.
- [init(engine: PHASEEngine, assetIdentifier: String, mixerParameters: PHASEMixerParameters) throws](phasesoundevent/init(engine:assetidentifier:mixerparameters:).md)
  Creates a sound event node with the given asset and mixer parameters.
### Configuring Mixers and Metaparameters
- [var mixers: [String : PHASEMixer]](phasesoundevent/mixers.md)
  Nodes in the event tree that control the volume of their child nodes.
- [var metaParameters: [String : PHASEMetaParameter]](phasesoundevent/metaparameters.md)
  The object’s meta parameters.
### Preparing Playback
- [func prepare(completion: ((PHASESoundEvent.PrepareHandlerReason) -> Void)?)](phasesoundevent/prepare(completion:).md)
  Enables a sound event to play and runs the argument code when the sound event plays back.
- [PHASESoundEvent.PrepareHandlerReason](phasesoundevent/preparehandlerreason.md)
  Indicates the results of sound-event preparation.
- [var prepareState: PHASESoundEvent.PrepareState](phasesoundevent/preparestate-swift.property.md)
  The status of sound-event preparation.
- [PHASESoundEvent.PrepareState](phasesoundevent/preparestate-swift.enum.md)
  Indicates the state of sound-event preparation.
### Checking Playback Status
- [var renderingState: PHASESoundEvent.RenderingState](phasesoundevent/renderingstate-swift.property.md)
  The sound event’s playback status.
- [PHASESoundEvent.RenderingState](phasesoundevent/renderingstate-swift.enum.md)
  The playback status of audio.
### Providing Buffered Data
- [var pushStreamNodes: [String : PHASEPushStreamNode]](phasesoundevent/pushstreamnodes.md)
  A collection of audio streams for playback.
### Starting Playback
- [func start(completion: ((PHASESoundEvent.StartHandlerReason) -> Void)?)](phasesoundevent/start(completion:).md)
  Invokes the sound event and runs the specified code on completion.
- [PHASESoundEvent.StartHandlerReason](phasesoundevent/starthandlerreason.md)
  Indicates the status after starting a sound event.
### Seeking a Time
- [func seek(to: Double, completion: ((PHASESoundEvent.SeekHandlerReason) -> Void)?)](phasesoundevent/seek(to:completion:).md)
  Advances the sound event’s playback position to a specific time.
- [PHASESoundEvent.SeekHandlerReason](phasesoundevent/seekhandlerreason.md)
  Indicates the status after a sound event changes its playback position.
### Pausing Playback
- [func pause()](phasesoundevent/pause.md)
  Pauses the sound event.
- [func resume()](phasesoundevent/resume.md)
  Resumes the sound event.
### Stopping Playback
- [func stopAndInvalidate()](phasesoundevent/stopandinvalidate.md)
  Stops a sound event and prevents it from resuming.
- [var isIndefinite: Bool](phasesoundevent/isindefinite.md)
  A Boolean value that indicates whether the sound loops or stops on its own.
### Instance Properties
- [var pullStreamNodes: [String : PHASEPullStreamNode]](phasesoundevent/pullstreamnodes.md)

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

- [class PHASESoundAsset](phasesoundasset.md)
  A sound resource stored in the asset registry.
- [PHASESoundEvent.RenderingState](phasesoundevent/renderingstate-swift.enum.md)
  The playback status of audio.
- [class PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
  A base class for sound event nodes that connect to form a node hierarchy.
- [class PHASESoundEventNodeAsset](phasesoundeventnodeasset.md)
  A template object for sounds that can play in reaction to environmental state.
- [class PHASEAsset](phaseasset.md)
  A base class that adds a name to framework assets.
- [Sound Event Nodes](sound-event-nodes.md)
  Objects that connect to form a hierarchical tree of audio actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent)*