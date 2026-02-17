# Streaming large images with Metal sparse textures

**Framework**: Metal

Limit texture memory usage for large textures by loading or unloading image detail on the basis of MIP and tile region.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- Xcode 14.0+

#### Overview

This sample demonstrates sparse texture streaming by rendering a ground plane that samples from a 16K resolution texture. The renderer uses [`Managing sparse texture memory`](managing-sparse-texture-memory.md) to subdivide the image into regions, or , and chooses the tiles to keep in memory. The GPU updates an access counter buffer, and the app determines the tiles it needs to load or discard. The sample shows a heat map of the available MIP levels on the lower left of the screen, where  represents level 0,  represents levels 1 to 3,  represents levels 4 and 5, and  represents the remaining MIP levels. The app contains a checkbox that toggles the camera animation. When the animation runs, the app updates the sparse texture as the camera moves through the scene. Lastly, this sample demonstrates asynchronous updates using [`Dispatch`](https://developer.apple.com/documentation/Dispatch), or , to update the sparse texture.

![A screen capture of the sparse textures app showing the Apple Park texture and a heat map of the mapped sparse texture tiles.](https://docs-assets.developer.apple.com/published/492721f4ae4dbd9ca277e82d21e18460/sparse-textures-1-screen-capture.png)

Sparse textures are special textures that manage the residency of both tiles and MIP levels. For instance, a 16K resolution texture may use more than one gigabyte of memory, not including mipmaps that may increase levels memory requirements by 33%. To efficiently use space, the smallest MIP levels are often stored together, called a mipmap tail. For example, this may contain the 8 x 8, 4 x 4, 2 x 2, and 1 x 1 MIP levels. The following figure shows an example texture with its mipmaps and mipmap tail.

![An illustration showing a texture map and its eight levels of mipmaps. The last five levels of the mipmap tail are shown grouped together. An enlarged version of the mipmap tail is also included.](https://docs-assets.developer.apple.com/published/8818e36dca13e626b914eaa9bf93d1d4/sparse-textures-2-example-texture%402x.png)

The app follows a straightforward process to manage a sparse texture. First, it checks for sparse texture support. Next, it initializes the sparse texture by loading a texture of Apple Park, and loading and mapping the mipmap tails. Then, the app renders a scene that uses the sparse texture. After rendering, the app updates the texture in parallel with the main render pass. It retrieves the access counters, processes them, and discards tiles that aren’t needed anymore. It also maps and unmaps tiles, blits nonresident tiles, and updates the residency buffer when the blitting work finishes. To  means to copy a rectangle of pixels from a source image buffer to a destination memory buffer.

##### Configure the Sample Code Project

The Xcode project contains schemes for running the sample on macOS and iOS with a physical device that supports sparse textures. You can enable or disable camera movement by checking the switch button on the top-right of the app screen.

To run the app:

- Build the project with Xcode 12 and later.
- Target a macOS device with an M1 chip or later and macOS 12 or later.
- Target an iOS device with an A13 chip or later and iOS 14 or later.

##### Check for Sparse Texture Support

The sample checks if the [`MTLGPUFamily.apple6`](mtlgpufamily/apple6.md) feature set is available with the [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md) method. This feature set begins with the Apple A13 GPUs. Here’s the code from `AAPLViewController:viewDidLoad`:

##### Manage the Sparse Texture

A sparse texture divides large textures into tiles that the application treats as smaller textures with their own MIP levels. The sparse texture contains a residency buffer that tracks the MIP levels that are currently loaded. The following figure shows how the above texture would be subdivided into separate tile regions. The mipmap tail is considered its own tile, and the app ensures that all the tails are resident.

![An illustration of a large texture and its mipmaps, showing their division into tile regions. An enlarged version of the mipmap tail is also included.](https://docs-assets.developer.apple.com/published/38bd41fa07bb15ff077a3d68b7ea7cab/sparse-textures-3-texture-with-tiles%402x.png)

The residency buffer and access counter buffers use the same layout, but use different data types. The layout is an array of integer values representing each tile, starting with level 0. The tiles are laid out left to right and top to bottom. The app updates the residency buffer while the GPU updates the access counters. The residency buffer uses 8-bit integer values to represent Boolean residency or nonresidency, and the access counters are 64-bit integer values. The following figure shows the memory layout of the residency and access counter buffers.

![An illustration of the layout of the residency and access counter buffers. Resident tiles are colored in. Levels 0, 1, and 2 are shown, as well as the mipmap tail, with 0 being the largest.](https://docs-assets.developer.apple.com/published/9c70d68899aaa662ac4ad3cf2eb14d38/sparse-textures-4-memory-layout%402x.png)

The `AAPLSparseTexture` class manages the sparse texture in this sample and uses an [`MTLHeap`](mtlheap.md) to store the texture data for the tiles. A heap is a Metal object that allows an app to quickly allocate and free textures from a memory pool. Heaps allow quick allocation of tile memory and help limit the amount of memory used by the sparse texture. In addition to the heap, the class allocates two buffers. The first buffer is the residency buffer that tracks the highest MIP-level resident in the texture. When a shader fails to sample a sparse texture, it can use this buffer to fall back to a resident tile at a lower MIP level.

During rendering, the GPU uses the access counters buffer to store a counter per tile and increments it when a shader samples from the corresponding tile region. The app can query and analyze this buffer to find tiles to map or unmap. When the heap is low on available memory, the class can replace resident tiles that the shader hasn’t recently accessed. And this is how the app uses the residency and access counters buffers to dynamically adjust the residency of the sparse texture while staying within a memory budget.

##### Initialize the Sparse Texture

The app uses a 16K texture map of Apple Park stored in the Khronos Texture (KTX) file format. The `AAPLSparseTexture` and `AAPLStreamedTextureDataBacking` classes manage all aspects of using sparse textures. The app specifies a heap size of 16 MiB to quickly allocate memory to store tile data.

In the following code, the app starts loading the KTX file. The loader reads the file header and maps the file to memory using `mmap`. Memory mapping facilitates memory copies into staging buffers when the app needs to blit tiles to the sparse texture. The second step creates a heap for the mapped tiles and a second heap for the staging buffers. Allocating buffers from a heap is more efficient because Metal won’t perform expensive state tracking to avoid data hazards. The sparse texture manager performs its own heap management because only the sparse texture, in the grander scheme, needs to have data-hazard tracking. The third step maps the , the highest mipmap levels that fit inside one memory block. Then the texture manager blits the bottom mipmap tail into the sparse texture to ensure that all tiles contain a minimal amount of texture data. The final step creates the access counter buffer for all frames in flight. Lastly, the app updates the residency buffer to tell Metal which tiles are resident.

At this point, the app has initialized the sparse texture, copied the bottom mipmap tails to GPU memory, and mapped the mipmap tails resident. The app may now use the sparse texture for rendering objects.

##### Render the Scene

The app performs ordinary rendering tasks in `drawInMTKView,` like updating animation variables and uniform buffers, creating a command buffer, and rendering the scene. The end of the following block of code shows an optional rendering pass that renders a quad in the lower-left of the screen. This quad shows a color-coded version of the residency buffer. You may disable this visualization by setting the preprocessor variable `DEBUG_SPARSE_TEXTURE` to 0.

The app begins the update process after it commits the main command buffer. It asks the sparse texture class to update by querying the access counters and mapping and blitting tiles. The update can occur concurrently with the rendering thread using GCD. You may disable asynchronous processing by setting the preprocessor variable `ASYNCHRONOUS_TEXTURE_UPDATES` to 0.

##### Sample the Sparse Texture

The following code shows how the app draws the ground plane. It sets typical render states like pipeline state object, vertex and fragment buffers, and texture state. It also sets a fragment buffer, `_sparseTexture.residencyBuffer`, that the shader utilizes to sample the texture. And finally, it sets the sparse texture using `setFragmentTexture`.

The shader code uses the function `sampleSparseTexture` to handle sampling from the sparse texture. Metal provides a `sparse_sample` function that returns a `sparse_color<half4>` object. This object has a `resident` member function that returns `false` for an unmapped tile region. If the tile is resident, `sampleSparseTexture` returns the sampled color. Otherwise, it uses the residency buffer to determine the best MIP level for each mapped tile. Then it resamples the texture with the `min_lod_clamp` argument to ensure that unmapped tile regions aren’t accessed.

The residency buffer is a two-dimensional data structure that stores the best MIP level for each mapped tile. The function `getResidencyBufferMipmap` takes the input texture coordinates and converts them to tile coordinates `readX` and `readY`. The shader then indexes the residency buffer and returns the best MIP level.

While the fragment stage is running, the GPU records the number of texture memory operations by the shader. The app analyzes this buffer to stream and map new regions of texture data that aren’t resident.

The following figure shows an example of how the tiles sample resident parent tiles if a requested tile isn’t resident. The green tiles show a tile that the shader accessed and was resident. The red tiles show a tile that the shader accessed, but had to fall back to a lower MIP level. The app detects a tile it needs to map when the access counter is nonzero and the corresponding residency buffer is zero.

![An illustration showing how the shader samples resident parent tiles if a requested tile isn’t resident. Levels 0, 1, and 2 are shown, along with the mipmap tail, with level 0 being the largest. Tile colors denote whether a tile is accessed and resident, accessed but not resident, nonresident, or resident.](https://docs-assets.developer.apple.com/published/1cfaf424d0e334e6359c736605e936d4/sparse-textures-5-tiles-sample%402x.png)

##### Update the Sparse Texture

The following figure shows how the update process decides when to map or unmap tiles. For every resident tile that the shader accessed, the tile moves to the front of the least-recently used (LRU) cache, a data structure that combines a linked list and an unordered map. The `processAccessCounters` method creates map requests for the accessed nonresident tile and its nonresident parent tiles. The parent tiles need to form a chain from the bottom mipmap tail to the highest level tile. The update process checks for any dependencies and doesn’t create unmap requests for required parent tiles. And if the heap doesn’t have enough memory available, then `discardTilesFromLRU` unmaps unnecessary tiles to make room.

![An illustration showing how the shader decides to map or unmap tiles. Levels 0, 1, and 2 are shown, along with the mipmap tail, with level 0 being the largest. Different colors denote whether a tile is discarded LRU, required, required parent, nonresident, or resident.](https://docs-assets.developer.apple.com/published/186f598d40e05c0e52ee513f36c4be0e/sparse-textures-6-texture-update%402x.png)

To summarize, the `AAPLSparseTexture:update:` method calls four functions to update the texture:

- `updateAccessCountersBuffer` uses a blit encoder to get the access counters.
- `processAccessCounters` examines the access counter buffer to determine the tiles to map or unmap.
- `discardTilesFromLRU` uses an LRU cache to manage the sparse texture heap and determine the tiles to discard.
- `mapAndBlitTiles` maps tiles that need residency and blits them into the sparse texture.

The remaining sections cover these methods in more detail.

##### Update the Access Counter Buffers

The sparse texture class uses the [`getTextureAccessCounters(_:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:)`](mtlblitcommandencoder/gettextureaccesscounters(_:region:miplevel:slice:resetcounters:countersbuffer:countersbufferoffset:).md) API to copy and reset the counters for the sparse texture. It requests Metal to copy the data from each MIP level into the `_accessCountersBuffer`. The initialization step precalculated the offsets into this buffer, and the app can reference them from the `_accessCountersMipmapOffsets` array.

##### Process the Access Counter Buffers

When the sparse texture class examines the access counters buffer, each entry contains the number of times the shader accessed each MIP region. A value of zero means that the tile wasn’t referenced at all in the last frame. Since there can be several frames in flight, the app ensures that tiles aren’t unmapped prematurely. To manage this, the sparse texture class uses a simple data structure `TextureTile`:

The sparse texture class categorizes texture tiles in one of five states: unmapped, mapped, queue for mapping, queue for unmapping, or stored in the LRU cache. When examining each counter for all tiles, the sparse texture manager applies the following actions:

- Queue an accessed tile that’s unmapped for mapping.
- Store a mapped and unaccessed tile in the LRU cache.
- Queue an unaccessed tile in the LRU cache for unmapping.
- Change an accessed tile in the LRU cache back to a mapped state.
- Do nothing if the accessed tile is mapped.

The `SparseTexture:newMapTileRequest:` method adds the tile to a list of tiles to map. The helper function `setTextureTileRefCounterParent` ensures that parent tiles are properly reference counted. Resident parent tiles may depend on tiles in lower mipmap levels, so the sparse texture class doesn’t put them in the LRU cache. The following code shows the logic of putting tiles into the LRU cache.

##### Discard Tiles From the Lru Cache

The app uses a heap of textures to manage the mapped tiles in the sparse texture. If there’s no memory available to map nonresident tiles, then the sparse texture class discards older tiles. It uses an LRU cache to prioritize tiles to discard. The `AAPLPointerLRUCache` class manages a `std::list` and `std::unordered_map` to track mapped tile pointers. When the manager retrieves a pointer with `AAPLPointerLRUCache::get`, it moves the tile to the front of the cache. When the manager discards a tile and the cache is full, `discardLeastRecentlyUsed` removes the last entry in the cache. The app tracks the number of tiles that need discarding and creates unmap requests in the following code:

This completes the process to get the access counter buffers and create the map and unmap requests. The next step is to map and blit tiles.

##### Map and Blit Tiles

The app stores a list of mapping and unmapping requests that the `mapAndBlitTiles` method encodes using a . The `updateTileMappingMode` method converts the sparse pixel regions to tile regions and then updates the texture mapping to reflect the highest mapped MIP level.

While the resource state encoder is processing, the app starts streaming the tiles from the KTX file and blits them into the texture. The sparse texture manager iterates over new tile requests and calls `streamTileToStagingBuffer` to allocate staging buffers from the heap. The manager copies the texture from the file to the staging buffer and uses a blit encoder to write it to the sparse texture.

The last step is to wait until the blit command encoder is finished. During this time, the `mapAndBlitTiles` method updates the residency buffer and parent reference counts. This function waits to update the residency buffer until after the blits have finished, so the shader doesn’t access data that hasn’t finished mapping. The following code shows this process:

Once the resource state encoder maps the tiles, the blit encoder copies the texture data and the app updates the residency buffer, the process repeats for each frame. The app code renders a quad to the screen using the residency buffer to show the highest MIP levels available to visualize the sparse texture tile residency. You may set the `USE_SMALL_SPARSE_TEXTURE_HEAP` preprocessor variable to 1 to see how mapping and unmapping occurs more frequently when the heap size is smaller.

## See Also

- [Combining blit and compute operations in a single pass](combining-blit-and-compute-operations-in-a-single-pass.md)
  Run concurrent blit commands and then a compute dispatch in a single pass with a unified compute encoder.
- [Reading pixel data from a drawable texture](reading-pixel-data-from-a-drawable-texture.md)
  Access texture data from the CPU by copying it to a buffer.
- [Creating and sampling textures](creating-and-sampling-textures.md)
  Load image data into a texture and apply it to a quadrangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/streaming-large-images-with-metal-sparse-textures)*