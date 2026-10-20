# MTLNewComputePipelineStateCompletionHandler

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A completion handler signature a method calls when it finishes creating a compute pipeline.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLNewComputePipelineStateCompletionHandler = ((any MTLComputePipelineState)?, (any Error)?) -> Void
```

```c
typedef void (^)(id<MTLComputePipelineState>, NSError *) MTLNewComputePipelineStateCompletionHandler;
```

## Parameters

- `computePipelineState`: An [`MTLComputePipelineState`](./mtlcomputepipelinestate.md) instance if the method completes successfully; otherwise `nil`.
- `error`: On return, if an error occurs, a pointer to an error information instance; otherwise `nil`.

## See Also

### Supporting types
- [typealias MTLNewRenderPipelineStateCompletionHandler](./mtlnewrenderpipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline.
- [typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler](./mtlnewrenderpipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [typealias MTLNewComputePipelineStateWithReflectionCompletionHandler](./mtlnewcomputepipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatecompletionhandler)*