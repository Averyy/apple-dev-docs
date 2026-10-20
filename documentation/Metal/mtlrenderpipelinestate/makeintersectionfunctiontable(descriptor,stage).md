# makeIntersectionFunctionTable(descriptor:stage:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new intersection function table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLIntersectionFunctionTable)?
```

```objc
- (id<MTLIntersectionFunctionTable>) newIntersectionFunctionTableWithDescriptor:(MTLIntersectionFunctionTableDescriptor *) descriptor stage:(MTLRenderStages) stage;
```

## Parameters

- `descriptor`: An [`MTLIntersectionFunctionTableDescriptor`](../mtlintersectionfunctiontabledescriptor.md) instance that configures the visible function table the method creates.
- `stage`: An [`MTLRenderStages`](../mtlrenderstages.md) instance that represents the render pass stage the intersection function table applies to.

## See Also

### Creating function handles and tables
- [func functionHandle(function: any MTLFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?](./functionhandle%28function,stage%29-7uvul.md)
  Creates a function handle for a shader.
- [func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLVisibleFunctionTable)?](./makevisiblefunctiontable%28descriptor,stage%29.md)
  Creates a new visible function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makeintersectionfunctiontable(descriptor:stage:))*