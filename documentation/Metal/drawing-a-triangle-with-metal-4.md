# Drawing a triangle with Metal 4

**Framework**: Metal

Render a colorful, rotating 2D triangle by running draw commands with a render pipeline on a GPU.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 12.0+
- tvOS 12.0+
- Xcode 26.2+

#### Overview

This sample demonstrates how to render imagery by sending commands to the GPU with the Metal 4 API, and relates to WWDC25 session 205: [`Discover Metal 4`](https://developer.apple.comhttps://developer.apple.com/wwdc25/205).

Multiple times a second, the sample’s app displays a colorful triangle by:

1. Updating the vertex data for the triangle
2. Encoding draw commands as a  of visual content
3. Running the draw commands on a Metal device that represents an Apple silicon GPU
4. Updating the display after the GPU finishes rendering that frame

Apps can give a person the impression of motion by rendering and displaying frames at a sufficient frequency, typically at 60 frames or more per second.

The renderer encodes one frame at a time, and has three frames of content in flight at the same time. Starting when the first frame is visible on the display, the renderer is continually managing three frames at once:

- The first frame is in its final lifetime phase as the frame that’s visible to a person on the device’s display.
- The second frame is in its second lifetime phase where the GPU renders it in a , which is the collection of render commands that draw the triangle.
- The third frame is in its first lifetime phase where the renderer encodes the draw commands for the next render pass by using the Metal API on the CPU.

The renderer manages the frames as each progresses through its three lifetime phases. The diagram below illustrates how the first frames move through time, where each column represents a snapshot of the app’s current frames and their states:

![A timeline diagram that shows how frames progress through their lifetime phases by dividing time into vertical columns, each of which represents a snapshot in time as they flow from left to right. The first column has one box with the label “encode frame 1”. The second column has two boxes with the labels “encode frame 2” and “execute frame 1”. The third column has three boxes with the labels “encode frame 3”, “execute frame 2” and “display frame 1”. The next two columns continue the pattern with three boxes each, where column five has the labels “encode frame 5”, “execute frame 4”, and “display frame 3”. The final, right-most column has three boxes, each with an ellipsis that indicates the pattern continues indefinitely.](https://docs-assets.developer.apple.com/published/7d4026996b180f5d08fabfd934f6c536/drawing-a-triangle-with-metal-4-1%402x.png)

##### Create a Renderer

The sample implements two separate renderer classes and the app creates a new instance of the one that’s appropriate for the system it’s running on. The two classes are:

- `Metal4Renderer`, a renderer class that works with the Metal 4 API
- `MetalRenderer`, a renderer class that works with previous Metal API versions

The app checks whether the system supports Metal 4 by calling [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md) in the `MetalKitViewDelegate` class.

The app creates a Metal 4 renderer if the operating system supports [`MTLGPUFamily.metal4`](mtlgpufamily/metal4.md); otherwise it creates an instance of the other renderer, which supports previous versions of Metal.

The two renderers are identical in their behavior, but they use different Metal API generations to submit the same render commands to the GPU.

> **Note**: You may only need to implement a renderer that supports one Metal API depending on the platforms and devices you want your app to support.

##### Create Long Term Resources

The Metal 4 renderer’s initializer starts by creating an instance of [`MTL4CommandQueue`](mtl4commandqueue.md), [`MTL4CommandBuffer`](mtl4commandbuffer.md), and [`MTLLibrary`](mtllibrary.md) with the view’s [`MTLDevice`](mtldevice.md).

Generally, you send work to the GPU by encoding commands into a command buffer, and then submitting one or more command buffers to a queue. Your app can have multiple command buffers and queues, but the sample’s `Metal4Renderer` class needs only one of each.

The initializer creates other resources the renderer needs by calling helper methods.

The renderer defines `kMaxFramesInFlight` near the top of its primary source file.

The sample applies this constant when it creates separate instances of the resources the renderer needs for each in-flight frame, which includes the buffers that store a triangle’s geometry and color information.

Most of the helper methods that create the renderer’s long-term resources at launch are relatively short. For example, the `makeTriangleDataBuffers:` method creates `kMaxFramesInFlight` instances of [`MTLBuffer`](mtlbuffer.md) because each in-flight frame needs a separate buffer to store its triangle vertex data.

Creating a separate buffer instance for each in-flight frame eliminates the possibility of modifying a buffer for a later frame before or as the GPU reads from the same buffer to render an earlier frame.

The `makeArgumentTable` method creates just a single argument table that the renderer can reuse each time it encodes render commands into a render pass the GPU eventually runs. You set the resource bindings for any pass you encode with an [`MTL4CommandBuffer`](mtl4commandbuffer.md), including compute and render passes, by configuring an [`MTL4ArgumentTable`](mtl4argumenttable.md) instance.

Each argument table can store bindings to instances of various resource types, including:

- [`MTLBuffer`](mtlbuffer.md)
- [`MTLTexture`](mtltexture.md)
- [`MTLTensor`](mtltensor.md)
- [`MTLSamplerState`](mtlsamplerstate.md)
- [`MTLAccelerationStructure`](mtlaccelerationstructure.md)

For this sample, the argument table only needs to store two buffer bindings, one for the buffer that stores vertex triangle data, and another buffer that stores the viewport’s width and height.

> 💡 **Tip**: You can help minimize an app’s memory footprint by reducing the number of binding entries in an argument table to what your renderer needs.

The `makeResidencySet` and `makeCommandAllocators:` methods create a single [`MTLResidencySet`](mtlresidencyset.md) instance, and an [`MTL4CommandAllocator`](mtl4commandallocator.md) instance for each in-flight frame, respectively.

The end of the initializer configures the renderer’s initial state so that it’s ready to render the first frame when the system requests it.

The initializer adds two residency sets to the renderer’s command queue:

- The long-term residency set, which the renderer configures to track all of its [`MTLBuffer`](mtlbuffer.md) instances
- The view’s residency set, which MetalKit configures

See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) for more information about working with residency sets.

##### Create a Render Pipeline

The renderer’s `compileRenderPipeline:` method creates a render pipeline by configuring an [`MTL4RenderPipelineDescriptor`](mtl4renderpipelinedescriptor.md) instance and passing it to an [`MTL4Compiler`](mtl4compiler.md) instance’s [`newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:`](mtl4compiler/newrenderpipelinestatewithdescriptor:compilertaskoptions:error:.md) method.

The renderer’s `configureRenderPipeline:` method sets the various properties the compiler needs to create a render pipeline state.

The `makeVertexShaderConfiguration` helper method creates an [`MTL4LibraryFunctionDescriptor`](mtl4libraryfunctiondescriptor.md) instance that refers to the renderer’s vertex shader.

Similarly, the `makeFragmentShaderConfiguration` helper method creates another function descriptor instance that refers to the renderer’s fragment shader.

##### Draw a Frame By Encoding a Render Pass

The app is ready to render frames after its renderer creates and sets up all its resources at launch, including data buffers and a render pipeline state. Each time the system calls the app’s [`draw(in:)`](https://developer.apple.com/documentation/MetalKit/MTKViewDelegate/draw(in:)) method, its [`MTKViewDelegate`](https://developer.apple.com/documentation/MetalKit/MTKViewDelegate) implementation calls the renderer’s `renderFrameToView:` method, which encodes and runs the commands that render the frame with the following steps:

1. Check that the [`MTKView`](https://developer.apple.com/documentation/MetalKit/MTKView) parameter has valid [`currentDrawable`](https://developer.apple.com/documentation/MetalKit/MTKView/currentDrawable) and [`currentMTL4RenderPassDescriptor`](https://developer.apple.com/documentation/MetalKit/MTKView/currentMTL4RenderPassDescriptor) properties.
2. Increment the frame number, which tracks the resources it can reuse from previous frames that don’t need them any longer.
3. Prepare a command buffer.
4. Create and configure a render pass encoder.
5. Set the viewport to the size of the app’s view.
6. Configure the arguments for the render pass, which in this case are two data buffers.
7. Encode a draw command for the triangle.
8. Mark the end of the render pass and the command buffer that contains it.
9. Run the render pass by submitting the command buffer to the Metal device’s command queue, and display the result when it finishes.
10. Notify the renderer when it’s safe to reuse this frame’s resources for a new frame by signaling its shared event.

The remaining sections explain the important details of these steps.

##### Prepare a Command Buffer

The renderer uses the same [`MTL4CommandBuffer`](mtl4commandbuffer.md) instance to render every frame. You can reuse a Metal 4 command buffer instance immediately after submitting it to an [`MTL4CommandQueue`](mtl4commandqueue.md). This is because a command allocator stores a record of the command buffer’s contents when you submit it to a queue.

The renderer prepares the command buffer for a new set of commands by calling its [`beginCommandBuffer(allocator:)`](mtl4commandbuffer/begincommandbuffer(allocator:).md) method.

The renderer reuses an [`MTL4CommandAllocator`](mtl4commandallocator.md) instance the GPU no longer needs by rotating through the `kMaxFramesInFlight` allocators it creates at launch.

> ❗ **Important**: Unlike a command buffer, you can’t immediately reuse an allocator after submitting a command buffer to a queue, but you can after the device finishes running the passes in the command buffer you associate with the allocator.

The renderer ensures the next allocator in the rotation is available by calling the `waitOnSharedEvent:forEarlierFrame:` method. That method calls the [`wait(untilSignaledValue:timeoutMS:)`](mtlsharedevent/wait(untilsignaledvalue:timeoutms:).md) method of the renderer’s [`MTLSharedEvent`](mtlsharedevent.md) instance, which can potentially block the caller for 10 milliseconds before it returns.

The command queue updates the shared event after the Metal device finishes rendering the previous frame that uses the same allocator, which indicates to this method that it’s now available to reuse. Ideally, the shared event’s method returns immediately because the earlier frame using the allocator is done rendering and no longer needs it.

##### Create an Encoder for a Render Pass

The `renderFrameToView:` method creates a render command encoder by retrieving an [`MTL4RenderPassDescriptor`](mtl4renderpassdescriptor.md) instance from the view’s [`currentMTL4RenderPassDescriptor`](https://developer.apple.com/documentation/MetalKit/MTKView/currentMTL4RenderPassDescriptor) property and passing it to the command buffer’s [`makeRenderCommandEncoder(descriptor:options:)`](mtl4commandbuffer/makerendercommandencoder(descriptor:options:).md) method. The view’s property represents a valid configuration for a render pass to render a frame in a format that’s compatible with that view.

The command buffer’s factory method returns an [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md) instance, which provides methods that configure a render pass and encode the commands for that pass.

The method also gives the render encoder a unique name that can help you identify its render pass from other passes in Metal debugger. For more information about Metal debugger and inspecting passes, see:

- [`Metal debugger`](https://developer.apple.com/documentation/Xcode/Metal-debugger)
- [`Analyzing your Metal workload`](https://developer.apple.com/documentation/Xcode/Analyzing-your-Metal-workload)

##### Configure the Viewport for the Render Pass

The renderer’s `setViewport` method configures an [`MTLViewport`](mtlviewport.md) and passes it to the encoder’s [`setViewport(_:)`](mtl4rendercommandencoder/setviewport(_:).md)method.

The method configures the viewport’s 2D size by setting the `x` and `y` members to the dimensions of the app’s view, in pixels.

##### Configure Any Arguments for the Render Pass

The renderer’s `setRenderPassArguments:` method configures two arguments for the render pass, both of which are [`MTLBuffer`](mtlbuffer.md) instances.

The method retrieves the next triangle vertex buffer in the rotation. Each render pass needs its own copy of triangle vertex data because the data for each frame is unique, and the GPU needs access to each frame’s input data until it finishes rendering that frame. The renderer tracks and rotates through `kMaxFramesInFlight` buffers of triangle vertex data in an array, similar to the command allocators because each frame has slightly different coordinates for the triangle as it rotates.

The method calls the renderer’s `configureVertexDataForBuffer:` method, which calculates the positions of the triangle’s vertices by applying a rotation angle and then copies the vertex data into the [`MTLBuffer`](mtlbuffer.md).

##### Encode Draw Commands

The renderer draws exactly one triangle with a single call to [`drawPrimitives(primitiveType:vertexStart:vertexCount:)`](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:).md):

This renderer only needs one draw command, but yours can encode multiple drawing commands in a single render pass.

##### End the Render Pass

The `renderFrameToView:` method marks the conclusion of the render pass by calling the encoder’s [`endEncoding()`](mtl4commandencoder/endencoding().md) method.

It then marks the end of the command buffer by calling its [`endCommandBuffer()`](mtl4commandbuffer/endcommandbuffer().md) method because it only needs to encode a single render pass. However, your app can encode multiple passes of different types in a single command buffer with a series of encoder types, including the following:

- [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md)
- [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md)
- [`MTL4MachineLearningCommandEncoder`](mtl4machinelearningcommandencoder.md)

##### Run the Render Pass By Submitting the Command Buffer

The renderer sends the command buffer to run on the GPU in its `submitCommandBufferForView:` method. The method starts by retrieving the [`CAMetalDrawable`](https://developer.apple.com/documentation/QuartzCore/CAMetalDrawable) instance the view stores in its [`currentDrawable`](https://developer.apple.com/documentation/MetalKit/MTKView/currentDrawable) property.

> **Note**: The view’s current drawable is the same instance as the one in the view’s [`currentMTL4RenderPassDescriptor`](https://developer.apple.com/documentation/MetalKit/MTKView/currentMTL4RenderPassDescriptor) convenience property, specifically the first entry in the descriptor’s [`colorAttachments`](mtl4renderpassdescriptor/colorattachments.md) property, which the renderer uses to create each render pass encoder.

The method adds the following actions to the renderer’s [`MTL4CommandQueue`](mtl4commandqueue.md) instance, which run on the GPU timeline:

1. Wait for the view’s drawable with the [`waitForDrawable(_:)`](mtl4commandqueue/waitfordrawable(_:).md) method.
2. Submit the command buffer to run on the GPU with the [`commit:count:`](mtl4commandqueue/commit:count:.md) method.
3. Notify the drawable that the GPU is finished running the render pass with the [`signalDrawable(_:)`](mtl4commandqueue/signaldrawable(_:).md) method.

The Metal device needs to wait until the view’s drawable is available because it stores the output from the render pass and provides the mechanism that updates the content on the display. When the drawable is ready, the GPU runs the single render pass in the command buffer, which saves the results to the drawable’s texture.

> **Note**: Your app can submit one or more Metal 4 command buffers to any command queue, if and only if the command buffers and command queues come from the same Metal device.

The method concludes by calling the drawable’s [`present()`](mtldrawable/present().md) method, which instructs the drawable to show its content on the device’s display shortly after it gets the notification from the command queue. The [`MTLDrawable`](mtldrawable.md) protocol defines this method, which the [`CAMetalDrawable`](https://developer.apple.com/documentation/QuartzCore/CAMetalDrawable) protocol inherits.

##### Notify the Renderer When a Frames Resources Are Ready for Reuse

The last command the `renderFrameToView:` method adds to the command queue notifies the renderer when it can reuse this frame’s triangle vertex buffer and command allocator, by signaling its [`MTLSharedEvent`](mtlsharedevent.md) instance with the current frame number.

For example, if the `frameNumber` equals `4` and `kMaxFramesInFlight` equals `3`, this signal informs the renderer when its okay to reuse the fourth frame’s resources and apply them for frame seven.

## See Also

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)
  Discover the features and functionality in the Metal 4 foundational APIs.
- [Performing calculations on a GPU](performing-calculations-on-a-gpu.md)
  Use Metal to find GPUs and perform calculations on them.
- [Using Metal to draw a view’s contents](using-metal-to-draw-a-view's-contents.md)
  Create a MetalKit view and a render pass to draw the view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/drawing-a-triangle-with-metal-4)*