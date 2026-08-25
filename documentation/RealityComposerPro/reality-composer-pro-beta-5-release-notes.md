# Reality Composer Pro Beta 5 Release Notes

**Framework**: Reality Composer Pro

Review known issues and changes in Reality Composer Pro 3.

#### Overview

Reality Composer Pro Beta 5 is a standalone app, available for download from the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/), and is no longer part of Xcode. Reality Composer Pro requires a Mac with Apple silicon running macOS Tahoe 26.5 or later.

##### Resolved Issues

- Fixed: A material that uses subsurface scattering (SSS weight greater than 0) with specular roughness below 1 no longer renders black on surfaces facing away from a directional or spot light. (180306610)
- Fixed: `ComputeGraphComponent` instances in a Reality file now render when your app loads them. (177674901)

##### General

###### Known Issues

- Asset Generation is only supported on macOS 27. (178159978) - **Workaround:** Update to macOS 27.

##### Materials and Shaders

###### Known Issues

- Imported asset’s shader graph fails on normal map. (184117276)

##### 3d Modeling

###### Known Issues

- Adding a Mesh Resource type to the Model Mesh field causes the entity to flicker on screen and primitive geometry shapes to no longer load. (185447536)

##### Rcp Assist

###### Known Issues

- RCP Assist creates a ShaderGraph (MaterialX 1.38) material instead of Physically Based when explicitly asked to create a Physically Based material type. (184871460)

##### Script Graph

###### Known Issues

- “On Initialize” node can fail to start animation or audio on build and run. (182533099) - **Workaround:** Use the “On Activate” node to start audio and animation events.

##### Scripting and Shaders

###### Known Issues

- When using world position in scripts or shaders, Reality Composer Pro content shifts relative to the world origin in shared space apps. (178279067) - **Workaround:** Use relative position, or calculate the relationship of your content to the world origin and adjust your scripts or shaders accordingly. Refer to the Squirrel sample for examples.

##### Preview on Visionos

###### Known Issues

- Textures in a scene may not load, leaving objects with a flat grey appearance. (182734493) - **Workaround:** For textures to load correctly, enter immersive mode and then exit it.

##### Migration

###### Known Issues

- Migrating Reality Composer Pro 2 projects with timelines fails. (184861508)

## See Also

- [Reality Composer Pro Release Notes](reality-composer-pro-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 2 Release Notes](reality-composer-pro-beta-2-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 3 Release Notes](reality-composer-pro-beta-3-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 4 Release Notes](reality-composer-pro-beta-4-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-beta-5-release-notes)*