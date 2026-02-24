# Synchronizing a managed resource in macOS

**Framework**: Metal

Manually synchronize memory for a Metal resource in apps.

#### Overview

For Mac computers with Intel or external GPUs, Metal offers *managed resources.* Managed resources are [`MTLResource`](mtlresource.md) instances, such as an [`MTLTexture`](mtltexture.md) or [`MTLBuffer`](mtlbuffer.md), which use memory that your app can copy between the CPU and GPU. Managed resources use a [`storageMode`](mtlresource/storagemode.md) of [`MTLStorageMode.managed`](mtlstoragemode/managed.md).

You need to manually synchronize managed resources, copying changed memory between the CPU and GPU. This is different from Apple family GPUs, which use [`MTLStorageMode.shared`](mtlstoragemode/shared.md) for resources that the CPU and GPU can both access. Synchronize after your code finishes memory writes. After data synchronizes, you can safely read it in both your app and GPU functions.

As a best practice, try to keep your data synchronization points to a minimum. Even synchronization calls which don’t copy data can result in a small performance hit.

> **Note**:  Managed resources are the default memory storage type for Intel and external GPU devices in Metal. For more information about macOS resource storage modes and how to select them, see [`Choosing a resource storage mode for Intel and AMD GPUs`](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md).

##### Synchronize a Managed Buffer

First, create an [`MTLBuffer`](mtlbuffer.md) with the option [`MTLStorageMode.managed`](mtlstoragemode/managed.md), which tells Metal to reserve managed memory space for the resource:

**Swift**:

```swift
// Create a matrix data structure.
struct MatrixData {
    var modelMatrix = matrix_float4x4()
    var viewMatrix = matrix_float4x4()
    var projectionMatrix = matrix_float4x4()
}

// Create a managed buffer.
guard let matrixBuffer = device.makeBuffer(length: MemoryLayout<MatrixData>.size, options: .storageModeManaged) else { return }
```

**Objective-C**:

```objective-c
// Create a matrix data structure.
id <MTLBuffer> _matrixBuffer;
typedef struct
{
    matrix_float4x4 modelMatrix;
    matrix_float4x4 viewMatrix;
    matrix_float4x4 projectionMatrix;
} MatrixData;

// Create a managed buffer.
_matrixBuffer = [_device newBufferWithLength:sizeof(MatrixData)
                                     options:MTLResourceStorageModeManaged];
```

Next, modify the buffer’s data on the CPU:

**Swift**:

```swift
// Modify the managed buffer's data with the CPU.
var matrixData = MatrixData()
matrixData.modelMatrix = updatedModelMatrix
matrixBuffer.contents().storeBytes(of: matrixData, as: MatrixData.self)
```

**Objective-C**:

```objective-c
// Modify the managed buffer's data with the CPU.
MatrixData *matrixData = (MatrixData*)_matrixBuffer.contents;
matrixData->modelMatrix = updatedModelMatrix;
```

After completing a CPU modification, call the [`didModifyRange:`](mtlbuffer/didmodifyrange:.md) method. This method updates a specific range of data and keeps the buffer synchronized. Before calling this method, the modified buffer’s data on the GPU is in an undefined state.

**Swift**:

```swift
// Synchronize the managed buffer.
matrixBuffer.didModifyRange(0..<MemoryLayout<matrix_float4x4>.size)
```

**Objective-C**:

```objective-c
// Synchronize the managed buffer.
[_matrixBuffer didModifyRange:NSMakeRange(0, sizeof(matrixData->modelMatrix))];
```

After encoding a GPU modification, encode a [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) command. This command updates the entire buffer and keeps it synchronized. Before executing this command, the modified buffer’s data on the CPU is in an undefined state.

**Swift**:

```swift
// Create a command buffer for GPU work.
if let commandBuffer = commandQueue.makeCommandBuffer() {
    // Create a compute command encoder.
    guard let computeCommandEncoder =
            commandBuffer.makeComputeCommandEncoder(dispatchType: MTLDispatchType.serial)
    else { return }
    
    // Encode a compute pass to modify the managed buffer's data with the GPU.
    computeCommandEncoder.setComputePipelineState(computePipelineStateObject)
    computeCommandEncoder.setBuffer(matrixBuffer, offset: 0, index: 0)
    computeCommandEncoder.dispatchThreads(gridSize, threadsPerThreadgroup: threadgroupSize)
    computeCommandEncoder.endEncoding()
    
    // Add a completion handler and commit the command buffer.
    let commandBufferHandler: MTLCommandBufferHandler
    commandBuffer.addCompletedHandler(commandBufferHandler)
    commandBuffer.commit()
}
```

**Objective-C**:

```objective-c
// Create a command buffer for GPU work.
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// Encode a compute pass to modify the managed buffer's data with the GPU.
id <MTLComputeCommandEncoder> computeCommandEncoder = [commandBuffer computeCommandEncoderWithDispatchType:MTLDispatchTypeSerial];
[computeCommandEncoder setComputePipelineState:computePipelineStateObject];
[computeCommandEncoder setBuffer:_matrixBuffer
                          offset:0
                         atIndex:0];
[computeCommandEncoder dispatchThreads:gridSize
                 threadsPerThreadgroup:threadgroupSize];
[computeCommandEncoder endEncoding];

// Synchronize the managed buffer.
id <MTLBlitCommandEncoder> blitCommandEncoder = [commandBuffer blitCommandEncoder];
[blitCommandEncoder synchronizeResource:_matrixBuffer];
[blitCommandEncoder endEncoding];

// Add a completion handler and commit the command buffer.
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> cb) {
    // In this code block, the command buffer `cb` is updated and synchronized, and can be safely read or written to.
}];
[commandBuffer commit];
```

##### Synchronize a Managed Texture

