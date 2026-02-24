# Copying data to a private resource

**Framework**: Metal

Use a blit command encoder to copy buffer or texture data to a private resource.

#### Overview

Resources with an [`MTLStorageMode.private`](mtlstoragemode/private.md) storage mode are accessible only to the GPU. Private resources perform better than shared resources, and you don’t have to explicitly synchronize them the way you do for managed resources.

However, because private resources aren’t accessible to the CPU, you can’t populate them with it. To write data from the CPU to a private resource, you need to first write the data to a shared or managed resource. You can then copy the data from that resource to the private resource.

For more information about resource storage modes, see [`Setting resource storage modes`](setting-resource-storage-modes.md).

##### Copying Data From a Shared Buffer to a Private Buffer

First, create a shared buffer and populate its contents using the [`makeBuffer(bytes:length:options:)`](mtldevice/makebuffer(bytes:length:options:).md) method.

**Swift**:

```swift
// Create and populate a source buffer.
let bufferData = <#UnsafeRawPointer#>, bufferLength = <#Int#>
let bufferOptions = MTLResourceOptions.storageModeShared
if let sourceBuffer = device.makeBuffer(bytes: bufferData, length: bufferLength, options: bufferOptions) {
    ...
}
```

**Objective-C**:

```objective-c
// Create and populate a source buffer.
id <MTLBuffer> _sourceBuffer;
_sourceBuffer = [_device newBufferWithBytes:bufferData
                                     length:bufferLength
                                    options:MTLResourceStorageModeShared];
```

Next, create a private buffer that’s large enough to store your buffer data using the [`makeBuffer(length:options:)`](mtldevice/makebuffer(length:options:).md) method.

**Swift**:

```swift
// Create a private buffer.
if let privateBuffer = device.makeBuffer(length: bufferLength, options: .storageModePrivate) {
    ...
}
```

**Objective-C**:

```objective-c
// Create a private buffer.
id <MTLBuffer> _privateBuffer;
_privateBuffer = [_device newBufferWithLength:bufferLength
                                      options:MTLResourceStorageModePrivate];
```

Finally, encode and commit an [`copy(from:sourceOffset:to:destinationOffset:size:)`](mtlblitcommandencoder/copy(from:sourceoffset:to:destinationoffset:size:).md) command. Set the shared buffer as the `sourceBuffer` parameter. Set the private buffer as the `destinationBuffer` parameter.

**Swift**:

```swift
// Create a command buffer for GPU work.
guard let commandBuffer = commandQueue.makeCommandBuffer() else { return }

// Create a blit command encoder.
guard let blitCommandEncoder = commandBuffer.makeBlitCommandEncoder() else { return }

// Copy data from the source buffer to the private buffer.
let sourceBuffer = <#MTLBuffer#>, privateBuffer = <#MTLBuffer#>, bufferLength = <#Int#>
blitCommandEncoder.copy(from: sourceBuffer, sourceOffset: 0, to: privateBuffer, destinationOffset: 0, size: bufferLength)
blitCommandEncoder.endEncoding()

// Add a completion handler and commit the command buffer.
let commandBufferHandler = <#MTLCommandBufferHandler#>
commandBuffer.addCompletedHandler(commandBufferHandler)
commandBuffer.commit()
```

**Objective-C**:

```objective-c
// Create a command buffer for GPU work.
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// Encode a blit pass to copy data from the source buffer to the private buffer.
id <MTLBlitCommandEncoder> blitCommandEncoder = [commandBuffer blitCommandEncoder];
[blitCommandEncoder copyFromBuffer:_sourceBuffer
                      sourceOffset:0
                          toBuffer:_privateBuffer
                 destinationOffset:0 size:bufferLength];
[blitCommandEncoder endEncoding];

// Add a completion handler and commit the command buffer.
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> cb) {
    // Populate private buffer.
}];
[commandBuffer commit];
```

> **Note**:  In macOS, Metal doesn’t reformat buffer contents or layout to improve GPU access. There’s no difference in GPU performance between managed or private buffers, so there’s no performance benefit in copying data from a managed buffer to a private buffer.

##### Copying Data From a Shared Buffer to a Private Texture

Use this implementation to copy texture data from the CPU to a private texture in one operation, without having to synchronize a managed texture.

