# Automating motion path creation with editor-scripting commands

**Framework**: Reality Composer Pro

Build the same multi-track Sequence and Motion Path shown in the Sequencer UI programmatically, by chaining editor-scripting commands together.

#### Overview

Everything in [`Building multi-track animation sequences`](building-multi-track-animation-sequences.md) is achievable through the Sequencer UI, but Reality Composer Pro also exposes editor-scripting commands that an assistant agent can chain together to build the same result. This is distinct from [`Getting started with Script Graphs`](getting-started-with-script-graphs.md), which authors runtime behavior assets — editor scripting drives the editor itself. The practical entry point is the Assistant tab’s execute mode (sometimes called Agent mode), where these commands run in sequence against the open project.

#### Prepare a Scene Entity As a Rootable Prototype

The Sequencer-side commands are `add_sequence`, `add_track_to_sequence`, `add_path_to_track`, `edit_path`, and `edit_path_orbit_parameters`.

> 💡 **Tip**: There’s one prerequisite worth knowing before you reach for them: `add_sequence` rejects runtime scene-entity ids outright, and it also rejects anything located under `core.lib/`. If the entity you want to animate exists only in the scene and has no asset-side counterpart, call `create_prototype_assets` on it first — this registers it as a `Generated Prototypes/<name>` asset in the Project Browser, and that asset’s id is what you pass as `rootTargetEntityID`.

#### Build and Shape an Orbit Motion Path

With that prerequisite handled, an Orbit Motion Path comes together as a short chain. First, if needed, `create_prototype_assets` turns the runtime entity into a `Generated Prototypes/<name>` asset. Next, `add_sequence` with `rootTargetEntityID` set to that prototype’s id creates the Sequence and returns its own id. Then `add_track_to_sequence`, given the sequence id and an `entityForNewTrackID` (typically the same prototype, though it can be any descendant), adds a track and returns a track id. From there, `add_path_to_track` adds a Motion Path to that track — passing the track id and an optional `delay` — and returns a path id, again defaulting to the same two-point straight line you’d get from the UI.

![Screenshot of a sphere with an Orbit Motion Path in the Reality Composer Pro Animation Sequence editor.](https://docs-assets.developer.apple.com/published/caf6ee3d14d0975da20cc62ee8586e5c/AnimationMotionPathOrbit%402x.png)

Configure the path’s overall behavior with `edit_path`, passing the path id along with `type` set to `1` for Orbit, a `duration` in seconds, `constantSpeed` set to `true`, `isClosed` set to `true` to loop it, and `useLookAlongPath` set to `true` so the entity faces the direction it’s traveling. Finally, `edit_path_orbit_parameters` fills in the orbit’s geometry: `radius`, `numPoints` (at least four), `spinsPerOrbit`, and a `spinAxis` — for example, a radius of 0.5, eight points, zero additional spins, and a spin axis of (0, 1, 0) for a flat circle in the XZ plane.

#### Continue the Chain to Wire Auto Play

This chain builds the Sequence and its Motion Path, but it doesn’t wire auto-play on its own — an Animation Library Component still has to reference the Sequence. The same Root Entity rule described in [`Creating animation sequences for auto-play`](creating-animation-sequences-for-autoplay.md) applies to scripted Sequences too. See that article’s “Wire auto-play with editor-scripting commands” section to continue the chain from the prototype and Sequence id produced here.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
- [Creating animation sequences for auto-play](creating-animation-sequences-for-autoplay.md)
  Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.
- [Building multi-track animation sequences](building-multi-track-animation-sequences.md)
  Root a Sequence correctly so it shows up as a clip and plays automatically at runtime.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Build character animation state machines visually using the Animation Graph in Reality Composer Pro.
- [Building an advanced Animation Graph](building-an-advanced-animation-graph.md)
  Drive a character’s locomotion state machine from a Script Graph at runtime.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/automating-motion-path-creation-with-editor-scripting-commands)*