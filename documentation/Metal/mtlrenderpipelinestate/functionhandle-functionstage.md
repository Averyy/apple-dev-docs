# functionHandle(function:stage:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a function handle for a shader.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func functionHandle(function: any MTLFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?
```

## Parameters

- `function`: An   instance that represents the shader the method creates a handle for.
- `stage`: An   instance that represents the rendering stage that invokes the shader that   represents.

## See Also

- [func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLVisibleFunctionTable)?](mtlrenderpipelinestate/makevisiblefunctiontable(descriptor:stage:).md)
  Creates a new visible function table.
- [func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLIntersectionFunctionTable)?](mtlrenderpipelinestate/makeintersectionfunctiontable(descriptor:stage:).md)
  Creates a new intersection function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/functionhandle(function:stage:))*