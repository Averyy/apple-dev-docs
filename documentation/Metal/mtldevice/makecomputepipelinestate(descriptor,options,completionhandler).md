# makeComputePipelineState(descriptor:options:completionHandler:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously creates a compute pipeline state and reflection information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, completionHandler: @escaping @Sendable ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)
```

```swift
func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption) async throws -> (any MTLComputePipelineState, MTLComputePipelineReflection?)
```

```objc
- (void) newComputePipelineStateWithDescriptor:(MTLComputePipelineDescriptor *) descriptor options:(MTLPipelineOption) options completionHandler:(MTLNewComputePipelineStateWithReflectionCompletionHandler) completionHandler;
```

## Discussion

Use the compute pipeline state to configure a compute pass by calling the [`setComputePipelineState(_:)`](../mtlcomputecommandencoder/setcomputepipelinestate%28_%29.md) method of an [`MTLComputeCommandEncoder`](../mtlcomputecommandencoder.md) instance.

## Parameters

- `descriptor`: An [`MTLComputePipelineDescriptor`](../mtlcomputepipelinedescriptor.md) instance.
- `options`: An [`MTLPipelineOption`](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.
- `completionHandler`: A Swift closure or an Objective-C block the method calls when it finishes creating the compute pipeline state.

## Default Implementations

### MTLDevice Implementations
- [func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLComputePipelineState, MTLComputePipelineReflection?)](./makecomputepipelinestate%28descriptor,options%29.md)

## See Also

### Creating compute pipeline states
- [func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState](./makecomputepipelinestate%28descriptor,options,reflection%29.md)
  Synchronously creates a compute pipeline state and reflection information.
- [func makeComputePipelineState(function: any MTLFunction) throws -> any MTLComputePipelineState](./makecomputepipelinestate%28function%29.md)
  Synchronously creates a compute pipeline state with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, completionHandler: ((any MTLComputePipelineState)?, (any Error)?) -> Void)](./makecomputepipelinestate%28function,completionhandler%29.md)
  Asynchronously creates a compute pipeline state with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState](./makecomputepipelinestate%28function,options,reflection%29.md)
  Synchronously creates a compute pipeline state and reflection with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, options: MTLPipelineOption, completionHandler: ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)](./makecomputepipelinestate%28function,options,completionhandler%29.md)
  Asynchronously creates a compute pipeline state and reflection with a function instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecomputepipelinestate(descriptor:options:completionhandler:))*