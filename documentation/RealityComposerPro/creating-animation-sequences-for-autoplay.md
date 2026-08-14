# Creating animation sequences for auto-play

**Framework**: Reality Composer Pro

Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.

#### Overview

Building on the Root Entity rule from [`Building multi-track animation sequences`](building-multi-track-animation-sequences.md), this article covers wiring a finished Sequence for auto-play. That rule governs how the Sequence, its tracks, and the Animation Library Component relate to each other throughout this article. A Sequence only appears in an entity’s Animation Library Component “available clips” list when the Sequence’s Root Entity is that same entity, or its prototype. Unless the Sequence is rooted where its Animation Library Component expects to find it, the tracks and actions you author at runtime go to waste. The Animation Library Component has to live on the entity the Sequence is rooted at — not on a parent, not on a child, not on some other entity that happens to reference the same assets.

![Screenshot of the Autoplay toggle in Reality Composer Pro Inspector in an Animation Library.](/images/RealityComposerPro/AnimationLibraryAutoplay@2x.png)

The failure mode is quiet rather than loud. If you put the Animation Library Component on the wrong entity, the Sequence simply won’t be selectable from that component’s clip dropdown — there’s no error explaining why it’s missing. If you try to use an entity’s Animation Library Component that has no eligible clips, the UI shows “No entries found in Animation Library Component for this entity.” From editor-scripting commands, the equivalent failure is `edit_entry_in_animation_library_component` reporting “no animations available” when it tries to bind a Sequence that isn’t rooted at the entity holding the component.

There are exactly two fixes. Either move the Animation Library Component onto the entity that is the Sequence’s actual Root Entity, or leave the component where it is and recreate the Sequence with its Root Entity set correctly to match. Which fix makes sense depends on which side you set up incorrectly. Either way, you must change one side to match the other.

#### Wire a Sequence for Auto Play

With the Root Entity rule satisfied, wiring auto-play is a short sequence of steps in the Animation Library Component’s own Inspector panel. Click the Add Animation Entry button — the plus icon at the bottom of the component — to create a new entry, which starts out with the placeholder name “Empty.”

![Screenshot of an animation library with an empty placeholder in the list of animations.](/images/RealityComposerPro/AnimationLibrary1@2x.png)

Click the entry’s dropdown on the right side to choose its source: this list includes both animation clips embedded in the entity’s USD asset and any Sequences whose Root Entity is this entity or its prototype, side by side in the same picker. Selecting your finished Sequence from that list automatically renames the entry to match, though you can still rename it manually later by double-clicking the name field.

![Screenshot of adding a sequence in a Reality Composer Pro animation library.](/images/RealityComposerPro/AnimationLibraryAdd@2x.png)

> 💡 **Tip**: Once at least one entry has an assigned animation, the Auto Play toggle appears on the component — it’s hidden entirely before that point, since there’s nothing to auto-play. Turn it on, and a Default Animation dropdown appears alongside it; use that dropdown to choose which entry plays automatically when the entity is added to the scene and enabled.

To walk through this end to end: build a Sequence rooted at the entity you want to animate, using tracks, actions, and a Motion Path as described in [`Building multi-track animation sequences`](building-multi-track-animation-sequences.md). Add an Animation Library Component to that same entity — not a different one — through the Inspector’s Add Component menu, under Animation > Animation Library. Click Add Animation Entry, and in the new entry’s dropdown select your Sequence by name. Turn on Auto Play, and in the Default Animation dropdown that appears, choose the entry you just created. From this point on, the entity plays your Sequence automatically as soon as it’s active in the scene, with no additional script required to kick off playback.

At runtime, the same entries are also reachable directly through [`AnimationLibraryComponent`](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent) — Auto Play simply means RealityKit makes that call for you.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-animation-sequences-for-autoplay)*