# makeVisibleFunctionTable(descriptor:stage:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLVisibleFunctionTable>) newVisibleFunctionTableWithDescriptor:(MTLVisibleFunctionTableDescriptor *) descriptor stage:(MTLRenderStages) stage;
```

## Parameters

- `descriptor`: An [`MTLVisibleFunctionTableDescriptor`](../mtlvisiblefunctiontabledescriptor.md) instance that configures the visible function table the method creates.
- `stage`: An [`MTLRenderStages`](../mtlrenderstages.md) instance that represents the render pass stage the visible function table applies to.

## See Also

### Creating function handles and tables
- [func functionHandle(function: any MTLFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?](./functionhandle%28function,stage%29-7uvul.md)
  Creates a function handle for a shader.
- [func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLIntersectionFunctionTable)?](./makeintersectionfunctiontable%28descriptor,stage%29.md)
  Creates a new intersection function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makevisiblefunctiontable(descriptor:stage:))*