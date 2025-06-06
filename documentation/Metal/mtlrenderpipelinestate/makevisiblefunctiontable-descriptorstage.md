# makeVisibleFunctionTable(descriptor:stage:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new visible function table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLVisibleFunctionTable)?
```

## Parameters

- `descriptor`: An   instance that configures the visible function table the method creates.
- `stage`: An   instance that represents the render pass stage the visible function table applies to.

## See Also

- [func functionHandle(function: any MTLFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?](mtlrenderpipelinestate/functionhandle(function:stage:).md)
  Creates a function handle for a shader.
- [func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLIntersectionFunctionTable)?](mtlrenderpipelinestate/makeintersectionfunctiontable(descriptor:stage:).md)
  Creates a new intersection function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makevisiblefunctiontable(descriptor:stage:))*