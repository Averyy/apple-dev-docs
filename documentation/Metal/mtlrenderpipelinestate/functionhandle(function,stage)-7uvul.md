# functionHandle(function:stage:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLFunctionHandle>) functionHandleWithFunction:(id<MTLFunction>) function stage:(MTLRenderStages) stage;
```

## Parameters

- `function`: An [`MTLFunction`](../mtlfunction.md) instance that represents the shader the method creates a handle for.
- `stage`: An [`MTLRenderStages`](../mtlrenderstages.md) instance that represents the rendering stage that invokes the shader that `function` represents.

## See Also

### Creating function handles and tables
- [func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLVisibleFunctionTable)?](./makevisiblefunctiontable%28descriptor,stage%29.md)
  Creates a new visible function table.
- [func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLIntersectionFunctionTable)?](./makeintersectionfunctiontable%28descriptor,stage%29.md)
  Creates a new intersection function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/functionhandle(function:stage:)-7uvul)*