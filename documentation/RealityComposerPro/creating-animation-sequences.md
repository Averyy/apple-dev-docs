# Creating animation sequences

**Framework**: Reality Composer Pro

Build and customize animation sequences to control entity movement and behavior in your scene.

#### Overview

In Reality Composer Pro, a **sequence** is an asset that defines a series of animations you can apply to an entity. Reality Composer Pro includes pre-made **sequence actions** you can apply to entities to quickly add animations. In addition, you can create your own custom sequences tailored to your specific animation needs.

You can build and design sequences in the Sequence Editor, where you can add and edit motion paths, animations, and movements. Apply a sequence to an entity. When you create a sequence, Reality Composer Pro prompts you to open an entity in your project.

##### Create or Open an Animation Sequence

1. In the Project Browser, control-click a folder, and then click **New > Sequence**.
2. Type a name for the sequence and then press Enter.
3. Under **Set Target Entity,** click **Choose** to locate and then select an entity for the sequence.

> 💡 **Tip**: You can use the Search box to help you find the entity.

**Method 2** In the Project Browser, browse to an animation sequence and double-click it to open it. The animation sequence and its associated entity open automatically.

![A screenshot of the Reality Composer Pro showing an animation sequence in project browser.](https://docs-assets.developer.apple.com/published/cd52db86e9bb5084c24fb6fc8318fb9c/AnimationProjectBrowser%402x.png)

##### Explore the Animation Clips Panel

The animation clips panel shows a list of compatible animations.

> 💡 **Tip**: You can click the tab to view the Hierarchy for the currently opened animation sequence.

![A screenshot of the Reality Composer Pro showing an animation sequence in project browser.](https://docs-assets.developer.apple.com/published/1273b94797181722f140cc2c2f84128e/OpenExistingAnimation%402x.png)

##### Use the Sequence Editor Controls

The Sequence Editor works much like a basic video editor, with the following controls (left to right):

- Back
- Rewind
- Play/Pause
- Fast Forward
- End
- Repeat

You can also click and drag the Start and End icons to adjust the length (corresponding to **Trim Start** and **Trim End** in the Sequence Inspector) of the sequence playback.

Click the Options (…) to change the following options:

- Units — Frames or Seconds
- Snap — Nodes to Ruler, Nodes to Nodes, Playhead to Ruler

##### Add an Additional Sequence Track

1. Click **(+)** in the lower right corner to add a track.
2. In the Inspector, enter a name for the new track.

##### Add Actions to a Sequence

Actions are pre-defined, modular parts you can add to a Sequencer track to perform different functions — such as playing an audio file or moving along a customizable motion path.

1. Under **Animation Clips**, under **Actions**, click and drag an Action onto a Sequencer Track.
2. In the Sequencer Track, click on the added action and then configure it in the Inspector. Different actions have different parameters.

##### Review the Sequence Inspector

**Name** The name of the sequence.

**Speed** Playback speed. 1 is normal playback. Higher numbers increase playback speed, lower numbers reduce playback speed.

**Trim Start** The number of seconds to trim from the beginning of the sequence.

**Trim End** The number of seconds to trim from the end of the sequence.

**Delay** The number of seconds to delay before playing the sequence.

**Fill Mode**

- Forward
- Backward
- Both

**Repeat Mode**

- None — Sequence does not repeat
- Repeat — Sequence repeats
- Auto Reverse — Sequence plays forward and then backward

**Repeats Forever** (toggle) If sequence is set to repeat, this toggle sets the sequence to loop indefinitely.

**Repeat Duration** If Repeat mode is set to Repeat but Repeats Forever is toggled off, Repeat Duration lets you specify a specific number seconds for the sequence to repeat.

**Repeat Duration** (slider) The slider below Repeat Duration lets you trim the start and end for the repeated portion of the sequence.

**Target Skeleton** Skeleton to use for the animation sequence.

**Root Motion Joint**

**Root Motion Options**

- Extract All
- Extract XZ
- Extract XZ Orient Y
- None
- Remove All

**Is Additive** (toggle) When toggled on, blends this animation as an additive layer on top of other animations.

**Subtract Base Animation** (toggle) When Is Additive is toggled on, subtracts the base pose from this clip before blending.

**Draw Bones** (toggle) Displays (overlays) the bones for the animated entity.

**Draw Axis** (toggle) When Draw bones is toggled on, this draws the movement axis on screen.

**Draw Names** (toggle) When Draw bones is toggled on, this displays the bone names on screen.

##### Animation Graph Nodes

The Animation Graph Editor provides a range of nodes organized by category. Each node performs a specific operation on poses, skeletons, or animation data.

- Blend nodes - **Add** — Adds two poses.
- **Blend 1D** — Blends a number of samples from child nodes distributed along a single axis.
- **Pose Mask** — Filters a pose by applying per-joint weights from a pose mask.
- **Subtract** — Subtracts one pose from another.
- Control flow nodes - **State Machine** — Evaluates a state machine.
- Inverse Kinematics (IK) nodes - **Constraint Parameters** — Parameters for a single named rig constraint.
- **Foot Placement** — Adjusts foot positions on terrain using inverse kinematics and constraints.
- **Full Body IK Node** — Full body inverse kinematics solver node with output pose based on the child pose and rig-defined constraints.
- **Joint Parameters** — Parameters for a single named rig joint.
- Modifier nodes - **Motion Warping** — Adjusts animation playback speed to ensure root motion reaches a target position.
- **Root Motion Generation** — Moves the root joint to the desired position and orientation over time.
- Output nodes - **Final Pose** — The final pose of the animation.
- Physics nodes - **Physics Bone Solver** — Applies rigid-body physics simulation to a bone chain.
- **Spring Bone** — Applies spring physics simulation to a bone for secondary motion.
- Source nodes - **Animation Clip** — Represents an animation clip at edit time. Plays an animation resource using keyframes.
- **Bind Pose** — Returns the bind pose of the current skeleton.
- **BlendShape Input** — Provides blend shape weights from a parameter.

## See Also

- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Define and control character animations using a visual, node-based state machine in Reality Composer Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-animation-sequences)*