First, create an [`MTLTexture`](mtltexture.md) in managed memory from an [`MTLTextureDescriptor`](mtltexturedescriptor.md) with its storage mode set to [`MTLStorageMode.managed`](mtlstoragemode/managed.md):

**Swift**:

```swift
// Create a texture descriptor.
let textureDescriptor = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: .rgba8Unorm,
                                                                 width: textureSize.width,
                                                                 height: textureSize.height,
                                                                 mipmapped: false)

// Set the descriptor's storage mode and usage.
textureDescriptor.storageMode = MTLStorageMode.managed
textureDescriptor.usage = [.shaderRead, .shaderWrite]

// Create a managed texture.
let imageTexture = device.makeTexture(descriptor: textureDescriptor)
```

**Objective-C**:

```objective-c
id <MTLTexture> _imageTexture;
// Create a texture descriptor.
MTLTextureDescriptor *textureDescriptor = [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm
                                                                                             width:textureSize.width
                                                                                            height:textureSize.height
                                                                                         mipmapped:NO];

// Set the descriptor's storage mode and usage.
textureDescriptor.storageMode = MTLStorageModeManaged;
textureDescriptor.usage = MTLTextureUsageShaderRead | MTLTextureUsageShaderWrite;

// Create a managed texture.
_imageTexture = [_device newTextureWithDescriptor:textureDescriptor];
```

To perform a CPU modification and simultaneously notify Metal about the change, call the [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md) method. This method updates a specific region of data and keeps the texture synchronized. To update a specific texture slice, call the [`replace(region:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:)`](mtltexture/replace(region:mipmaplevel:slice:withbytes:bytesperrow:bytesperimage:).md) method instead. Before calling one of these methods, the modified texture’s data on the GPU is in an undefined state.

**Swift**:

```swift
// Simultaneously modify and synchronize the managed texture's data with the CPU.
let region = MTLRegionMake2D(textureOrigin.x, textureOrigin.y, textureSize.width, textureSize.height)
let bytesPerRow = pixelSize * textureSize.width
imageTexture.replace(region: region, mipmapLevel: 0, withBytes: textureData, bytesPerRow: bytesPerRow)
```

**Objective-C**:

```objective-c
// Simultaneously modify and synchronize the managed texture's data with the CPU.
[_imageTexture replaceRegion:MTLRegionMake2D(textureOrigin.x, textureOrigin.y, textureSize.width, textureSize.height)
                 mipmapLevel:0
                   withBytes:textureData
                 bytesPerRow:pixelSize*textureSize.width];
```

After encoding a GPU modification, encode a [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) command. This command updates the entire texture and keeps it synchronized. To update a specific texture slice or mipmap level, encode the [`synchronize(texture:slice:level:)`](mtlblitcommandencoder/synchronize(texture:slice:level:).md) command instead. Before executing this command, the modified texture’s data on the CPU is in an undefined state.

**Swift**:

```swift
// Create a command buffer for GPU work.
if let commandBuffer = commandQueue.makeCommandBuffer() {
    // Create a compute command encoder.
    guard let computeCommandEncoder =
            commandBuffer.makeComputeCommandEncoder(dispatchType: MTLDispatchType.serial)
    else { return }
    
    // Encode a compute pass to modify the managed texture's data with the GPU.
    computeCommandEncoder.setComputePipelineState(computePipelineStateObject)
    computeCommandEncoder.setTexture(imageTexture, index: 0)
    computeCommandEncoder.dispatchThreads(gridSize, threadsPerThreadgroup: threadgroupSize)
    computeCommandEncoder.endEncoding()
    
    // Synchronize the managed texture.
    guard let blitCommandEncoder = commandBuffer.makeBlitCommandEncoder() else { return }
    blitCommandEncoder.synchronize(resource: imageTexture)
    blitCommandEncoder.endEncoding()
    
    // Add a completion handler.
    commandBuffer.addCompletedHandler { commandBuffer in
        // Once the completion handler is called, it's safe to use the managed resource on CPU.
    }

    // Commit the command buffer.
    commandBuffer.commit()
}
```

**Objective-C**:

```objective-c
// Create a command buffer for GPU work.
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// Encode a compute pass to modify the managed texture's data with the GPU.
id <MTLComputeCommandEncoder> computeCommandEncoder = [commandBuffer computeCommandEncoderWithDispatchType:MTLDispatchTypeSerial];
[computeCommandEncoder setComputePipelineState:computePipelineStateObject];
[computeCommandEncoder setTexture:_imageTexture
                          atIndex:0];
[computeCommandEncoder dispatchThreads:gridSize
                 threadsPerThreadgroup:threadgroupSize];
[computeCommandEncoder endEncoding];

// Synchronize the managed texture with an ecoded command.
id <MTLBlitCommandEncoder> blitCommandEncoder = [commandBuffer blitCommandEncoder];
[blitCommandEncoder synchronizeResource:_imageTexture];
[blitCommandEncoder endEncoding];

// Add a completion handler and commit the command buffer.
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> commandBuffer) {
    // Once the completion handler is called, it's safe to use the managed resource on CPU.
}];
[commandBuffer commit];
```

## See Also

- [Setting resource storage modes](setting-resource-storage-modes.md)
  Set a storage mode that defines the memory location and access permissions of a resource.
- [Choosing a resource storage mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
  Select an appropriate storage mode for your textures and buffers on Apple GPUs.
- [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
  Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Copying data to a private resource](copying-data-to-a-private-resource.md)
  Use a blit command encoder to copy buffer or texture data to a private resource.
- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.
- [Reducing the memory footprint of Metal apps](reducing-the-memory-footprint-of-metal-apps.md)
  Learn best practices for using memory efficiently in iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-a-managed-resource-in-macos)*