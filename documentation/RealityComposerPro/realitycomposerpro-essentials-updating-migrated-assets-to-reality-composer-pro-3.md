# Updating migrated assets to Reality Composer Pro 3

**Framework**: Reality Composer Pro

Fix common problems that appear after migrating a project from Reality Composer Pro 2 to Reality Composer Pro 3.

#### Overview

This article walks through the changes to expect in each asset type after migrating a project from Reality Composer Pro 2 to Reality Composer Pro 3.

This article focuses on specific areas such as animation, materials, and audio.

See [`Migrating older projects to Reality Composer Pro 3`](realitycomposerpro-essentials-migrating-older-projects-to-reality-composer-pro-3.md) for more information about how migration works and what to expect.

#### Rewire Usd Authored Animations

You usually need to rewire animations by hand. Only entities that already had a [`AnimationLibraryComponent`](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent) migrate with animations fully wired.

Reality Composer Pro 3 imports USD-authored animations as an asset but doesn’t automatically attach them to the entity. If the Reality Composer Pro 2 scene already contained an explicit `AnimationLibraryComponent`, migration rebuilds the component and links the clips. If you authored your Reality Composer Pro 2 animation in USD using time samples on transforms, skeletal animation, and blendshape weights, then migrating to Reality Composer Pro 3 creates an animation/Timeline asset for it but does not add an `AnimationLibraryComponent` to the entity.

After they are migrated, the animation assets exist in the Project Browser, but the entity doesn’t play anything automatically. This is because in RealityKit, playback requires an `AnimationLibraryComponent` that references the clip.

To restore the animation in Reality Composer Pro 3, select the entity, add an `AnimationLibraryComponent`, and then point it to the migrated animation clip. Additional considerations:

- Reality Composer Pro 3 imports migrated animations set to loop forever (loop count `0`) but plays them only once. In Reality Composer Pro 3, when you configure an `AnimationLibraryComponent` with animations and select an individual animation, you can configure the individual animation further under Clip and toggle Repeats Forever (bool) and set Repeat Mode to None, Repeat, or Auto Reverse.
- Joint-name migration only succeeds when each animation/skinning maps to exactly one skeleton. If it’s ambiguous, Reality Composer Pro 3 leaves those assets unmigrated and shows an error telling you to reimport them.

> **Note**: During migration, joint name separators change from underscores to slashes.

#### Review Migrated Sequences and Rebuild Actions

Reality Composer Pro 2 Timelines (tracks of actions) migrate into Reality Composer Pro 3 Sequences, but only three action types survive: Enable/Disable Entity, Play Audio, and Billboard. Reality Composer Pro 3 removes everything else (Add Force, Animation, Emphasize, Hide/Show, Notification, Orbit, Spin, Transform By/To, Replace Behaviors, and other action types) and shows the message: “Unsupported Actions Detected — Some Actions are not supported and will be removed from the generated sequences. Review the sequences after import to resolve any issues.” To fix this, review every migrated Sequence and rebuild the dropped actions using Reality Composer Pro 3’s tools (Sequences, Behavior Trees, Script Graph, Motion Paths, and other action types).

#### Move Audio Files Outside the Scene Hierarchy

In Reality Composer Pro 2, you dragged audio files from the Project Browser into the hierarchy so audio components could reference them. In Reality Composer Pro 3, audio files in the Project Browser are already accessible to every component in the hierarchy, and you create Audio File Groups in the Project Browser instead of the hierarchy.

#### Add a Component to Access the Audio Mixer

