# Optimizing audio playback in Reality Composer Pro

**Framework**: Reality Composer Pro

Balance audio quality against CPU, memory, and power cost when configuring playback.

#### Overview

Reality Composer Pro makes it easy to drop a sound into a scene, but the defaults behind that convenience carry real performance costs. Whether an asset streams or preloads, which playback component it uses, and the property values left at their defaults all affect CPU load, memory footprint, and power consumption — costs that aren’t obvious from the Inspector alone. Left unexamined, a scene can end up spending its audio budget on the wrong tradeoffs: high memory use for sounds that didn’t need it, ongoing decode work on the audio thread for assets that could have preloaded once, or full spatialization cost for sounds that only needed a fixed stereo mix.

![A screenshot of a Reality Composer Pro Scene with an audio asset opened in the Inspector.](https://docs-assets.developer.apple.com/published/38442e94ea52826322c532b9a28bd750/AudioVillageAtmosphere%402x.png)

This article covers the tradeoffs that matter most as a scene grows: memory versus compute when choosing how an asset loads, spatialization cost versus realism when choosing a playback component and tuning its properties, and organizational choices — like grouping related assets and sounds — that pay off as the number of audio sources increases. It assumes familiarity with Reality Composer Pro’s audio components and asset workflow. For that background, see [`Adding audio components in Reality Composer Pro`](introduction-to-reality-composer-pro-audio.md).

#### Choose a Loading Strategy for Each Audio Asset

Every audio asset in a scene loads using one of two strategies, set through [`AudioFileResource.LoadingStrategy`](https://developer.apple.com/documentation/RealityKit/AudioFileResource/LoadingStrategy-swift.enum): [`AudioFileResource.LoadingStrategy.preload`](https://developer.apple.com/documentation/RealityKit/AudioFileResource/LoadingStrategy-swift.enum/preload) decodes the entire asset into memory up front, and [`AudioFileResource.LoadingStrategy.stream`](https://developer.apple.com/documentation/RealityKit/AudioFileResource/LoadingStrategy-swift.enum/stream) decodes it incrementally from disk during playback. In Reality Composer Pro, this is the **Should Stream** toggle in the audio file Inspector — see [`Adding audio components in Reality Composer Pro`](introduction-to-reality-composer-pro-audio.md) for where to find that control.

Match the strategy to how the asset behaves in the scene:

- Short, frequent, or latency-sensitive sounds — UI feedback, footsteps, gunshots — benefit from `.preload`. The decode work happens once at load time, so playback starts immediately and the real-time CPU cost during each play is low and predictable.
- Long-duration assets — music beds, ambiences, voice-over — benefit from `.stream`. Memory use stays low because only a small buffer is decoded at a time, but that decoding continues on the audio thread for as long as the sound plays.

Normalization interacts with this choice in a way that’s easy to miss: the `.dynamic` case of `AudioResource.Normalization` applies real-time dynamic compression to bring an asset to a target loudness. For a `.preload` resource, that compression work happens once, at load time. For a `.stream` resource, it runs continuously alongside the ongoing decode, so combining `.stream` with dynamic normalization stacks two ongoing per-frame costs on the audio thread instead of one. If a streamed asset also needs loudness normalization, weigh that combined cost against simply preloading it.

#### Pick the Cheapest Playback Component That Meets the Need

Reality Composer Pro’s three playback components — Spatial Audio, Ambient Audio, and Channel Audio — don’t cost the same to render, even when playing identical source material. See [`Adding audio components in Reality Composer Pro`](introduction-to-reality-composer-pro-audio.md) for what each component fundamentally does; this section focuses on their relative cost and how to choose deliberately.

Ranked from most to least expensive:

- **Spatial Audio** does the most work: it tracks the emitting entity’s position and orientation relative to the listener, calculates distance attenuation, mixes the source down to mono, applies directivity, and sends a portion of the signal to the reverb system.
- **Ambient Audio** costs less to render than Spatial Audio: it still applies orientation, but without Spatial Audio’s distance attenuation or reverb send.
- **Channel Audio** is the cheapest: it plays straight to output channels with none of Spatial Audio’s positional, distance, or reverb processing.

[`SpatialAudioComponent`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent) is the component Reality Composer Pro applies automatically when an entity emits audio and no component is explicitly specified. That means a scene where you never explicitly configure a playback component for your audio-emitting entities pays the highest per-voice cost across the board, without anyone having chosen it.

Choose deliberately instead of relying on the default:

- Use Channel Audio for music beds and other fixed-direction audio that doesn’t need to move with an entity.
- Use Ambient Audio for orientation-only soundscapes, such as field recordings, where distance falloff doesn’t matter.
- Reserve Spatial Audio for sounds that genuinely need position tracking and distance falloff.

![A screenshot of Reality Composer Pro Scene with Ambient Audio properties displayed in the Inspector.](https://docs-assets.developer.apple.com/published/f988a95c135fcc6c220418f6ad2b9a23/AudioVillageAmbientAudio2%402x.png)

#### Tune Spatial Audio Properties for Cost and Realism

[`SpatialAudioComponent`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent) exposes several properties for shaping how a spatialized sound behaves, including [`gain`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent/gain), [`directLevel`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent/directLevel), and [`reverbLevel`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent/reverbLevel), all relative decibel values in the range `[-Decibel.infinity, Decibel.zero]`.

![A screenshot of Reality Composer Pro Spatial Audio Component settings in the Inspector.](https://docs-assets.developer.apple.com/published/4bfc0f5c3a3390eaa96dbf3f5bf40115/AudioSpatialAudioComponentExample%402x.png)

- `gain` sets the overall output level of the sound.
- `directLevel` sets the level of the direct, unreverberated signal that reaches the listener.
- `reverbLevel` sets the level of the signal sent to the reverb system. Setting `reverbLevel` to `-Decibel.infinity` removes the reverb send entirely, collapsing the sound fully dry into the listener’s head. Because this eliminates the sound’s contribution to the reverb bus, it’s a genuine way to reduce cost for sounds that don’t need reverb.

Two more properties shape the sound’s directional and distance behavior:

- [`directivity`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent/directivity) (`Audio.Directivity`) controls how sound radiates from the source. The `.beam(focus:)` case models a parametric, frequency-dependent radiation pattern, where `focus` sets the beam’s width.
- [`distanceAttenuation`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent/distanceAttenuation) (`Audio.DistanceAttenuation`) controls how level falls off with distance, using either `.rolloff(factor:)` for a custom falloff curve or `.default`.

Treat `directivity` and `distanceAttenuation` as realism and quality controls, not cost controls. A narrow beam or a custom rolloff factor changes how a sound behaves, but it doesn’t reduce the work the engine does to compute it. Of the four properties described here, `reverbLevel` is the only one that reduces engine workload when tuned down.

> ❗ **Important**: Spatial audio sources project along negative-Z. If you author your source content facing positive-Z and you’re using a non-default `directivity` value — a `.beam(focus:)` with a non-zero focus — rotate the audio source entity 180 degrees around the y-axis so the beam points the intended direction. The default, `.beam(focus: .zero)`, projects sound evenly in all directions and needs no rotation.

#### Author Mono Source Material for Spatial Audio

Spatial audio sources are single-channel only. Regardless of how many channels a source asset has, [`SpatialAudioComponent`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent) mixes it down to mono before spatializing it.

Because that mixdown happens automatically, it’s tempting to import stereo or multichannel assets and let the engine handle it. Author and export source assets as mono directly instead. This avoids phase-cancellation artifacts that can appear when a stereo file collapses to one channel, and it keeps source files smaller on disk — which also reduces the memory cost of preloading, as described in [`Choose a loading strategy for each audio asset`](optimizing-audio-playback#Choose-a-loading-strategy-for-each-audio-asset.md).

#### Manage the Reverb Budget Across a Scene

Within a given ARView or RealityView, only one [`ReverbComponent`](https://developer.apple.com/documentation/RealityKit/ReverbComponent) can be active at a time on macOS and iOS; see [`Adding audio components in Reality Composer Pro`](introduction-to-reality-composer-pro-audio.md) for how to add one and choose a preset. Because reverb is a shared, scene-wide system rather than something each sound carries independently, `reverbLevel` — covered in [`Tune spatial audio properties for cost and realism`](optimizing-audio-playback#Tune-spatial-audio-properties-for-cost-and-realism.md) — is the lever that controls each sound’s contribution to that shared cost.

> **Note**: On visionOS, `ReverbComponent` is only active while your app has a progressive or full immersive space open. In Shared Space or a mixed immersion style, RealityKit uses real-environment acoustics simulation instead and ignores `ReverbComponent` entirely. If you tune `reverbLevel` or `directLevel` expecting your reverb preset to shape the sound, verify your app’s immersion style — the preset has no effect outside an immersive space.

#### Avoid Unnecessary Power Cost From Preparing Audio Early

[`prepareAudio(_:)`](https://developer.apple.com/documentation/RealityKit/Entity/prepareAudio(_:)) gets an audio resource ready to play, but that readiness isn’t free. As its documentation states: “As soon as the system prepares an audio resource, the audio engine begins tracking the position of the entity and allocates rendering resources, which incurs a power cost.” The guidance that follows is direct: “For optimal system resource usage, avoid preparing sounds before they are needed.”

[`playAudio(_:)`](https://developer.apple.com/documentation/RealityKit/Entity/playAudio(_:)) calls `prepareAudio(_:)` internally before it calls `play()`, so the same power cost applies the instant you call `playAudio(_:)` — there’s no way to play a sound without first paying the preparation cost.

Two practices compound this cost if you’re not careful:

- Calling `playAudio(_:)` repeatedly without checking `isPlaying` first starts a new playback instance each time, and each instance carries its own tracking and rendering allocation running concurrently.
- Preparing or playing audio on an entity that isn’t yet parented in the scene still incurs the tracking and allocation cost, even though the entity isn’t placed anywhere and nothing is audible yet.

That second point rules out an intuitive-but-wrong optimization: preparing audio ahead of time as a “warm-up” step before an entity is placed. Playback only actually starts once the entity is parented and placed in the scene, so preparing early doesn’t save time later — it just starts the power cost sooner. Prepare and play audio only when the entity is in place and the sound is actually needed.

#### Control Playback at Runtime Instead of Restarting It

Once a sound is playing, use [`AudioPlaybackController`](https://developer.apple.com/documentation/RealityKit/AudioPlaybackController) to change its behavior rather than stopping and re-triggering `playAudio(_:)`. Starting playback returns an [`AudioPlaybackController`](https://developer.apple.com/documentation/RealityKit/AudioPlaybackController), which exposes:

- `fade(to:duration:)`, `speed`, `reverbSendLevel`, `seek(to:)`, and `play(at:)` to adjust a playing sound in place, without paying the tracking and rendering allocation cost of stopping it and preparing a new playback instance.
- `stop()`, `pause()`, and `isPlaying` to control and query playback state — checking `isPlaying` before playing again is what lets you avoid the redundant-instance cost described next.

Check `isPlaying` before calling `playAudio(_:)` again on the same entity, so you don’t spin up a redundant concurrent playback instance as described in [`Avoid unnecessary power cost from preparing audio early`](optimizing-audio-playback#Avoid-unnecessary-power-cost-from-preparing-audio-early.md).

#### Organize Assets with Audio File Groups and Audio Mix Groups

Audio File Groups and Audio Mix Groups solve two different organizational problems, and it’s worth keeping them distinct despite the similar names. See [`Adding audio components in Reality Composer Pro`](introduction-to-reality-composer-pro-audio.md) for the steps to create each one; this section covers why each matters.

An **Audio File Group** bundles a set of sound variations — different footstep sounds, different bird calls — into a single referenceable group, and Reality Composer Pro selects a random file from that group at runtime. Grouping variations this way means you don’t need to author and reference several near-identical assets individually, which keeps both your project structure and your asset memory footprint smaller than duplicating similar sounds one by one.

An **Audio Mix Group** centralizes runtime volume and speed control for a related set of sounds — all sound effects, for example — behind a single slider. At the code level, `mixGroupName` on [`AudioFileResource.Configuration`](https://developer.apple.com/documentation/RealityKit/AudioFileResource/Configuration-swift.struct) assigns a resource to a mix group. Routing related sounds through a mix group means your app manages one control surface for the group instead of holding a separate `AudioPlaybackController` reference for every sound it needs to adjust together.

## See Also

- [Adding audio components in Reality Composer Pro](introduction-to-reality-composer-pro-audio.md)
  Configure audio components in a Reality Composer Pro scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/optimizing-audio-playback)*