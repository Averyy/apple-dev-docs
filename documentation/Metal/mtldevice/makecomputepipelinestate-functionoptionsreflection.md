# makeComputePipelineState(function:options:reflection:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Synchronously creates a compute pipeline state and reflection with a function instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeComputePipelineState(function computeFunction: any MTLFunction, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState
```

#### Discussion

Use the compute pipeline state to configure a compute pass by calling the [`setComputePipelineState(_:)`](mtlcomputecommandencoder/setcomputepipelinestate(_:).md) method of an [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instance.

## Parameters

- `computeFunction`: An   instance.
- `options`: An   instance that represents the reflection information you want the method to generate.
- `reflection`: Set to   if you don’t need reflection data.

## See Also

- [func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState](mtldevice/makecomputepipelinestate(descriptor:options:reflection:).md)
  Synchronously creates a compute pipeline state and reflection information.
- [func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)](mtldevice/makecomputepipelinestate(descriptor:options:completionhandler:).md)
  Asynchronously creates a compute pipeline state and reflection information.
- [func makeComputePipelineState(function: any MTLFunction) throws -> any MTLComputePipelineState](mtldevice/makecomputepipelinestate(function:).md)
  Synchronously creates a compute pipeline state with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, completionHandler: ((any MTLComputePipelineState)?, (any Error)?) -> Void)](mtldevice/makecomputepipelinestate(function:completionhandler:).md)
  Asynchronously creates a compute pipeline state with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, options: MTLPipelineOption, completionHandler: ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)](mtldevice/makecomputepipelinestate(function:options:completionhandler:).md)
  Asynchronously creates a compute pipeline state and reflection with a function instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecomputepipelinestate(function:options:reflection:))*