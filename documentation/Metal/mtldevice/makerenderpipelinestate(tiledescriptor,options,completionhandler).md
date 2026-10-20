# makeRenderPipelineState(tileDescriptor:options:completionHandler:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously creates a tile shader’s render pipeline state and reflection information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func makeRenderPipelineState(tileDescriptor descriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: @escaping @Sendable ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)
```

```swift
func makeRenderPipelineState(tileDescriptor descriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) async throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

```objc
- (void) newRenderPipelineStateWithTileDescriptor:(MTLTileRenderPipelineDescriptor *) descriptor options:(MTLPipelineOption) options completionHandler:(MTLNewRenderPipelineStateWithReflectionCompletionHandler) completionHandler;
```

## Parameters

- `descriptor`: An [`MTLTileRenderPipelineDescriptor`](../mtltilerenderpipelinedescriptor.md) instance.
- `options`: An [`MTLPipelineOption`](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.
- `completionHandler`: A Swift closure or an Objective-C block the method calls when it finishes creating the render pipeline state.

## Default Implementations

### MTLDevice Implementations
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](./makerenderpipelinestate%28tiledescriptor,options%29.md)
  Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.

## See Also

### Creating tile render pipeline states
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](./makerenderpipelinestate%28tiledescriptor,options%29.md)
  Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState](./makerenderpipelinestate%28tiledescriptor,options,reflection%29.md)
  Synchronously creates a tile shader’s render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:completionhandler:))*