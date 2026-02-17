# Combining blit and compute operations in a single pass

**Framework**: Metal

Run concurrent blit commands and then a compute dispatch in a single pass with a unified compute encoder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- Xcode 26.2+

#### Overview

This sample demonstrates how to use Metal 4’s unified compute encoder to combine texture data and create a grayscale version of it at the same time. The app runs blit and dispatch operations in a single compute pass, then renders the results with a render pass.

This sample builds on Metal 4 fundamentals in [`Drawing a triangle with Metal 4`](drawing-a-triangle-with-metal-4.md), including command buffers, allocators, residency sets, and submitting work to the GPU.

Each time the system requests a frame, the app:

1. Creates a composite color texture by copying two color textures with concurrent blit commands.
2. Creates a grayscale texture by converting the composite color texture with a compute kernel.
3. Draws two adjacent rectangles, one for each composite texture.

An [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) instance combines blit, dispatch, and acceleration structure commands into a single pass, which reduces your app’s overhead from creating multiple encoders and encoding separate passes. The app increases its GPU utilization by running independent blit commands that concurrently write to memory regions that don’t overlap. However, it prevents the blit and dispatch stage memory operations from running at the same time, by synchronizing them with an intrapass barrier.

![A timeline diagram along a GPU runtime axis that shows a compute pass followed by a render pass. The compute pass contains two blit stages that run in parallel, followed by an intrapass barrier, and then a dispatch stage. A consumer barrier separates the compute pass from the render pass, which contains render stages.](https://docs-assets.developer.apple.com/published/96b6bb182776b7b6d12ff9f7caf8fed8/combining-blit-and-compute-operations-in-a-single-pass%402x.png)

The app also reuses its one argument table by modifying the arguments in the table as necessary. For example, each blit command copies from a different source texture, and the dispatch command needs access to both composite textures. Metal processes bindings at draw and dispatch time, allowing the renderer to reconfigure bindings so that you don’t have to create new argument tables.

##### Create Long Term Resources

The renderer’s initializer creates the fundamental Metal instances it needs: a command queue, a reusable command buffer, and the default library. For more information on how these work, see [`Drawing a triangle with Metal 4`](drawing-a-triangle-with-metal-4.md).

The initializer also creates buffers, textures, an argument table, a shared event, and residency sets by calling helper methods:

The renderer stores and reuses them for every frame.

##### Load Textures From Image Files

The `createTextures` helper method starts by loading the contents from the app’s two TGA files into textures:

The `loadImageToTexture:` method creates an instance of [`MTLTexture`](mtltexture.md) with a pixel format that stores four color channels: blue, green, red, and alpha. Each channel uses an 8-bit unnormalized value, where `0` maps to `0.0` and `255` maps to `1.0`:

After creating the texture, the method copies the image data into it with its [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md) method:

##### Create Textures for the Composite Images

The app creates two additional textures to store the composite images, by configuring an instance of [`MTLTextureDescriptor`](mtltexturedescriptor.md) with dimensions that fit both source images. The first texture stores the composite color texture that the compute pass creates from the background and chyron textures. The second texture stores the grayscale equivalent of the composite color texture.

The descriptor configures the composite texture’s height to fit both the background image and the chyron.

The `createTextures` method creates the composite color texture with read-only access, because the `convertToGrayscale` kernel only reads from it:

The composite grayscale texture needs both read and write access, because the fragment shader reads from it and the compute kernel writes to it:

##### Create an Argument Table

The renderer binds resources to shader parameters by creating an argument table that stores buffer and texture bindings:

The `createArgumentTable` method configures an instance of [`MTL4ArgumentTableDescriptor`](mtl4argumenttabledescriptor.md) with the largest number of buffer and texture bindings the app ever needs at one time:

The compute pass binds two textures for the color input and grayscale output. The render pass binds two buffers for vertex data and viewport size, plus one texture that changes between draw calls.

> 💡 **Tip**: Minimize an app’s memory footprint by setting the binding counts to only what the renderer needs.

##### Compile a Render Pipeline

The renderer compiles a render pipeline at launch time by creating an instance of [`MTL4Compiler`](mtl4compiler.md) with a default configuration:

The `createRenderPipelineFor:` method compiles a render pipeline with vertex and fragment shaders:

##### Compile a Compute Pipeline with a Grayscale Kernel

The renderer compiles a compute pipeline with the `convertToGrayscale` kernel function.

The `createComputePipeline` method creates an [`MTL4LibraryFunctionDescriptor`](mtl4libraryfunctiondescriptor.md) that refers to the `convertToGrayscale` kernel in the default library:

The `convertToGrayscale` kernel converts each pixel from color to grayscale. The kernel’s signature declares two texture parameters and a grid position parameter:

The kernel uses the `read` access qualifier for `inTexture` because it only reads from it, and the `write` access qualifier for `outTexture` because it only writes to it.

The `gridId` parameter provides each thread’s position in the 2D grid. The `[[thread_position_in_grid]]` attribute qualifier tells Metal to generate and pass these coordinates to each thread.

The kernel calculates the grayscale value by applying the Rec. 709 luma coefficients to the color pixel’s RGB components:

The kernel first checks whether the thread’s grid coordinates are within the texture’s bounds, then returns early if they aren’t. This check handles the case where the grid size exceeds the texture’s size.

##### Calculate the Threadgroup Count

The renderer calculates how many threadgroups to dispatch based on the composite texture’s dimensions.

The `configureThreadgroupForComputePasses` method sets a 16 × 16 threadgroup size, which runs on any Apple silicon GPU:

The method calculates the number of threadgroups in each dimension by dividing the texture’s dimensions by the threadgroup size and rounding up:

This calculation ensures the grid covers an area that’s at least as large as the texture, which is why the kernel checks whether each thread’s coordinates are within bounds.

##### Combine Textures with Concurrent Blit Commands

The renderer encodes a compute pass that combines two operations with a compute encoder:

- Copying texture data with blit commands
- Converting the result to grayscale with a dispatch command

The renderer encodes two copy commands that write to different regions of the composite color texture:

The `encodeChyronTextureCopy:` method copies the chyron texture to the top of the composite texture:

The `encodeBackgroundTextureCopy:` method copies the background texture below the chyron:

The unified compute encoder automatically improves the app’s runtime performance when commands write to different destination textures or non-overlapping regions, because it runs those operations concurrently.

> **Note**: Metal runs copy commands sequentially when they write to overlapping regions of a destination texture.

##### Synchronize the Blit and Dispatch Stages with a Barrier

The renderer resolves an access conflict between the blit and dispatch stages by encoding an intrapass barrier:

An access conflict happens when multiple commands access the same resource at the same time, and at least one of those commands modifies the resource. The copy commands store data to `compositeColorTexture` during the blit stage, and the dispatch command loads from the same texture during the dispatch stage. Without a barrier, the GPU can run these stages concurrently, creating a race condition where the dispatch might read incomplete data.

The barrier forces the GPU to wait until the blit stage completes before starting the dispatch stage, ensuring the dispatch loads the final data values from the composite texture.

For more information about access conflicts and synchronization, see [`Resource synchronization`](resource-synchronization.md) and [`Synchronizing stages within a pass`](synchronizing-stages-within-a-pass.md).

##### Convert the Composite Texture to Grayscale

The renderer converts the composite color texture to grayscale by dispatching the `convertToGrayscale` kernel:

After encoding the dispatch command, the renderer ends the compute pass:

##### Render the Composite Textures

The renderer creates a render encoder to draw a rectangle for both the color and grayscale composite textures:

The renderer resolves an access conflict between the compute and render passes by encoding a consumer barrier:

The dispatch command in the compute pass stores data to `compositeGrayscaleTexture`, and the fragment shader in the render pass loads from the same texture. The consumer barrier forces the GPU to wait until the dispatch stage from the earlier compute pass completes before starting the vertex stage of the render pass. This ensures the fragment shader loads the correct and final data from the grayscale texture.

The `afterQueueStages` parameter refers to stages in earlier passes, whereas the `beforeStages` parameter refers to stages in the current and later passes.

The renderer prepares the render pass for drawing by configuring the viewport, setting the render pipeline state, and binding the argument table to both vertex and fragment stages:

The renderer provides input data to the vertex shader by binding the vertex and viewport buffers to the argument table:

The renderer draws the first rectangle by binding the composite color texture and calling the encoder’s draw method:

The renderer draws the second rectangle with the grayscale texture by changing the texture binding in the argument table and issuing another draw command:

The app changes the binding entries in the argument table between draw calls because each call needs different arguments.

> **Note**:  You can modify the entries in an [`MTL4ArgumentTable`](mtl4argumenttable.md) instance after passing it to an encoder’s [`setArgumentTable(_:)`](mtl4computecommandencoder/setargumenttable(_:).md) method because Metal evaluates the argument table each time you call a command-encoding method.

After encoding both draw commands, the renderer ends the render pass.

##### Submit the Command Buffer to the Gpu

After encoding the compute and render passes, the renderer finalizes and submits the command buffer to the Metal device by committing the command buffer to the device’s command queue:

## See Also

- [Performing calculations on a GPU](performing-calculations-on-a-gpu.md)
  Use Metal to find GPUs and perform calculations on them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/combining-blit-and-compute-operations-in-a-single-pass)*