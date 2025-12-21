# MTLIntersectionFunctionBufferArguments

**Framework**: Metal  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLIntersectionFunctionBufferArguments
```

#### Overview

Struct containing arguments for intersection function buffers.

## Topics

### Initializers
- [init()](mtlintersectionfunctionbufferarguments/init.md)
- [init(intersectionFunctionBuffer: UInt64, intersectionFunctionBufferSize: UInt64, intersectionFunctionStride: UInt64)](mtlintersectionfunctionbufferarguments/init(intersectionfunctionbuffer:intersectionfunctionbuffersize:intersectionfunctionstride:).md)
### Instance Properties
- [var intersectionFunctionBuffer: UInt64](mtlintersectionfunctionbufferarguments/intersectionfunctionbuffer.md)
- [var intersectionFunctionBufferSize: UInt64](mtlintersectionfunctionbufferarguments/intersectionfunctionbuffersize.md)
- [var intersectionFunctionStride: UInt64](mtlintersectionfunctionbufferarguments/intersectionfunctionstride.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
- [class MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [class MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [struct MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature.md)
  Constants for specifying different types of custom intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctionbufferarguments)*