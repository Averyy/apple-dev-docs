# Rendering terrain dynamically with argument buffers

**Framework**: Metal

Use argument buffers to render terrain in real time with a GPU-driven pipeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.13+
- Xcode 13.1+

#### Overview

This sample demonstrates dynamic terrain generation on an outdoor landscape, using argument buffers to select terrain materials, vegetation geometry, and particle effects within a GPU-driven pipeline. The sample creates a landscape with visually distinct areas, called habitats, that differ based on the land’s elevation. These are the habitats in the sample, ordered from highest to lowest elevation:

- Snow
- Rock
- Grass
- Sand

![Screenshot of the sample app running to show the different habitats visually.](https://docs-assets.developer.apple.com/published/99d45f3f5b748f9b4ac9dfcc8e81e6ec/dynamic-terrain-with-argument-buffers-1-screenshot.png)

> **Note**: This sample reduces the overhead of encoding commands on the CPU by using argument buffers. For an introduction to argument buffers, see the samples listed in [`Buffers`](buffers.md).

##### Getting Started

The Xcode project contains schemes for running the sample in macOS and iOS. Metal isn’t supported in the iOS Simulator, so the iOS scheme requires a physical device that supports GPU family 4 to run the sample. The default scheme is macOS, which runs the sample as is on your Mac.

In macOS, use these controls to navigate the scene:

-  Move the camera body.
-  Move the camera view.
-  Move the camera view.
-  Raise the terrain.
-  Lower the terrain.

In iOS, use these controls to navigate the scene:

-  Move the camera view.
-  Cycle through a predefined terrain manipulation sequence.

> **Note**: The particle effects in this sample require a Mac that supports Tier 2 argument buffers. Particle effects aren’t available on iOS devices.

##### Respond to Landscape Alterations

The app determines the landscape’s initial topology from a static height map, `TerrainHeightMap.png`.

At runtime, as you alter the landscape with the provided controls, the sample evaluates the latest topology to determine whether it should apply a new habitat to the land based on its new elevation. If so, the sample updates the argument buffer corresponding to the land with the correct materials and vegetation geometry for the new habitat. The sample renders this new habitat by passing the land elevation value to the `EvaluateTerrainAtLocation` function.

##### Define an Argument Buffer for Terrain Habitats

The sample defines a custom argument buffer structure, `TerrainHabitat`, that defines the elements of a terrain habitat.

Among these elements, `elevationStrength` and `elevationThreshold` determine the elevation range in which the habitat is active. Additionally, `diffSpecTextureArray` and `normalTextureArray` determine the textures used to render the habitat.

The app nests `TerrainHabitat` within another argument buffer, `TerrainParams`, that provides many slight visual variations for added realism.

`TerrainHabitat` is the specific argument buffer definition for a terrain habitat. However, because the app nests its definition within `TerrainParams`, the app sends the `TerrainParams` objects to the GPU pipeline.

##### Render Terrain

The sample provides the GPU with the textures corresponding to various habitats. First, the sample calls the `useResource:usage:` method to indicate which textures the GPU uses.

Then, the sample calls the `setFragmentBuffer:offset:atIndex:` method to set the argument buffer, `terrainParamsBuffer`, that contains those textures.

The sample accesses the argument buffer in the fragment function, `terrain_fragment`, to output the correct material for the terrain. First, the sample passes the `mat` parameter into the fragment function.

Then, the sample passes the current land elevation into the `EvaluateTerrainAtLocation` function, where the fragment samples the texture corresponding to that elevation.

##### Render Vegetation

The sample passes the `terrainParamsBuffer` argument buffer to the vegetation render pass through an instance of `AAPLTerrainRenderer`. This data determines which type of vegetation to render at a given location. First, the sample calls the `setBuffer:offset:atIndex:` method to set the argument buffer for the vegetation render pass.

Then, the sample passes the argument buffer into the `EvaluateTerrainAtLocation` function, which produces a `habitatPercentages` value.

The habitat percentages are processed to select a specific index into the vegetation geometries, determined by the value of `pop_idx`.

Finally, the sample uses this population index to render an instance of a particular vegetation geometry onto the landscape.

##### Render Particles

The sample passes the `terrainParamsBuffer` argument buffer to the particle render pass through an instance of `AAPLTerrainRenderer`. This data determines which type of particles to render at a given location. First, the sample calls the `setBuffer:offset:atIndex:` method to set the argument buffer for the particle render pass.

Then, the sample checks the relative percentages of habitat coverage in the altered landscape with the `EvaluateTerrainAtLocation` function, where the sample passes the 3D position of the particle.

The sample chooses the appropriate habitat by selecting the terrain with the highest percentage of habitat coverage.

Finally, the app retrieves the particle’s corresponding habitat material from the argument buffer and sets it to the new particle.

## See Also

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
  Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)
  Optimize resource performance within an argument buffer.
- [Indexing argument buffers](indexing-argument-buffers.md)
  Assign resource indices within an argument buffer.
- [Encoding argument buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [class MTLArgumentDescriptor](mtlargumentdescriptor.md)
  A representation of an argument within an argument buffer.
- [protocol MTLArgumentEncoder](mtlargumentencoder.md)
  An interface you can use to encode argument data into an argument buffer.
- [var MTLAttributeStrideStatic: Int](mtlattributestridestatic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/rendering-terrain-dynamically-with-argument-buffers)*