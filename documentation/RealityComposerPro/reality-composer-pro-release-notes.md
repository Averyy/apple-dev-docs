# Reality Composer Pro Release Notes

**Framework**: Reality Composer Pro

Review known issues and changes in Reality Composer Pro 3.

#### Overview

Reality Composer Pro is a standalone app, available for download from the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/reality-composer-pro/), and is no longer part of Xcode. Reality Composer Pro requires a Mac with Apple silicon running macOS Tahoe 26.5 or later.

##### General

###### Known Issues

- Asset Generation is only supported on macOS 27. (178159978) - **Workaround:** Update to macOS 27.

##### Materials and Shaders

###### Known Issues

- Imported asset’s shader graph fails on normal map. (184117276)

##### 3d Modeling

###### Known Issues

- Adding a Mesh Resource type to the Model Mesh field causes the entity to flicker on screen and primitive geometry shapes to no longer load. (185447536) - **Workaround:** Save the project and relaunch Reality Composer Pro 3.

##### Rcp Assist

###### Known Issues

- RCP Assist creates a ShaderGraph (MaterialX 1.38) material instead of Physically Based when explicitly asked to create a Physically Based material type. (184871460)

##### Scripting and Shaders

###### Known Issues

- When using world position in scripts or shaders, Reality Composer Pro content shifts relative to the world origin in shared space apps. (178279067) - **Workaround:** Use relative position, or calculate the relationship of your content to the world origin and adjust your scripts or shaders accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-release-notes)*