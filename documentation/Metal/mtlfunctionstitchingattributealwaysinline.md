# MTLFunctionStitchingAttributeAlwaysInline

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MTLFunctionStitchingAttributeAlwaysInline
```

```objc
@interface MTLFunctionStitchingAttributeAlwaysInline : NSObject
```

#### Overview

To inline functions in a call graph, instantiate an instance of this class and assign it as an attribute on the [`MTLFunctionStitchingGraph`](./mtlfunctionstitchinggraph.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MTLFunctionStitchingAttribute](./mtlfunctionstitchingattribute.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [var attributes: [any MTLFunctionStitchingAttribute]](./mtlfunctionstitchinggraph/attributes.md)
  A list of attributes to configure how the Metal device object generates the new stitched function.
### Stitched function libraries
- [Customizing shaders using function pointers and stitching](./customizing-shaders-using-function-pointers-and-stitching.md)
  Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [class MTLStitchedLibraryDescriptor](./mtlstitchedlibrarydescriptor.md)
  A description of a new library of procedurally generated functions.
- [class MTLFunctionStitchingGraph](./mtlfunctionstitchinggraph.md)
  A description of a new stitched function.
- [class MTLFunctionStitchingInputNode](./mtlfunctionstitchinginputnode.md)
  A call graph node that describes an input to the call graph.
- [class MTLFunctionStitchingFunctionNode](./mtlfunctionstitchingfunctionnode.md)
  A call graph node that describes a function call and its inputs.
- [protocol MTLFunctionStitchingNode](./mtlfunctionstitchingnode.md)
  A protocol to identify call graph nodes.
- [protocol MTLFunctionStitchingAttribute](./mtlfunctionstitchingattribute.md)
  A protocol to identify types that customize how the Metal compiler stitches a function together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingattributealwaysinline)*