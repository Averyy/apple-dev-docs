# Rendering reflections with fewer render passes

**Framework**: Metal

Use layer selection to reduce the number of render passes needed to generate an environment map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.13+
- Xcode 12.3+

#### Overview

This sample demonstrates dynamic reflections on a chrome sphere, using layer selection to render the frame in two passes. The first pass renders the environment onto the cube map. The second pass renders the environment reflections onto the sphere; it renders additional actors in the scene; and it renders the environment itself.

![Reflections with Layer Selection](https://docs-assets.developer.apple.com/published/e4a361c089b944adfd6aca1902e22f80/reflections-with-layer-selection-1-ReflectionsWithLayerSelections.png)

You can implement an object that reflects its environment by sampling its reflections from a cube map of the environment. A cube map is a single texture composed of six 2D texture layers arranged in the shape of a cube. The reflections vary based on the positions of other objects in the environment, so each of the cube map’s six faces needs to be rendered dynamically in every frame. This would normally require six separate render passes, one for each face, but Metal allows you to render an entire cube map in a single pass.

![Render Passes](https://docs-assets.developer.apple.com/published/257f04c7dc2202916dc67845aa682fdc/reflections-with-layer-selection-2-RenderPasses.png)

##### Getting Started

This sample contains macOS and iOS targets. Run the iOS scheme on a physical device because Metal isn’t supported in the simulator.

Layer Selection is supported on all macOS GPUs but only iOS GPUs which support the [`MTLFeatureSet.iOS_GPUFamily5_v1`](mtlfeatureset/ios_gpufamily5_v1.md) feature set.

You check the GPU that you choose at runtime supports indirect command buffers (ICBs) by calling an [`MTLDevice`](mtldevice.md) instance’s [`supportsFeatureSet(_:)`](mtldevice/supportsfeatureset(_:).md) method.

This sample calls ‘supportsFeatureSet:’ for this purpose within its view controller’s `viewDidLoad:` callback.

##### Separate the Scene

A cube map is represented as a render target array with six layers, one for each of its faces. The `[[render_target_array_index]]` attribute qualifier, specified for a structure member of a vertex function return value, identifies each array layer separately. This layer selection feature allows the sample to decide which part of the environment gets rendered to which cube map face.

An `AAPLActorData` object represents an actor in the scene. In this sample, each actor is a temple model with the same mesh data but a different diffuse color. These actors sit on the XZ-plane; they’re always reflected in the X or Z direction relative to the sphere and could be rendered to any of the +X, -X, +Z, or -Z faces of the cube map.

##### Perform Culling Tests for the Reflection Pass

Before rendering to the cube map, it’s useful to know which faces each actor should be rendered to. Determining this information involves a procedure known as a , and it’s performed on each actor for each cube map face.

At the start of every frame, for each cube map face, a view matrix is calculated and the view’s frustum is stored in the `culler_probe` array.

These culler probes test the intersection between an actor and the viewing frustum of each cube map face. The test results determine how many faces the actor is rendered to (`instanceCount`) in the reflection pass, and which faces (`instanceParams`) it’s rendered to.

The following diagram shows the results of the culling tests performed on the temple actors, based on their positions relative to the reflective sphere. Because `_actorData[0]` and `actorData[1]` bisect two viewing frustums, their `instanceCount` property is set to 2, and there are two elements in their `instanceParams` array. (This array contains the cube map face indices of the viewing frustums that the actors intersect.)

![Face Culling and Face Index Assignment](https://docs-assets.developer.apple.com/published/57d3d13eba123862fe54513ed0622919/reflections-with-layer-selection-3-CullingAndFaceIdxSelection.png)

##### Configure Render Targets for the Reflection Pass

The render target for the reflection pass is a cube map. The sample configures the render target by using a `MTLRenderPassDescriptor` object with a color render target, a depth render target, and six layers. The `renderTargetArrayLength` property sets the number of cube map faces and allows the render pipeline to render into any or all of them.

##### Issue Draw Calls for the Reflection Pass

The `drawActors:pass:` method sets up the graphics rendering state for each actor. Actors are only drawn if they are visible in any of the six cube map faces, determined by the `visibleVpCount` value (accessed through the `instanceCountInReflection` property). The value of `visibleVpCount` determines the number of instances for the instanced draw call.

In this draw call, the sample sets the `baseInstance` parameter to the value of `actorIdx * 5`. This setting is important because it tells the vertex function how to select the appropriate render target layer for each instance.

##### Render the Reflection Pass

In the `vertexTransform` vertex function, the `instanceParams` argument points to the buffer that contains the cube map faces that each actor should be rendered to. The `instanceId` value indexes into the `instanceParams` array.

The output structure of the vertex function, `ColorInOut`, contains the `face` member that uses the `[[render_target_array_index]]` attribute qualifier. The return value of `face` determines the cube map face that the render pipeline should render to.

Because the value of the draw call’s `baseInstance` parameter is set to `actorIdx * 5`, the `instanceId` value of the first instance drawn in the draw call is equal to this value. Each subsequent rendering of an instance increments the `instanceId` value by 1. The `instanceParams` array has five slots for each actor because an actor can be visible in up to five cube map faces. As a result, the `instanceParams[instanceId]` element always contains one of the face indices in which the actor is visible. Therefore, the sample uses this value to select a valid render target layer.

In summary, to render each actor to the reflective cube map, the sample issues an instanced draw call for the actor. The vertex function uses the built-in `instanceId` variable to index into the `instanceParams` array that contains the index of the cube map face that the instance should be rendered to. Therefore, the vertex function sets this face index in the `face` return value member, which uses the `[[render_target_array_index]]` attribute qualifier. This ensures that each actor is rendered to each cube map face it should appear in.

![Instanced Draw with render_target_array_index](https://docs-assets.developer.apple.com/published/866006843b2d022fc18816b0e78168b9/reflections-with-layer-selection-4-InstancedRenderingWithTargetIndex.png)

##### Perform Culling Tests for the Final Pass

The sample performs similar view updates for the main camera in the final pass. At the start of every frame, a view matrix is calculated and the view’s frustum is stored in the `culler_final` variable.

This final culler probe is used to test the intersection between an actor and the viewing frustum of the camera. The test result simply determines whether or not each actor is visible in the final pass.

##### Configure Render Targets for the Final Pass

The render target for the final pass is the view’s , a displayable resource obtained by accessing the view’s `currentRenderPassDescriptor` property. However, don’t access this property prematurely because it implicitly retrieves a drawable. Drawables are expensive system resources created and maintained by the Core Animation framework. Hold a drawable as briefly as possible to avoid resource stalls. In this sample, a drawable is acquired just before the final render pass is encoded.

##### Issue Draw Calls for the Final Pass

The `drawActors:pass`: method sets up the graphics rendering state for each actor. Actors are only drawn if they are visible to the main camera, as determined by the `visibleVpCount` value (accessed through the `visibleInFinal` property).

Because each actor is drawn only once in the final pass, the `instanceCount` parameter is always set to 1 and the `baseInstance` parameter is always set to 0.

##### Render the Final Pass

The final pass renders the final frame directly to the view’s drawable, which is then presented onscreen.

## See Also

- [Rendering a scene with forward plus lighting using tile shaders](rendering-a-scene-with-forward-plus-lighting-using-tile-shaders.md)
  Implement a forward plus renderer using the latest features on Apple GPUs.
- [Rendering a scene with deferred lighting in Objective-C](rendering-a-scene-with-deferred-lighting-in-objective-c.md)
  Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.
- [Rendering a scene with deferred lighting in Swift](rendering-a-scene-with-deferred-lighting-in-swift.md)
  Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.
- [Rendering a scene with deferred lighting in C++](rendering-a-scene-with-deferred-lighting-in-c++.md)
  Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/rendering-reflections-with-fewer-render-passes)*