While Reality Composer Pro 2 provided a global Audio Mixer UI with level metering on the stereo output, Reality Composer Pro 3 does not. In Reality Composer Pro 3, place an [`AudioMixGroupsComponent`](https://developer.apple.com/documentation/realitykit/audiomixgroupscomponent) on an entity to access the Audio Mixer. If you have multiple `AudioMixGroupsComponent` instances on different entities, they stay in sync. Add Mix Groups through the component or from the Project Browser. Assign sounds to the Mix Group through the `AudioMixGroupsComponent`, or through the Project Browser. See [`Adding audio components in Reality Composer Pro`](introduction-to-reality-composer-pro-audio.md) to learn more.

#### Fix Migrated Materials That Render Incorrectly

If a migrated material looks untextured, miscolored, or otherwise incorrect, check the following:

- Make sure textures aren’t missing. If you move or rename a texture file after authoring the Reality Composer Pro 2 project, the importer can’t find it. There’s no dialog and no auto-relink, and the material falls back to a default value. The import error surfaces in Reality Composer Pro 3’s in-app Console.
- Verify that the material’s shader graph is reading the correct UV channel.
- Make sure you remap the normal texture to tangent space before connecting it to a normal field for shader graph.
- Verify that every texture path resolves, and open the Reality Composer Pro 3 Console tab (located next to the Project Browser tab by default) for any import errors.

#### Make Materials Occlude By Defining Their Shader Type

In Reality Composer Pro 2, you authored occlusion in a shader graph using the Occlusion Surface and Shadow Receiver Surface nodes. These nodes are no longer part of the shader graph node library in Reality Composer Pro 3. Occlusion describes an intent instead of a surface appearance, so there is no per-pixel result to author. To create an Occlusion material, first create a new material in the Project Browser or select an existing one, then set Shader to Occlusion in the Inspector.

See [`Building materials in Reality Composer Pro`](building-materials-in-reality-composer-pro.md) to learn more.

#### Verify Texture Transform and Color Space Properties

Reality Composer Pro 3 handles textures differently than Reality Composer Pro 2. Textures in Reality Composer Pro 3 are now standalone assets with their own settings. In Reality Composer Pro 2, an image offered little control of its own, and connecting it to a material determined how Reality Composer Pro 2 interpreted its data.

Reality Composer Pro 3 now applies transform, color space, and compression to the texture as soon as it imports the file, and every material that references the texture shares the resulting compiled result. Because Reality Composer Pro 3 determines interpretation once per texture, any number of materials can share the resulting compiled texture, and you can inspect, change, or correct it from one location.

If a texture does not look right, check Transform, Color Space, and Compression on the texture asset before looking at the material. Washed out or overly dark color, incorrect surface detail, banded masks, and blocky gradients usually trace back to an inferred setting that does not match the image’s intent.

Because inference depends on the texture’s file name and how the image is connected, Reality Composer Pro 3 is most likely to infer settings incorrectly for images with unusual names or images used in ways that differ from their content. Review these settings first for textures brought in from earlier projects. Reality Composer Pro 3 infers these settings at import time, so most content doesn’t need to be set up manually. Two things drive the inference: the texture’s file name, which Reality Composer Pro 3 matches against a set of naming patterns, and the material input the image is connected to.

- Reality Composer Pro 3 assigns the Color transform to images feeding color inputs such as base color, emissive color, or specular color.
- Reality Composer Pro 3 assigns the Mask transform to single-channel data inputs such as roughness, metallic, opacity, clearcoat, and ambient occlusion.
- Reality Composer Pro 3 assigns the Normal transform to a normal input. When neither the name nor the connection resolves to something more specific, the texture falls back to the Color transform. Select a texture in the Project Browser and its settings appear in the Inspector, and then check the following:
- Transform selects how Reality Composer Pro 3 interprets the image data, with options including Color, Normal, Mask, Cubemap, Default, and Identity.
- Color Space controls how Reality Composer Pro 3 reads the stored values.
- The Transform Settings group holds options such as Compression and Resize. Edits apply to the texture asset, so every material referencing it updates. These settings live on the asset and are shared, so there is no per-material override of a texture’s Transform, Color Space, or Compression. When one image needs two different interpretations in the same project, import the file a second time or duplicate the texture asset so each copy carries its own settings.

#### Fix Texture Coordinates and Uv Sets

If UV slots collide, it means a material is sampling a different UV set than the one intended, and textures appear misplaced, stretched, or mirrored. To diagnose it, open the material’s shader graph and look at the nodes feeding the UV input of the affected texture rather than at the image node itself. If a Texture Coordinates node does not produce the expected result, replace it with the 2D vector variant of the Primvar Reader node, and set its `Varname` to the name of the authored texture coordinate. This reads the mesh’s primary UV set by name instead of relying on slot resolution.

> 💡 **Tip**: If you don’t know the name of the texture coordinate’s `primvar`, open the imported geometry and expand the primvars section.

#### Manage Material References and Overrides

In Reality Composer Pro 3, assigning a material to a material slot on an entity’s model component creates a reference to the material asset. Editing a property in the Inspector edits that asset, and the change appears on every entity and in every scene that uses it. A Reality Composer Pro 3 project is a database of assets. Choosing an asset in any picker creates a reference to that asset, not a copy and not an override.

> **Note**: The same rule applies wherever you pick an asset, not just to materials. To make a local override: In the Project Browser, Control-click an asset and then click Instantiate. This creates a new asset named after the original with `(instance)` appended, which you then assign to the material slot. Note: An instance inherits values from its prototype and follows prototype changes, and overriding a property on the instance breaks the link for that property only. Duplicate the material instead when the copy should be fully independent of the original. Tip: Choose carefully which asset a slot points to before editing it. There is no implicit per-material override.

#### Migrate Particle Systems

When you open a Reality Composer Pro 2 project in Reality Composer Pro 3, Reality Composer Pro 3 migrates the component automatically. However, be aware of the following differences between Reality Composer Pro 3 and Reality Composer Pro 2 Particle Emitter components:

- Reality Composer Pro 3 has no per-emitter playback like Reality Composer Pro 2. The Simulate (Play) button on the scene plays all the particles in the scene that have Simulation State set to Play, and you control playing, pausing, or stopping a Particle Emitter component using that same Simulation State property.
- Reality Composer Pro 3 also has no Burst button to trigger and visualize particle bursts for an emitter as there is in Reality Composer Pro 2. It splits Reality Composer Pro 2’s combined color controls into individual color properties for the main and spawned particles, and displays all variation properties individually.

For more information about working with the Reality Composer Pro 3 Particle Emitter component, see [`Creating particle systems in Reality Composer Pro`](creating-particle-systems-in-reality-composer-pro.md).

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Migrating older projects to Reality Composer Pro 3](realitycomposerpro-essentials-migrating-older-projects-to-reality-composer-pro-3.md)
  Bring existing Reality Composer Pro 2 projects into the Reality Composer Pro 3 workspace.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Explore the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Use Reality Composer Pro’s node-based editor to build materials, animations, audio effects, and scripts without writing code.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Edit a prototype once and propagate the change to every placement of that asset in a scene.
- [Previewing content and running simulations](realitycomposerpro-essentials-previewcontentrunsimulations.md)
  Test and iterate on your scenes directly in Reality Composer Pro, with or without a linked Xcode project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-updating-migrated-assets-to-reality-composer-pro-3)*