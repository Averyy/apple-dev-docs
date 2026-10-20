# setIntersectionFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Binds an intersection function table to the buffer argument table, making it callable in your Metal shaders.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setIntersectionFunctionTable(_ intersectionFunctionTable: (any MTLIntersectionFunctionTable)?, bufferIndex: Int)
```

```objc
- (void) setIntersectionFunctionTable:(id<MTLIntersectionFunctionTable>) intersectionFunctionTable atBufferIndex:(NSUInteger) bufferIndex;
```

## Parameters

- `intersectionFunctionTable`: The [`MTLIntersectionFunctionTable`](../mtlintersectionfunctiontable.md) to bind.
- `bufferIndex`: The index in the buffer argument table the intersection function table binds to.

## See Also

### Binding arguments for acceleration structures
- [func setAccelerationStructure((any MTLAccelerationStructure)?, bufferIndex: Int)](./setaccelerationstructure%28_,bufferindex%29.md)
  Binds an acceleration structure to the buffer argument table, allowing functions to access it on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontable(_:bufferindex:))*