# Reality Composer Pro Release Notes

**Framework**: Reality Composer Pro

Review known issues and changes in Reality Composer Pro 3.

#### Overview

Reality Composer Pro Beta is now a standalone app you can download from the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/) and is no longer part of Xcode. Reality Composer Pro requires a Mac with Apple silicon running macOS Tahoe 26.5 or later.

##### General

###### Known Issues

- After enabling the experimental feature “Assistant for ShaderGraph,” the feature does not activate until you restart Reality Composer Pro. (177106224) - **Workaround:** Restart Reality Composer Pro after enabling the feature.
- Asset Generation requires macOS 27. (178159978) - **Workaround:** Update to macOS 27.

##### Materials and Shaders

###### Known Issues

- When you enable `clearcoat`, specular occlusion might not be visible. (175159311) - **Workaround:** Lower the `clearcoat` value to near zero, or set it to zero, to make specular occlusion visible.
- When switching between shader types, the Portal preview panel sometimes fails to refresh and display the Portal material. (177742196)
- The current beta allows graph variables in ShaderGraph. This is not a valid option, and a future release removes it. (178161668)
- Some nodes lack title and description in the current beta. This does not affect their behavior or functionality. (178162061)

##### 3d Asset Editing

###### Known Issues

- Light maps on cube and box primitives might not render properly. (176278045) - **Workaround:** Import explicitly modeled meshes with non-overlapping UVs instead of USD primitives or RealityKit box mesh resources. Use this approach when you need specific UV requirements, such as no overlaps over the entire model.
- Using the LOD Generator or simplifying meshes with baked lighting may produce visual glitches. (174362762) - **Workaround:** Avoid using the LOD Generator and baked lighting on the same mesh.

##### Audio

###### Known Issues

- Audio functionality requires the Audio Library component to be on the same entity as the audio source. (174520828) - **Workaround:** Place an Audio Library component on each entity that has a Spatial, Ambient, or Channel Audio component for the files intended to play from that source.

##### Scripting and Shaders

###### Known Issues

- When using world position in scripts or shaders, Reality Composer Pro content shifts relative to the world origin in shared space apps. (178279067) - **Workaround:** Use relative position, or calculate the relationship of your content to the world origin and adjust your scripts or shaders accordingly.

##### Plugins

###### Known Issues

- Plugin support is not available in the current beta. (178086142)

##### Preview on Visionos

###### Known Issues

- Reality Composer Pro Preview, which lets you preview your content on visionOS in real time directly from your Mac, is not yet available. (178172509)

##### Particle Emitter

###### Known Issues

- The Particle Emitter inspector does not provide the preset menu that was available in Reality Composer Pro 2. Presets such as Fireworks, Impact, Magic, Rain, Snow, and Sparks cannot be applied from the editor. (165089607) - **Workaround:** Configure the emitter manually in the inspector, or apply a preset programmatically using `ParticleEmitterComponent.Presets`.

##### Assistant

###### Known Issues

- AI models for 3D object and texture generation might download incorrectly, preventing the feature from working. (178649074) - **Workaround:** Clear out the Reality Composer Pro container.

##### Xcode Integration

###### Known Issues

- Xcode projects exported from Reality Composer Pro using “Run with Xcode” require macOS 27. On macOS 26.5, the app does not launch correctly. (178199201) - **Workaround:** Build and run on macOS 27.

##### Realitykit

###### Known Issues

- `ComputeGraphComponent` instances stored in a Reality file do not render when you load the file. (177674901)

## See Also

- [Reality Composer Pro Beta 2 Release Notes](reality-composer-pro-beta-2-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 3 Release Notes](reality-composer-pro-beta-3-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-release-notes)*