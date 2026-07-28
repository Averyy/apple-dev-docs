# Creating animation sequences for auto-play

**Framework**: Reality Composer Pro

Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.

#### Overview

Building on the Root Entity rule from [`Building multi-track animation sequences`](building-multi-track-animation-sequences.md), this article covers wiring a finished Sequence for auto-play. That rule governs how the Sequence, its tracks, and the Animation Library Component relate to each other throughout this article. A Sequence only appears in an entity’s Animation Library Component “available clips” list when the Sequence’s Root Entity is that same entity, or its prototype. Unless the Sequence is rooted where its Animation Library Component expects to find it, the tracks and actions you author at runtime go to waste. The Animation Library Component has to live on the entity the Sequence is rooted at — not on a parent, not on a child, not on some other entity that happens to reference the same assets.

![Screenshot of the Autoplay toggle in Reality Composer Pro Inspector in an Animation Library.](https://docs-assets.developer.apple.com/published/571df0374c19716392e52cc65a5fb7f0/AnimationLibraryAutoplay%402x.png)

The failure mode is quiet rather than loud. If you put the Animation Library Component on the wrong entity, the Sequence simply won’t be selectable from that component’s clip dropdown — there’s no error explaining why it’s missing. If you try to use an entity’s Animation Library Component that has no eligible clips, the UI shows “No entries found in Animation Library Component for this entity.” From editor-scripting commands, the equivalent failure is `edit_entry_in_animation_library_component` reporting “no animations available” when it tries to bind a Sequence that isn’t rooted at the entity holding the component.

There are exactly two fixes. Either move the Animation Library Component onto the entity that is the Sequence’s actual Root Entity, or leave the component where it is and recreate the Sequence with its Root Entity set correctly to match. Which fix makes sense depends on which side you set up incorrectly. Either way, you must change one side to match the other.

#### Wire a Sequence for Auto Play

With the Root Entity rule satisfied, wiring auto-play is a short sequence of steps in the Animation Library Component’s own Inspector panel. Click the Add Animation Entry button — the plus icon at the bottom of the component — to create a new entry, which starts out with the placeholder name “Empty.”

![Screenshot of an animation library with an empty placeholder in the list of animations.](https://docs-assets.developer.apple.com/published/ca7c56e452a0261afa9de0ecf5f8e495/AnimationLibrary1%402x.png)

Click the entry’s dropdown on the right side to choose its source: this list includes both animation clips embedded in the entity’s USD asset and any Sequences whose Root Entity is this entity or its prototype, side by side in the same picker. Selecting your finished Sequence from that list automatically renames the entry to match, though you can still rename it manually later by double-clicking the name field.

![Screenshot of adding a sequence in a Reality Composer Pro animation library.](https://docs-assets.developer.apple.com/published/adf6632b78f8df977e12aefd928afb42/AnimationLibraryAdd%402x.png)

> 💡 **Tip**: Once at least one entry has an assigned animation, the Auto Play toggle appears on the component — it’s hidden entirely before that point, since there’s nothing to auto-play. Turn it on, and a Default Animation dropdown appears alongside it; use that dropdown to choose which entry plays automatically when the entity is added to the scene and enabled.

To walk through this end to end: build a Sequence rooted at the entity you want to animate, using tracks, actions, and a Motion Path as described in [`Building multi-track animation sequences`](building-multi-track-animation-sequences.md). Add an Animation Library Component to that same entity — not a different one — through the Inspector’s Add Component menu, under Animation > Animation Library. Click Add Animation Entry, and in the new entry’s dropdown select your Sequence by name. Turn on Auto Play, and in the Default Animation dropdown that appears, choose the entry you just created. From this point on, the entity plays your Sequence automatically as soon as it’s active in the scene, with no additional script required to kick off playback.

At runtime, the same entries are also reachable directly through [`AnimationLibraryComponent`](https://developer.apple.com/documentation/RealityKit/AnimationLibraryComponent) — Auto Play simply means RealityKit makes that call for you.

#### Wire Auto Play with Editor Scripting Commands

The Animation Library side of this workflow has its own editor-scripting commands, and they’re designed to chain directly onto the output of the Motion Path recipe in [`Automating motion path creation with editor-scripting commands`](automating-motion-path-creation-with-editor-scripting-commands.md). The relevant commands are `create_prototype_assets`, `add_animation_library_component_to_entity`, `add_entry_to_animation_library_component`, `edit_entry_in_animation_library_component`, and `edit_animation_library_component`.

Picking up where the Orbit Motion Path recipe described in [`Automating motion path creation with editor-scripting commands`](automating-motion-path-creation-with-editor-scripting-commands.md) left off — a Sequence already exists, rooted at a `Generated Prototypes/<name>` prototype — wiring it for auto-play continues the same chain.

If the prototype doesn’t already have an Animation Library Component, `add_animation_library_component_to_entity` adds one; it errors if the entity already has one, so check first with a scene query and skip this call if a component is already present.

Next, `add_entry_to_animation_library_component`, given the prototype entity and an `entryName` of your choosing, adds an empty named entry to the component. Then `edit_entry_in_animation_library_component` binds the Sequence to that entry, taking the entity, the same `entryName`, and a `newClipName`.

This is the one place the two recipes’ outputs actually meet. It’s also where the gotcha from the Root Entity rule reappears in scripted form: `newClipName` must be the Sequence’s display name — something like “Sequence (1)” — never the opaque asset id token that `add_sequence` returned back in the Motion Path recipe. Finally, `edit_animation_library_component`, given the entity, `autoPlay = true`, and `defaultAnimationName` set to your entry name, turns on Auto Play with that entry as the default.

Chained together, the two recipes form one continuous programmatic path. `create_prototype_assets` turns a runtime entity into a rootable asset. `add_sequence` through `edit_path_orbit_parameters` build and shape the orbiting Motion Path on that asset. `add_animation_library_component_to_entity` through `edit_animation_library_component` wire the finished Sequence into that same asset’s Animation Library, so it plays the moment the entity becomes active, without opening the Sequencer UI at all. The same Root Entity constraint governs both halves: because the Sequence was rooted at the prototype in step two of the first recipe, the Animation Library Component in this second recipe has to live on that identical prototype for `edit_entry_in_animation_library_component` to find it as an available clip.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-animation-sequences-for-autoplay)*