First, create a shared buffer and populate its contents with your texture data.

**Swift**:

```swift
// Create and populate a source buffer with texture data.
let textureData = <#UnsafeRawPointer#>, textureSize = <#MTLSize#>
let textureLength = pixelSize * textureSize.width * textureSize.height
let textureOptions = MTLResourceOptions.storageModeShared
if let sourceBuffer = device.makeBuffer(bytes: textureData, length: textureLength, options: textureOptions) {
    ...
}
```

**Objective-C**:

```objective-c
// Create and populate a source buffer with texture data.
id <MTLBuffer> _sourceBuffer;
_sourceBuffer = [_device newBufferWithBytes:textureData
                                     length:pixelSize*textureSize.width*textureSize.height
                                    options:MTLResourceStorageModeShared];
```

Next, create a private texture with a suitable configuration for the texture data.

**Swift**:

```swift
// Create a texture descriptor.
let textureDescriptor = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: .bgra8Unorm,
                                                                 width: textureSize.width,
                                                                 height: textureSize.height,
                                                                 mipmapped: true)

// Set the texture descriptor's storage mode to private.
textureDescriptor.storageMode = MTLStorageMode.private

// Create a private texture from the descriptor.
let privateTexture = device.makeTexture(descriptor: textureDescriptor)
```

**Objective-C**:

```objective-c
// Create a texture descriptor.
MTLTextureDescriptor *textureDescriptor = [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm
                                                                                             width:textureSize.width
                                                                                            height:textureSize.height
                                                                                         mipmapped:NO];

// Set the texture descriptor's storage mode to private.
textureDescriptor.storageMode = MTLStorageModePrivate;

// Create a private texture.
id <MTLTexture> _privateTexture;
_privateTexture = [_device newTextureWithDescriptor:textureDescriptor];
```

Finally, encode and commit an [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)`](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md) command. Set the shared buffer as the `sourceBuffer` parameter. Set the private texture as the `destinationTexture` parameter.

**Swift**:

```swift
// Create a command buffer for GPU work.
guard let commandBuffer = commandQueue.makeCommandBuffer() else { return }

// Create a blit command encoder.
guard let blitCommandEncoder = commandBuffer.makeBlitCommandEncoder() else { return }

// Copy data from the source buffer to the private texture.
sourceBuffer = <#MTLBuffer#>, textureSize = <#MTLSize#>, privateTexture = <#MTLTexture#>, textureOrigin = <#MTLOrigin#>
let bytesPerRow = pixelSize * textureSize.width
let bytesPerImage = pixelSize * textureSize.width * textureSize.height
blitCommandEncoder.copy(from: sourceBuffer, sourceOffset: 0, sourceBytesPerRow: bytesPerRow,
                        sourceBytesPerImage: bytesPerImage, sourceSize: textureSize, to: privateTexture,
                        destinationSlice: 0, destinationLevel: 0, destinationOrigin: textureOrigin)
blitCommandEncoder.endEncoding()

// Add a completion handler and commit the command buffer.
let commandBufferHandler = <#MTLCommandBufferHandler#>
commandBuffer.addCompletedHandler(commandBufferHandler)
commandBuffer.commit()
```

**Objective-C**:

```objective-c
// Create a command buffer for GPU work.
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// Encode a blit pass to copy data from the source buffer to the private texture.
id <MTLBlitCommandEncoder> blitCommandEncoder = [commandBuffer blitCommandEncoder];
[blitCommandEncoder copyFromBuffer:_sourceBuffer
                      sourceOffset:0
                 sourceBytesPerRow:pixelSize*textureSize.width
               sourceBytesPerImage:pixelSize*textureSize.width*textureSize.height
                        sourceSize:textureSize
                         toTexture:_privateTexture
                  destinationSlice:0
                  destinationLevel:0
                 destinationOrigin:textureOrigin];
[blitCommandEncoder endEncoding];

