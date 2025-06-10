# init(buffer:vertexFormat:semantic:vertexCount:dataOffset:dataStride:)

**Framework**: SceneKit  
**Kind**: init

Creates a geometry source whose vertex data resides in the specified Metal buffer, allowing modification through a Metal compute shader.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(buffer: any MTLBuffer, vertexFormat: MTLVertexFormat, semantic: SCNGeometrySource.Semantic, vertexCount: Int, dataOffset offset: Int, dataStride stride: Int)
```

#### Return Value

A new geometry source object.

#### Discussion

Use this method to create a geometry source whose underlying data can be modified at render time by a Metal compute shader running on the GPU. To create a [`MTLBuffer`](https://developer.apple.com/documentation/Metal/MTLBuffer) object for use with a geometry source, use the [`device`](scnscenerenderer/device.md) property of the SceneKit view (or other renderer) responsible for drawing your scene.

```objc
// Create and fill a buffer.
id <MTLDevice> device = self.scnView.device;
self.geometryBuffer = [device newBufferWithBytes:myData length:myLength options:myOptions];
// Create a geometry source from the buffer.
SCNGeometrySource *source = [SCNGeometrySource geometrySourceWithBuffer:buffer
                             vertexFormat:myVertexFormat
                                 semantic:SCNGeometrySourceSemanticVertex
                              vertexCount:myVertexCount
                               dataOffset:0
                               dataStride:0];
```

Then, to modify the buffer’s contents at render time, implement a scene renderer delegate and schedule a compute command encoder during a render delegate method such as [`renderer(_:willRenderScene:atTime:)`](scnscenerendererdelegate/renderer(_:willrenderscene:attime:).md).

```objc
- (void)renderer:(id <SCNSceneRenderer>)aRenderer willRenderScene:(SCNScene *)scene atTime:(NSTimeInterval)time {
     // Get a command buffer and compute encoder from the view (or other renderer).
     id<MTLCommandBuffer> myCommandBuffer = [aRenderer.commandQueue commandBuffer];
     id<MTLComputeCommandEncoder> myComputeEncoder = [myCommandBuffer computeCommandEncoder];
 
     // Configure the compute command encoder.
     // (Note pipeline state is preconfigured outside of the render loop.)
     [myComputeEncoder setComputePipelineState:self.pipelineState];
     [myComputeEncoder setBuffer:self.geometryBuffer offset:0 atIndex:0];
 
     // Schedule the compute command and commit the command buffer.
     [myComputeEncoder dispatchThreadgroups:myThreadgroupCount
                      threadsPerThreadgroup:myThreadCount];
     [myComputeEncoder endEncoding];
     [myCommandBuffer commit];
}
```

> **Note**:  Geometry sources backed by a Metal buffer are available only with SceneKit views (or other renderers) whose [`renderingAPI`](scnscenerenderer/renderingapi.md) property is [`SCNRenderingAPI.metal`](scnrenderingapi/metal.md). Metal commands that modify the buffer’s contents must be enqueued from within one of the render loop methods defined in the [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) protocol. The result of attempting to modify a buffer at any other time is undefined.

## Parameters

- `buffer`: A Metal buffer containing per-vertex data for the geometry source.
- `vertexFormat`: The type of per-vertex data in the buffer. A   value defines the number of components for each vector in the geometry source and the data type and size of each component.
- `semantic`: The semantic value (or attribute) that the geometry source describes for each vertex. See Geometry Semantic Identifiers for available values.
- `vertexCount`: The number of vertices in the geometry source.
- `offset`: The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.
- `stride`: The number of bytes from each vector to the next in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/init(buffer:vertexformat:semantic:vertexcount:dataoffset:datastride:))*