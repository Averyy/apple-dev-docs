# MTLFunctionHandle

**Framework**: Metal  
**Kind**: protocol

An object representing a function that you can add to a visible function table.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFunctionHandle : NSObjectProtocol, Sendable
```

## Topics

### Querying handle properties
- [var device: any MTLDevice](mtlfunctionhandle/device.md)
  The device object that created the shader function.
- [var functionType: MTLFunctionType](mtlfunctionhandle/functiontype.md)
  The shader function’s type.
- [var name: String](mtlfunctionhandle/name.md)
  The function’s name.
### Instance Properties
- [var gpuResourceID: MTLResourceID](mtlfunctionhandle/gpuresourceid.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTLFunctionDescriptor](mtlfunctiondescriptor.md)
  A description of a function object to create.
- [protocol MTLFunction](mtlfunction.md)
  A interface that represents a public shader function in a Metal library.
- [class MTLVisibleFunctionTableDescriptor](mtlvisiblefunctiontabledescriptor.md)
  A specification of how to create a visible function table.
- [protocol MTLVisibleFunctionTable](mtlvisiblefunctiontable.md)
  A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.
- [class MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [class MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [protocol MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionhandle)*