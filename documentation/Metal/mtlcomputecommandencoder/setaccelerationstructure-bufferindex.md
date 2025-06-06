# setAccelerationStructure(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Binds an acceleration structure to the buffer argument table, allowing functions to access it on the GPU.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setAccelerationStructure(_ accelerationStructure: (any MTLAccelerationStructure)?, bufferIndex: Int)
```

## Parameters

- `accelerationStructure`: An   instance to bind to the argument table.
- `bufferIndex`: The index the structure binds to in the argument table.

## See Also

- [func setIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](mtlcomputecommandencoder/setintersectionfunctiontable(_:bufferindex:).md)
  Binds an intersection function table to the buffer argument table, making it callable in your Metal shaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setaccelerationstructure(_:bufferindex:))*