// Add a completion handler and commit the command buffer.
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> cb) {
    // Private texture is populated.
}];
[commandBuffer commit];
```

##### Copying Data From a Shared or Managed Texture to a Private Texture

First, create a shared texture or for Mac apps, a managed texture. For more information about creating buffers and textures with specific storage modes, see [`Setting resource storage modes`](setting-resource-storage-modes.md).

Then populate the contents of the source texture using the [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md) method.

**Swift**:

```swift
// Create and populate a source texture.
let sourceTexture = device.makeTexture(descriptor: textureDescriptor)
let region = MTLRegionMake2D(textureOrigin.x, textureOrigin.y, textureSize.width, textureSize.height)
let textureData = <#UnsafeRawPointer#>
let bytesPerRow = pixelSize * textureSize.width
sourceTexture.replace(region: region, mipmapLevel: 0, withBytes: textureData, bytesPerRow: bytesPerRow)
```

**Objective-C**:

```objective-c
// Create and populate a source texture.
id <MTLTexture> _sourceTexture;
_sourceTexture = [_device newTextureWithDescriptor:textureDescriptor];
[_sourceTexture replaceRegion:MTLRegionMake2D(textureOrigin.x, textureOrigin.y, textureSize.width, textureSize.height)
                  mipmapLevel:0
                    withBytes:textureData
                  bytesPerRow:pixelSize*textureSize.width];
```

Next, create a private texture with a suitable configuration for your texture data. If appropriate, reuse the texture descriptor that you configured for the shared or managed texture.

**Swift**:

```swift
// Set the texture descriptor's storage mode to private.
textureDescriptor.storageMode = MTLStorageMode.private

// Create a private texture from the descriptor.
let privateTexture = device.makeTexture(descriptor: textureDescriptor)
```

**Objective-C**:

```objective-c
// Set the texture descriptor's storage mode to `MTLStorageModePrivate`.
textureDescriptor.storageMode = MTLStorageModePrivate;

// Create a private texture.
id <MTLTexture> _privateTexture;
_privateTexture = [_device newTextureWithDescriptor:textureDescriptor];
```

Finally, encode and commit an [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md) command. Set the shared or managed texture as the `sourceTexture` parameter. Set the private texture as the `destinationTexture` parameter.

**Swift**:

```swift
// Create a command buffer for GPU work.
guard let commandBuffer = commandQueue.makeCommandBuffer() else { return }

// Create a blit command encoder.
guard let blitCommandEncoder = commandBuffer.makeBlitCommandEncoder() else { return }

// Copy data from the source texture to the private texture.
blitCommandEncoder.copy(from: sourceTexture, sourceSlice: 0, sourceLevel: 0, sourceOrigin: textureOrigin,
                        sourceSize: textureSize, to: privateTexture, destinationSlice: 0, destinationLevel: 0,
                        destinationOrigin: textureOrigin)
blitCommandEncoder.endEncoding()

// Add a completion handler and commit the command buffer.
let commandBufferHandler = <#MTLCommandBufferHandler#>
commandBuffer.addCompletedHandler(commandBufferHandler)
commandBuffer.commit()
```

**Objective-C**:

```objective-c
// Create a command buffer for GPU work.
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// Encode a blit pass to copy data from the source texture to the private texture.
id <MTLBlitCommandEncoder> blitCommandEncoder = [commandBuffer blitCommandEncoder];
[blitCommandEncoder copyFromTexture:_sourceTexture
                        sourceSlice:0
                        sourceLevel:0
                       sourceOrigin:textureOrigin
                         sourceSize:textureSize
                          toTexture:_privateTexture
                   destinationSlice:0
                   destinationLevel:0
                  destinationOrigin:textureOrigin];
[blitCommandEncoder endEncoding];

// Add a completion handler and commit the command buffer.
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> cb) {
    // Private texture is populated.
}];
[commandBuffer commit];
```

Copying data from a managed texture to a private texture involves two copy operations. For the first operation, Metal synchronizes the managed texture and copies the texture data from CPU-accessible memory to GPU-accessible memory. For the second operation, Metal copies the texture data from the managed texture to the private texture.

##### Copying Data From a Private Texture to a Shared Buffer

Use this implementation to copy texture data from the GPU to a shared buffer, without having to synchronize a managed texture.

First, create a private texture.

**Swift**:

```swift
// Create a texture descriptor.
let textureDescriptor = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: .bgra8Unorm,
                                                                 width: textureSize.width,
                                                                 height: textureSize.height,
                                                                 mipmapped: false)

