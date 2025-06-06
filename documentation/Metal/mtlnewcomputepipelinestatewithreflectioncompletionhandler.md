# MTLNewComputePipelineStateWithReflectionCompletionHandler

**Framework**: Metal  
**Kind**: typealias

A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MTLNewComputePipelineStateWithReflectionCompletionHandler = ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void
```

## Parameters

- `computePipelineState`: An   instance if the method completes successfully; otherwise  .
- `reflection`: An   instance if the method completes successfully; otherwise  .
- `error`: On return, if an error occurs, a pointer to an error information instance; otherwise  .

## See Also

- [typealias MTLNewRenderPipelineStateCompletionHandler](mtlnewrenderpipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline.
- [typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler](mtlnewrenderpipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [typealias MTLNewComputePipelineStateCompletionHandler](mtlnewcomputepipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatewithreflectioncompletionhandler)*