# makeRenderPipelineState(tileDescriptor:options:reflection:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Synchronously creates a tile shader’s render pipeline state and reflection information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func makeRenderPipelineState(tileDescriptor descriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState
```

#### Return Value

A new [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `descriptor`: An   instance.
- `options`: An   instance that represents the reflection information you want the method to generate.
- `reflection`: Pass   in either language when you don’t need reflection data.   Otherwise on return, if the method completes successfully,   it assigns an   instance to the pointee,   which contains the details about the function arguments.

## See Also

- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](mtldevice/makerenderpipelinestate(tiledescriptor:options:).md)
  Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)](mtldevice/makerenderpipelinestate(tiledescriptor:options:completionhandler:).md)
  Asynchronously creates a tile shader’s render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:reflection:))*