// Set the texture descriptor's storage mode to private.
textureDescriptor.storageMode = MTLStorageMode.private

// Create a private texture from the descriptor.
let sourceTexture = device.makeTexture(descriptor: textureDescriptor)
```

**Objective-C**:

```objective-c
// Create a texture descriptor.
MTLTextureDescriptor *textureDescriptor = [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm
                                                                                             width:textureSize.width
                                                                                            height:textureSize.height
                                                                                         mipmapped:NO];

// Set the texture descriptor's storage mode to `MTLStorageModePrivate`.
textureDescriptor.storageMode = MTLStorageModePrivate;

// Create a private texture.
id <MTLTexture> _sourceTexture;
_sourceTexture = [_device newTextureWithDescriptor:textureDescriptor];
```

Next, create a shared buffer that’s large enough to store your texture data.

**Swift**:

```swift
// Create a shared buffer.
let textureLength = pixelSize * textureSize.width * textureSize.height
let textureOptions = MTLResourceOptions.storageModeShared
if let sourceBuffer = device.makeBuffer(length: textureLength, options: textureOptions) {
    ...
}
```

**Objective-C**:

```objective-c
// Create a shared buffer.
id <MTLBuffer> _sharedBuffer;
_sharedBuffer = [_device newBufferWithLength: pixelSize*textureSize.width*textureSize.height
                                     options: MTLResourceStorageModeShared];
```

Next, encode a compute, render, or blit pass to populate the contents of your private texture.

**Swift**:

```swift
// Create a command buffer for GPU work.
guard let commandBuffer = commandQueue.makeCommandBuffer() else { return }

// Encode a compute, render, or blit pass to populate the source texture's contents.
...
```

**Objective-C**:

```objective-c
// Create a command buffer for GPU work.
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

/* Encode a compute, render, or blit pass to populate the source texture's contents. */
/* ... */
```

Finally, encode and commit an [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:).md) command. Set the private texture as the `sourceTexture` parameter. Set the shared buffer as the `destinationBuffer` parameter.

**Swift**:

```swift
// Create a blit command encoder.
guard let blitCommandEncoder = commandBuffer.makeBlitCommandEncoder() else { return }

// Encode a blit pass to copy data from the source texture to the shared buffer.
let bytesPerRow = pixelSize * textureSize.width
let bytesPerImage = pixelSize * textureSize.width * textureSize.height
let privateBuffer = <#MTLBuffer#>, bufferLength = <#Int#>
blitCommandEncoder.copy(from: sourceTexture, sourceSlice: 0, sourceLevel: 0,
                        sourceOrigin: textureOrigin, sourceSize: textureSize, to: sharedBuffer,
                        destinationOffset: 0, destinationBytesPerRow: bytesPerRow,
                        destinationBytesPerImage: bytesPerImage)
blitCommandEncoder.endEncoding()

// Add a completion handler and commit the command buffer.
let commandBufferHandler = <#MTLCommandBufferHandler#>
commandBuffer.addCompletedHandler(commandBufferHandler)
commandBuffer.commit()
```

**Objective-C**:

```objective-c
// Encode a blit pass to copy data from the source texture to the shared buffer.
id <MTLBlitCommandEncoder> blitCommandEncoder = [commandBuffer blitCommandEncoder];
[blitCommandEncoder copyFromTexture:_sourceTexture
                        sourceSlice:0
                        sourceLevel:0
                       sourceOrigin:textureOrigin
                         sourceSize:textureSize
                           toBuffer:_sharedBuffer
                  destinationOffset:0
             destinationBytesPerRow:pixelSize*textureSize.width
           destinationBytesPerImage:pixelSize*textureSize.width*textureSize.height];
[blitCommandEncoder endEncoding];

// Add a completion handler and commit the command buffer.
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> cb) {
    // Shared buffer is populated.
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
- [Synchronizing a managed resource in macOS](synchronizing-a-managed-resource-in-macos.md)
  Manually synchronize memory for a Metal resource in apps.
- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.
- [Reducing the memory footprint of Metal apps](reducing-the-memory-footprint-of-metal-apps.md)
  Learn best practices for using memory efficiently in iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/copying-data-to-a-private-resource)*