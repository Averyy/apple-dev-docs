# Creating animation sequences

**Framework**: Reality Composer Pro

Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.

#### Overview

In Reality Composer Pro, a **sequence** is an asset that defines a series of animations you can apply to an entity. Reality Composer Pro includes pre-made **sequence actions** you can apply to entities to quickly add animations. In addition, you can create your own custom sequences tailored to your specific animation needs.

You can build and design sequences in the Sequence Editor, where you can add and edit motion paths, animations, and movements. Apply a sequence to an entity. When you create a sequence, Reality Composer Pro prompts you to open an entity in your project.

##### Create or Open an Animation Sequence

1. In the Project Browser, control-click a folder, and then click **New** > **Animation** > **Sequence**.
2. Type a name for the sequence and then press Return.
3. Under **Set Target Entity,** click **Choose** to locate and then select an entity for the sequence.

> 💡 **Tip**: You can use the Search box to help you find the entity.

**Method 2** In the Project Browser, browse to an animation sequence and double-click it to open it. The animation sequence and its associated entity open automatically.

![A screenshot of Reality Composer Pro showing an animation sequence in the Project Browser.](https://docs-assets.developer.apple.com/published/cd52db86e9bb5084c24fb6fc8318fb9c/AnimationProjectBrowser%402x.png)

#### Browse the Animation Clips Panel

The Animation Clips panel shows a list of compatible animations for the currently open sequence. After you add tracks to your sequence, drag clips from this panel directly onto tracks in the Sequence Editor.

> 💡 **Tip**: Click the **Hierarchy** tab in the Animation Clips panel to view the entity hierarchy for the currently opened animation sequence. This is useful when your sequence has deeply nested entities and you need to find a specific child entity.

![A screenshot of Reality Composer Pro showing the Animation Clips panel with compatible animations listed for an open animation sequence.](https://docs-assets.developer.apple.com/published/1273b94797181722f140cc2c2f84128e/OpenExistingAnimation%402x.png)

#### Change Animation Sequence Playback

To sync a clip to a specific moment in your sequence, drag the left edge of a clip to set the **Trim Start**. To adjust the **Repeat Mode** and **Repeat Duration**, drag from the top of the right edge. To set the **Trim End**, drag from the bottom of the right edge. Hold Option while dragging the bottom-right edge to change the **Speed**. For actions, drag the right edge to adjust **Duration**.

#### Change Sequence Editor Display Options

Click **Options** (…) to change the following options:

- Units — Frames or Seconds
- Snap — Nodes to Ruler, Nodes to Nodes, Playhead to Ruler

#### Add a Sequence Track

To add a sequence track, click **[+]** in the lower left corner. Select a target entity in the preview tab and then click **Select**. In the Inspector, enter a name for the new track.

To add a sub-track to an existing sequence track, click **[+]** in the lower right corner of the sequence track. In the Inspector, enter a name for the new sub-track.

#### Add Actions to a Sequence

Actions are predefined, modular parts you can add to a sequence track to perform different functions. Under **Animation Clips**, under **Actions**, drag an action onto a sequence track. Click the action to select it, then configure its parameters in the Inspector. Different actions have different parameters.

The following actions are available:

- **Play Audio** — Plays an audio file or sound effect synchronized with the animation timeline. Add audio files to an Audio Library Component on the target entity before they appear in the Sequence Editor for selection. See [`PlayAudioAction`](https://developer.apple.com/documentation/RealityKit/PlayAudioAction).
- **Enable/Disable Entity** — Controls the visibility and active state of a target entity and its descendants in the scene, turning them on or off at specific timeline points. See [`SetEntityEnabledAction`](https://developer.apple.com/documentation/RealityKit/SetEntityEnabledAction).
- **Motion Path** — Defines spatial control points for path-based orbit, spin, or custom movement animation along predefined trajectories.
- **Billboard Blend In/Out** — Animates the blend factor of the target entity’s Billboard component, controlling how strongly the entity orients itself toward the active camera over time. See [`BillboardAction`](https://developer.apple.com/documentation/RealityKit/BillboardAction).

![A screenshot of Reality Composer Pro Animation Sequence Editor showing a Track with an Animation Motion Path.](https://docs-assets.developer.apple.com/published/b23265fb86b5d7b49b2e1d02a2328f53/AnimationMotionPath2%402x.png)

#### Configure Sequence Properties

The Sequence Settings control the global properties and target assignment for the sequence.

**Root Entity** The root entity in the scene hierarchy that this sequence uses as the targeting scope. The sequence can then apply animations to the root entity itself or to its child entities through individual tracks. For example, setting the Root Entity to `world` allows tracks to target any entity in the scene hierarchy as children of the `world` entity.

**Speed** Playback speed multiplier for the entire sequence. 1 is normal playback, 2 doubles playback speed, and so forth. Lower numbers reduce playback speed.

#### Configure Track Properties

Track properties let you turn a selected track on or off (mute). **Name** The name of the selected track.

**Mute** When toggled, disables the track.

#### Configure Clip Properties

The Animation Clip Properties provide controls for configuring animation clips on the Sequence Editor timeline.

**Trim Start** The number of seconds to trim from the beginning of the clip.

**Trim End** The number of seconds to trim from the end of the clip.

**Delay** The number of seconds to delay before playing the clip.

**Repeat Mode**

- None — Clip does not repeat
- Repeat — Clip repeats
- Auto Reverse — Clip plays forward and then backward

**Repeats Forever** (toggle) If the clip repeats, this toggle sets the clip to loop indefinitely.

**Repeat Duration** When you set the clip to repeat and turn off **Repeats Forever**, use Repeat Duration to specify the number of seconds for the clip to repeat.

## See Also

- [Creating animation sequences for auto-play](creating-animation-sequences-for-autoplay.md)
  Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.
- [Building multi-track animation sequences](building-multi-track-animation-sequences.md)
  Root a Sequence correctly so it shows up as a clip and plays automatically at runtime.
- [Automating motion path creation with editor-scripting commands](automating-motion-path-creation-with-editor-scripting-commands.md)
  Build the same multi-track Sequence and Motion Path shown in the Sequencer UI programmatically, by chaining editor-scripting commands together.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Build character animation state machines visually using the Animation Graph in Reality Composer Pro.
- [Building an advanced Animation Graph](building-an-advanced-animation-graph.md)
  Drive a character’s locomotion state machine from a Script Graph at runtime.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-animation-sequences)*