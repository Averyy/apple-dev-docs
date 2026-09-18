# Gaussian Splat Rendering Guidelines

**Framework**: RealityKit

Improving performance and watching thermal state when rendering Gaussian splats

#### Overview

Gaussian splats capture volumetric imagery using a 3D cloud of partially transparent ellipsoids (splats). During scene capture and training, splats’ colors are accumulated from multiple views of the 3D scene and stored with each splat in the form of Red, Green, and Blue weights for spherical harmonics functions. Mixtures of spherical harmonics blend between different views with an accuracy depending on the number of harmonics, with 16 coefficients per color being typical. Each splat stores its position, size and orientation data, as well as the 48 directional color values, so splat data can get very large. And Gaussian splat scenes may have large numbers of splats that require alpha blending to render correctly. This can lead to high rendering cost, which the system mitigates in various ways. It can also lead to excessive heating, so apps should monitor the thermal state of the device, and reduce rendering load to keep things comfortable. Adapting your app’s rendering in response to system state changes can improve your users’ experience.

##### Render Throttling

The `GaussianSplatComponent` renders the 3D Gaussian splat asset contained in its `GaussianSplatResource`. These Gaussian splat assets can vary in rendering cost by orders of magnitude. To allow large assets without unbounded GPU cost, the renderer applies internal mitigations and emits an event indicating that the rendering is being throttled. Apps should listen for this event, in order to reduce the asset complexity as needed. The `GaussianSplatEvents.RenderingChanged` event is published on the entity that owns the affected `GaussianSplatComponent`. Subscribers receive the entity and the state change that occurred. They can read its current `GaussianSplatComponent` state if they want context, but the event itself does not describe what mitigation the renderer applied, in the limited case.

##### Monitoring Thermal State

High compute load due to particularly demanding content may cause a device to become uncomfortably warm. While the system will throttle rendering to preserve frame rate, ***it is up to the developer to mitigate thermal impact***.  Apps should stay cool by observing the `NotificationCenter thermalStateDidChangeNotification`, and taking steps to reduce the load if the `ProcessInfo.thermalState` reaches serious or critical. The system will *not* automatically limit the rendering of an entity’s `GaussianSplatResource` in response to thermal state, so it is incumbent on developers to reduce the entity complexity until the thermal state has returned to fair or better.

##### Reducing Gaussian Splat Complexity

Much of the rendering cost of Gaussian splats is due to overdraw of numerous partially transparent splats. While much research effort goes into producing further optimized splats, some relatively simple approaches may reduce complexity with acceptable quality tradeoffs. Approaches to consider include truncating, decimating, or downsampling splat clouds, or culling less significant splats. Producing lower level of detail versions of splat assets may allow you to preserve performance when the system thermal levels or throttling state point to excessive rendering demands.

###### Truncating

For `GaussianSplatResource` objects initialized with a PLY file, truncating the splat cloud requires truncating the contents of the PLY file. Various open source libraries are available which can read and write PLY files, and thus save versions with truncated point lists.

###### Decimating

Decimating requires removing splats from the list in a more complex fashion, like removing every Nth splat, or removing random splats. Since most splats are ordered haphazardly, the effect may not be noticeably different from truncation. Because the splats vary in significance, the quality is likely to be sensitive to exactly which splats are removed. Compare results from multiple techniques to find the best quality for a given splat count.

###### Downsampling

Downsampling a splat cloud is typically accomplished by defining a 3D grid of ‘voxels’ in the scene’s volume, and keeping one splat per voxel. This has the advantage of removing splats evenly throughout the scene, and giving control over the resolution of features. Splats within a voxel may be merged or removed based on size, opacity, or other factors.

###### Culling

Splats can capture subtle lighting and atmospheric effects, among others, by including a lot of mostly transparent splats. For many assets a large number of the most transparent splats can be removed without unacceptably impairing the visual quality. Culling very small splats can also cut scene size with limited damage. This level of processing will require more complete parsing of the asset’s PLY file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussian-splat-rendering-guidelines)*