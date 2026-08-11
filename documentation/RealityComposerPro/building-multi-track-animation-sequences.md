# Building multi-track animation sequences

**Framework**: Reality Composer Pro

Root a Sequence correctly so it shows up as a clip and plays automatically at runtime.

#### Overview

A Sequence organizes animation over time using two building blocks: tracks and actions.

Tracks are timeline rows, each one scoped to a single entity — a main track picks its entity directly from the Preview viewport, while a sub-track always inherits the entity of the main track it belongs to. This lets one Sequence choreograph several entities at once, each with its own row or set of rows.

Actions are the events you place on those tracks. Unlike animation clips, which play back pre-authored USD animation data, actions trigger discrete behaviors: playing a sound, showing or hiding an entity, blending a billboard effect in or out, running a custom action you define, or animating an entity along a Motion Path. Each action type has its own Inspector property group, and some depend on a component — such as an Audio Library Component or a Billboard Component — already existing on the target entity.

Motion Path deserves special attention because it’s a small system in itself: a path made of points, each with position, rotation, scale, timing, and easing, optionally generated automatically into an orbit or spin shape rather than placed by hand.

![A screenshot of Reality Composer Pro showing an animation sequence with an Animation Motion Path selected.](https://docs-assets.developer.apple.com/published/ab9f9db12f08f1aa7e7ecf2de677514c/AnimationMotionPath3%402x.png)

> **Note**: The tracks and actions you author are wasted work at runtime unless the Sequence is rooted where its Animation Library Component expects to find it. The sections below build up multi-track authoring using tracks, actions, and Motion Path. Once your Sequence is ready, see [`Creating animation sequences for auto-play`](creating-animation-sequences-for-autoplay.md) to wire it for auto-play, or doc:automating-motion-path-creation-with-editor-scripting-commands to build the same Motion Path programmatically with editor-scripting commands.

If you haven’t created a Sequence yet, start there before returning to this article — this one assumes you already know how to open the Sequence Editor, assign a basic Root Entity, and drop a single clip on a track. See [`Creating animation sequences`](creating-animation-sequences.md) to learn the basics.

#### Add Multiple Tracks and Sub Tracks to a Sequence

Every main track targets one entity, and Reality Composer Pro asks you to pick that entity explicitly. Click the **+** button next to the track name to add a new main track, then click the entity you want in the Preview viewport and confirm the selection in the picker banner.

Sub-tracks skip the picker entirely. Click the **+** button on the right side of a main track’s header to add a sub-track underneath it, and that sub-track automatically targets the same entity as its parent — there’s no second entity choice to make. Use sub-tracks to spread multiple actions on the same entity across separate rows instead of stacking them all on one track, which keeps the timeline readable once a track starts collecting several audio cues, visibility toggles, and a Motion Path.

You can mute a track to disable it temporarily without deleting it, which is useful for isolating one action type while you tune the others.

#### Trigger Audio and Entity Visibility with Actions

Play Audio and Enable/Disable Entity are the two most common actions for scripting reactive scene behavior alongside an animation.

Play Audio synchronizes a sound with the timeline. Its Inspector group exposes Track Entry Name, Delay, Duration, Gain in decibels, a Controlled Playback toggle, and an Audio Resource picker. That picker only lists sounds that already exist as named references on an Audio Library Component belonging to the target entity — if the entity doesn’t have one yet, the Inspector shows an inline Add Audio Library Component button so you can add it without leaving the action’s properties panel. Once the component exists, its full configuration displays inline too, so the audio setup and the action setup live in the same place.

To reproduce this end to end, select the entity in the world hierarchy first and add an Audio Library Component to it through the Inspector’s Add Component menu, under Animation > Audio Library. Inside that component, click **+ Named Audio Reference** to create an entry, give it a name, and assign the audio asset you imported. Then open your Sequence, drag a Play Audio action from the Actions section onto a track, and select the newly placed clip on the timeline. In the Inspector, expand the Play Audio group and set Audio Resource to the named reference you just created — the sound now plays at the Delay you configured, for the Duration you set, whenever the Sequence reaches that point.

Enable/Disable Entity is simpler: it flips an entity’s active state at a specific timeline moment. Its properties are Track Entry Name, Delay, and an Is Enabled toggle. Use it for reveals, disappearing effects, or turning a particle system on right before a Motion Path starts moving through it — there’s no dependency on any other component, since visibility is a base entity property.

#### Add Camera Facing Transitions with Billboard Blend Inout

Billboard Blend In/Out fades a billboard effect in or out over the timeline rather than snapping it on or off. Its Inspector group has Track Entry Name, Delay, Duration, Transition In, and Transition Out — Transition In controls how long the blend takes to fully appear, and Transition Out controls how long it takes to fade away, both measured in seconds within the action’s overall Duration.

Like Play Audio, this action depends on a component: the target entity needs a Billboard Component so there’s something to actually keep facing the camera. If it’s missing, the Inspector shows an inline Add Billboard Component button beneath the action’s own settings, and clicking it adds the component in place. Once present, the Billboard Component’s full properties display inline in the same panel, so you can tune the billboard’s own behavior — such as the blend factor that controls how far it rotates toward the camera — right next to the blend timing you just set.

#### Extend the Timeline with Custom Actions

Custom Actions let you define your own action types beyond the five built-ins, backed by Custom Action Definition assets. Before they show up in the Sequencer, point Reality Composer Pro at your plugin code: open Project Settings from the menu bar, go to Build Settings, and set the Plugin Directory field to the location containing your custom action plugins. Once the directory is configured and loaded, your Custom Actions appear in the Actions section of the Sequencer Assets panel, sorted after the built-in actions and marked with a wrench icon. Each one carries the display name defined in its Custom Action Definition, and Reality Composer Pro uses that name both as its label in the asset tree and as the group label in the Inspector.

Dragging a Custom Action onto a track behaves like any other action: the Inspector shows Track Entry Name, Delay, Duration, and whatever schema-defined properties the definition provides. Below those sits the Bind Targets section, which only appears when the action has an animated value type — Float, Double, Vector2, Vector3, Vector4, Quaternion, or Transform, shown after a colon in the section header. Each binding card has a Component dropdown (choices include Transform, Opacity, Billboard, and Model, filtered to what the value type supports) and an Entity dropdown whose scope depends on which component you chose: for a Transform binding, the dropdown locks to the track’s own entity with no subtree choice at all; for Billboard and Opacity bindings, it lists every descendant of the track’s entity; and for Model bindings, a separate Value dropdown further filters to the target entity’s bindable material parameters. Use **+ Add Binding** to add another binding card, seeded with the first available component and entity, and the minus button on a card to remove it. If a chosen component isn’t present on the target entity, a validation row appears with a component-specific add button, the same inline-fix pattern used for Play Audio and Billboard Blend In/Out.

To try this yourself: set the Plugin Directory in Project Settings so your Custom Action Definition loads, then open your Sequence and drag the custom action from the Actions list onto a track. Select the placed action, and in Bind Targets click **+ Add Binding**, then choose a Component such as Opacity and an Entity from the track’s subtree — the action now drives that component’s value over its Delay-to-Duration window using whichever animated value the definition provides. A Sequence that includes Custom Actions still follows the same Root Entity and auto-play rules as any other Sequence described later in this article.

#### Animate Movement with a Motion Path

Motion Path drives an entity along a series of points in space rather than triggering a discrete event. Dragging a Motion Path action onto a track creates a default two-point straight-line path immediately, with diamond-shaped point markers rendered above the path in the viewport.

You can edit a Motion Path directly in 3D. Selecting it reveals a small viewport toolbar with Move, Rotate, and Scale gizmo tools, also reachable with the W, E, and R keys, letting you reposition, reorient, or resize whichever point is currently selected. There are four ways to create new points. Double-click anywhere along the path line in the viewport to divide that segment and insert a point at the click position. Double-click the point bar in the Inspector’s timeline to insert a point at a specific time instead of a specific position. With the last point in the path selected, clicking anywhere in 3D space extends the path by adding a new point at that click location — this is how you build out a path point by point. Finally, to close the path into a loop, select the last point and then click the first point; Reality Composer Pro connects the end of the path back to the start automatically.

Each point carries its own Position, Rotation ZYX, Scale, and Time values, plus an Ease Type that controls how the entity interpolates into that point. Reality Composer Pro offers several Ease Type options, from Linear for constant-speed motion to Ease In/Out variants that slow the entity down as it approaches or leaves a point — pick whichever curve best matches the motion you want, and adjust it later if the timing feels off.

To build a path manually from scratch, drag Motion Path from the Actions section onto a track, which creates the default two-point line. Select the Motion Path node on the timeline to bring up its properties in the Inspector, then use the viewport gizmos to move the existing points where you want them. Add more points by double-clicking along the path to divide it, or by selecting the last point and clicking further out in the viewport to extend the route. Once you’re happy with the shape, select the last point and then the first to close it into a loop if the motion should repeat seamlessly, and finally dial in each point’s Time and Ease Type in the Inspector so the motion speeds up and slows down where you want it.

#### Shape a Path with Orbit and Spin Modes

Rather than placing every point by hand, the Shape dropdown in the Motion Path Inspector can generate a path for you. Custom is the default — the manual, point-by-point mode described above. Orbit generates a circular or elliptical path and exposes its own Orbit Parameters group: Radius sets the orbit’s size in scene units, Number of Points sets how many points make up the generated path (a minimum of four), Spins Per Orbit sets how many full 360-degree rotations the entity makes around its own axis during one full orbit, and Spin Axis defines which axis that per-orbit spin happens around. Spin generates a path where the entity rotates in place around a central point rather than traveling a loop.

A handful of other Motion Path toggles apply regardless of shape. Look Along Path, when enabled, automatically orients the entity to face its direction of travel. Closed Shape connects the path’s end back to its start, the same result you’d get by manually closing a Custom path. Constant Speed keeps the entity moving at a uniform rate along the whole path regardless of how unevenly the points are spaced in time.

A generated shape still slots into a multi-track Sequence exactly like the manual path described above — pair it with an Enable/Disable Entity, Play Audio, or Billboard Blend track on a sub-track of the same entity to trigger those actions in sync with the motion. To build a Motion Path like this programmatically instead of through the Sequencer UI, see doc:automating-motion-path-creation-with-editor-scripting-commands.

#### Manage Overlapping Clips with Cross Fades

There’s a hard ceiling on how much overlap the cross-fade system supports: 0.75 seconds. Push an overlap past that threshold and the indicator switches to a warning icon, and the Sequencer reports the cross-fade as “Disabled” because it exceeds the maximum supported duration. If you see that warning, shorten the overlap rather than assuming the transition is still blending — past 0.75 seconds it isn’t. Below that threshold, the Sequencer shows a darker rounded region across the overlap with an icon marking it as a cross-fade, giving you immediate visual feedback while you nudge clips into position.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
- [Creating animation sequences for auto-play](creating-animation-sequences-for-autoplay.md)
  Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Build character animation state machines visually using the Animation Graph in Reality Composer Pro.
- [Building an advanced Animation Graph](building-an-advanced-animation-graph.md)
  Drive a character’s locomotion state machine from a Script Graph at runtime.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/building-multi-track-animation-sequences)*