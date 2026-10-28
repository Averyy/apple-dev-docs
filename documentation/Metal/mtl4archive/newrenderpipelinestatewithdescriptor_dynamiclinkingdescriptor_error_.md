# newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a render pipeline state from the archive with a render descriptor and a dynamic linking descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTLRenderPipelineState>) newRenderPipelineStateWithDescriptor:(MTL4PipelineDescriptor *) descriptor dynamicLinkingDescriptor:(MTL4RenderPipelineDynamicLinkingDescriptor *) dynamicLinkingDescriptor error:(NSError **) error;
```

## Return Value

A render pipeline state if the method succeeds, otherwise `nil`.

## Discussion

You create any kind of render pipeline states with this method, including:

- Traditional render pipelines
- Mesh render pipelines
- Tile render pipelines

## Parameters

- `descriptor`: A render pipeline descriptor.
- `dynamicLinkingDescriptor`: A descriptor that provides additional properties to link other functions with the pipeline.
- `error`: On return, if the method fails, a pointer to an error information instance; otherwise `nil`.

## See Also

### Creating render pipeline states
- [- newRenderPipelineStateWithDescriptor:error:](./newrenderpipelinestatewithdescriptor_error_.md)
  Creates a render pipeline state from the archive with a descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4archive/newrenderpipelinestatewithdescriptor:dynamiclinkingdescriptor:error:)*