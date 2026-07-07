# Reality Composer Pro Beta 3 Release Notes

**Framework**: Reality Composer Pro

Review known issues and changes in Reality Composer Pro 3.

#### Overview

Reality Composer Pro Beta 3 is a standalone app, available for download from the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/), and is no longer part of Xcode. Reality Composer Pro requires a Mac with Apple silicon running macOS Tahoe 26.5 or later.

##### Resolved Issues

- Fixed: After enabling the experimental feature “Assistant for ShaderGraph,” the feature now activates without requiring a restart. (177106224)
- Fixed: When switching between shader types, the Portal preview panel now correctly refreshes and displays the Portal material. (177742196)
- Fixed: Graph variables no longer appear as an option in ShaderGraph. (178161668)
- Fixed: Nodes now display their title and description correctly. (178162061)
- Fixed: Using the LOD Generator or simplifying meshes with baked lighting no longer produces visual glitches. (174362762)
- Fixed: Xcode projects exported from Reality Composer Pro using “Run with Xcode” no longer require macOS 27. (178199201)

##### General

###### Known Issues

- Asset Generation is only supported on macOS 27. (178159978) - **Workaround:** Update to macOS 27.

##### Materials and Shaders

###### Known Issues

- When you enable `clearcoat`, specular occlusion is not visible. (175159311) - **Workaround:** Lower the `clearcoat` value to near zero, or set it to zero, to make specular occlusion visible.
- A material that uses subsurface scattering (SSS weight greater than 0) with specular roughness below 1 renders black on surfaces facing away from a directional or spot light. This affects both the RealityKit PBR and OpenPBR surface nodes when the material’s lighting descriptors in the Material Inspector are left Unspecified. (180306610) - **Workaround:** In the ShaderGraph Material Descriptor Inspector, set lighting model to Lit, and Specular Model to GGX or GGX Anisotropy.

##### 3d Asset Editing

###### Known Issues

- Light maps on cube and box primitives do not render properly. (176278045) - **Workaround:** Import explicitly modeled meshes with non-overlapping UVs instead of USD primitives or RealityKit box mesh resources. Use this approach when you need specific UV requirements, such as no overlaps over the entire model.

##### Scripting and Shaders

###### Known Issues

- When using world position in scripts or shaders, Reality Composer Pro content shifts relative to the world origin in shared space apps. (178279067) - **Workaround:** Use relative position, or calculate the relationship of your content to the world origin and adjust your scripts or shaders accordingly. Refer to the Squirrel sample for examples.

##### Particle Emitter

###### Known Issues

- The Particle Emitter inspector does not include the preset menu from Reality Composer Pro 2. Presets such as Fireworks, Impact, Magic, Rain, Snow, and Sparks cannot be applied from the editor, so you build each particle effect by configuring the component’s properties individually. (165089607) - **Workaround:** Configure the emitter manually in the inspector, or apply a preset programmatically using `ParticleEmitterComponent/Presets`.

##### Realitykit

###### Known Issues

- `ComputeGraphComponent` instances in a Reality file do not render when your app loads them. (177674901)

## See Also

- [Reality Composer Pro Release Notes](reality-composer-pro-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 2 Release Notes](reality-composer-pro-beta-2-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-beta-3-release-notes)*