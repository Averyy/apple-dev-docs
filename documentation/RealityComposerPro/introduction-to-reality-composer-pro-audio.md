# Adding audio components in Reality Composer Pro

**Framework**: Reality Composer Pro

Configure audio components in a Reality Composer Pro scene.

#### Overview

Reality Composer Pro provides a set of audio components you can add to entities in your scene to control how sound is rendered. The three main audio source components — Spatial Audio, Ambient Audio, and Channel Audio — differ in how they respond to listener position and orientation.

A Reverb component lets you define an environment-wide reverb preset. Audio File Groups and the Audio Library Component provide flexible ways to reference and play audio assets from within your scene’s logic. An Audio Mix Group lets you control the volume and playback speed of a collection of sounds together through a single slider.

#### Import Audio Files Through the Project Browser

In the Project Browser, click **Import Asset**, select one or more audio files, and then click **Open**. Alternatively, drag files from the Finder into the desired location in the Project Browser.

#### Inspect and Preview Audio

To play back an audio file from the Project Browser, click an audio file. In the Preview tab, click **Play**.

> 💡 **Tip**: The Preview tab displays the audio file channels above the waveform.

The Inspector displays the following basic audio properties for the file.

> **Note**: Some key properties and usage are highlighted below. For more information, see [`AudioFileResource.Configuration`](https://developer.apple.com/documentation/realitykit/audiofileresource/configuration-swift.struct).

- **Should Loop** — When toggled on, the audio loops seamlessly. If you attempt to loop the sound using the completionHandler in the API, there will be a slight gap between repeats. Configuring the looping behavior on the resource allows the audio engine to guarantee sample-precise seamless looping.
- **Should Randomize Start** — Randomizes the start time of the audio file.

Use **Should Randomize Start** and **Should Loop** together to create audio variation using the same audio file. This is useful when you want constant sound with subtle variation, such as ambient nature sounds.

> 💡 **Tip**: You can also use these effects on a single audio file and then add multiple instances of that audio file to a scene for even more variation.

- **Should Stream** — When toggled on, the audio streams from disk instead of loading into memory.

Streaming audio saves memory but uses more compute. For more information, see [`AudioFileResource.LoadingStrategy`](https://developer.apple.com/documentation/realitykit/audiofileresource/loadingstrategy-swift.enum).

#### Choose an Audio Playback Component

There are three main audio components you can add to control how audio is rendered in space within your scene. Use **Spatial Audio** when sound should emanate from a specific entity and respond to your environment’s reverb. Use **Ambient Audio** for multichannel recordings where orientation matters but position does not. Use **Channel Audio** for music or non-spatialized audio that routes directly to device output channels.

#### Add a Spatial Audio Component

Spatial Audio is the **default** audio component placed on an entity. If you don’t specify Ambient or Channel for an entity, the system renders audio as Spatial.

- Spatial audio emanates from its entity.
- Spatial Audio inherits reverberation characteristics of the environment.

> 💡 **Tip**: To attach playback to the simulated reverb in your scene, use a Spatial Audio component. Regardless of how many channels an audio file has, the Spatial Audio component mixes it down to a single channel — preview this using the Audio Preview within the Spatial Audio component. Spatial Audio sources are Negative-Z forward, represented in the Spatial Audio component by the yellow arrow.

![A screenshot of the Reality Composer Pro Spatial Audio Component properties and graphical representation in the Viewport.](/images/RealityComposerPro/Audio_SpatialAudio@2x.png)

For more information, see [`SpatialAudioComponent`](https://developer.apple.com/documentation/realitykit/spatialaudiocomponent).

#### Add an Ambient Audio Component

Ambient Audio renders each channel of an audio resource from an angle based on the entity’s orientation. As you move toward or away from the entity, the volume does not change. As the entity or listener rotates, the audio channels shift accordingly. This makes Ambient Audio well-suited for multichannel field recordings of outdoor environments.

- Ambient audio is position-independent but orientation-sensitive.
- Ambient Audio does not take on Reverb characteristics; it relies on Reverb effects recorded in the source audio file.

For more information, see [`AmbientAudioComponent`](https://developer.apple.com/documentation/realitykit/ambientaudiocomponent).

#### Add a Channel Audio Component

Channel Audio routes audio directly to the device output channels with no spatialization or reverberation applied. Neither the entity’s position nor its orientation affects playback — the left channel always plays from the left and the right channel always from the right, regardless of listener orientation.

- Channel Audio does not take on Reverb characteristics.

Channel Audio is typically used for music.

For more information, see [`ChannelAudioComponent`](https://developer.apple.com/documentation/realitykit/channelaudiocomponent).

#### Add a Reverb Component

Add a Reverb component to an entity to define a preset Reverb characteristic such as Living Room or Concert Hall for a scene.

Only one Reverb component can be active at a time in a scene, and you can place it anywhere in a scene.

> 💡 **Tip**: Reverb components can be added to any entity in a scene. Place it at a high level in your Hierarchy.

> 💡 **Tip**: The Reverb component affects any entity that has a Spatial Audio component (the default).

For more information, see [`ReverbComponent`](https://developer.apple.com/documentation/realitykit/reverbcomponent).

#### Add an Audio File Group to Your Project

Add an **Audio File Group** to define a collection of audio files. When RealityKit plays an Audio File Group, it selects a random file from the collection — useful for groups of similar but varied sounds, such as footsteps or bird calls. You reference Audio File Groups through an **Audio Library Component** attached to an entity.

![A screenshot of adding audio files to a Reality Composer Pro Audio Library Component.](/images/RealityComposerPro/Audio_Library_2@2x.png)

You can have as many Audio File Groups in your project as you need. For example, you might define a group for Forest Sounds and another for Musical Instrument Sounds.

1. In the Project Browser, click **[+]**, then click **Audio** > Audio File Group**.
2. Type a name for the Audio File Group and press Return.
3. Click your Audio File Group.
4. In the Inspector, under **Audio File Asset**, next to **Sound**, click the field and select an audio file from your project.
5. To add more files to the Audio File Group, click **+** next to **Assets**.

After creating an Audio File Group, add an Audio Library Component to an entity and connect the component to the Audio File Group.

#### Add an Audio Library Component to an Entity

The Audio Library Component lets you reference and play specific sounds directly, or reference an Audio File Group to play sounds selected at random. Other components, such as Script Graphs and Animation Sequences, can reference audio files in the library.

> 💡 **Tip**: An Audio Library does not have to be played back from the entity it is attached to. Any entity can reference and play back audio files from the library.

1. Select an entity in your project.
2. In the Inspector, click **Add Component** > **Audio Library**.
3. Click **+Named Audio Reference**.
4. Next to **Name**, type a name for the audio asset.
5. Click the **Audio Asset** field and select an audio file from the list.
6. Repeat the last two steps to add as many audio references as you need.

![A screenshot of adding audio files to a Reality Composer Pro Audio Library Component.](/images/RealityComposerPro/Audio_Library_2@2x.png)

For more information, see [`AudioLibraryComponent`](https://developer.apple.com/documentation/realitykit/audiolibrarycomponent).

#### Add an Audio Mix Group Component

Use an **Audio Mix Group** to group sounds together — for example, instruments in a band, voices, and other environmental sounds — and then control their volume and playback speed as a group through a single slider. Add only one Audio Mix Group to your scene.

> 💡 **Tip**: Place the Audio Mix Group on a top-level entity in your Hierarchy.

1. In the Project Browser, click **[+]** > **Audio** > **Audio Mix Group**.
2. Type a name for the Mix Group and then press Return.
3. In the Inspector, under **Sounds**, click **Add Sound** and select a sound.
4. Repeat the previous step to add more sounds to the Mix Group.

## See Also

- [Optimizing audio playback in Reality Composer Pro](optimizing-audio-playback.md)
  Balance audio quality against CPU, memory, and power cost when configuring playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/introduction-to-reality-composer-pro-audio)*