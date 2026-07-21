# Reality Composer Pro Beta 4 Release Notes

**Framework**: Reality Composer Pro

Review known issues and changes in Reality Composer Pro 3.

#### Overview

Reality Composer Pro Beta 4 is a standalone app, available for download from the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/), and is no longer part of Xcode. Reality Composer Pro requires a Mac with Apple silicon running macOS Tahoe 26.5 or later.

##### Resolved Issues

- Fixed: When you enable `clearcoat`, specular occlusion is now visible. (175159311)
- Fixed: Light maps on cube and box primitives now render properly. (176278045)
- Fixed: The Particle Emitter inspector now includes the preset menu. Presets such as Fireworks, Impact, Magic, Rain, Snow, and Sparks can be applied from the editor. (165089607)

##### General

###### Known Issues

- Asset Generation is only supported on macOS 27. (178159978) - **Workaround:** Update to macOS 27.

##### Materials and Shaders

###### Known Issues

- A material that uses subsurface scattering (SSS weight greater than 0) with specular roughness below 1 renders black on surfaces facing away from a directional or spot light. This affects both the RealityKit PBR and OpenPBR surface nodes when the material’s lighting descriptors in the Material Inspector are left Unspecified. (180306610) - **Workaround:** In the ShaderGraph Material Descriptor Inspector, set lighting model to Lit, and Specular Model to GGX or GGX Anisotropy.

##### Script Graph

###### Known Issues

- “On Initialize” node can fail to start animation or audio on build and run. (182533099) - **Workaround:** Use the “On Activate” node to start audio and animation events.

##### Scripting and Shaders

###### Known Issues

- When using world position in scripts or shaders, Reality Composer Pro content shifts relative to the world origin in shared space apps. (178279067) - **Workaround:** Use relative position, or calculate the relationship of your content to the world origin and adjust your scripts or shaders accordingly. Refer to the Squirrel sample for examples.

##### Realitykit

###### Known Issues

- `ComputeGraphComponent` instances in a Reality file do not render when your app loads them. (177674901)

## See Also

- [Reality Composer Pro Release Notes](reality-composer-pro-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 2 Release Notes](reality-composer-pro-beta-2-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 3 Release Notes](reality-composer-pro-beta-3-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-beta-4-release-notes)*