# Blit passes

**Framework**: Metal

Encode a block information transfer pass to adjust and copy data to and from GPU resources, such as buffers and textures.

#### Overview

Your app can use a block information transfer (blit) pass to manage data within, and copy data between, buffers, textures, and other Metal resources. Start by creating a blit command encoder by calling an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance’s [`makeBlitCommandEncoder()`](mtlcommandbuffer/makeblitcommandencoder().md) method. Then use the [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) instance’s methods to encode individual commands of your blit pass.

You also have the option to customize a blit pass’s runtime behavior, such as sampling GPU hardware data. To enable these options, configure an [`MTLBlitPassDescriptor`](mtlblitpassdescriptor.md) instance and pass it to the command buffer’s [`makeBlitCommandEncoder(descriptor:)`](mtlcommandbuffer/makeblitcommandencoder(descriptor:).md) method. For more information about sampling GPU hardware data in a blit pass, see the articles in [`GPU counters and counter sample buffers`](gpu-counters-and-counter-sample-buffers.md), including:

- [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md)
- [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md)

## Topics

### Encoding a blit pass
- [protocol MTLBlitCommandEncoder](mtlblitcommandencoder.md)
  Encodes commands that copy and modify resources for a single blit pass.
- [struct MTLBlitOption](mtlblitoption.md)
  The options that enable behavior for some blit operations.
### Configuring a blit command encoder
- [class MTLBlitPassDescriptor](mtlblitpassdescriptor.md)
  A configuration you create to customize a blit command encoder, which affects the runtime behavior of the blit pass you encode with it.
- [class MTLBlitPassSampleBufferAttachmentDescriptor](mtlblitpasssamplebufferattachmentdescriptor.md)
  A configuration that instructs the GPU where to store counter data from the beginning and end of a blit pass.
- [class MTLBlitPassSampleBufferAttachmentDescriptorArray](mtlblitpasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a blit pass.

## See Also

- [Render passes](render-passes.md)
  Encode a render pass to draw graphics into an image.
- [Compute passes](compute-passes.md)
  Encode a compute pass that runs computations in parallel on a thread grid, processing and manipulating Metal resource data on multiple cores of a GPU.
- [Machine-learning passes](machine-learning-passes.md)
  Add machine-learning model inference to your Metal app’s GPU workflow.
- [Indirect command encoding](indirect-command-encoding.md)
  Store draw commands in Metal buffers and run them at a later time on the GPU, either once or repeatedly.
- [Ray tracing with acceleration structures](ray-tracing-with-acceleration-structures.md)
  Build a representation of your scene’s geometry using triangles and bounding volumes to quickly trace rays through the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/blit-passes)*