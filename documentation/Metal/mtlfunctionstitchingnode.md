# MTLFunctionStitchingNode

**Framework**: Metal  
**Kind**: protocol

A protocol to identify call graph nodes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFunctionStitchingNode : NSCopying, NSObjectProtocol
```

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md)
- [MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md)

## See Also

- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md)
  Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [class MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md)
  A description of a new library of procedurally generated functions.
- [class MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md)
  A description of a new stitched function.
- [class MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md)
  A call graph node that describes an input to the call graph.
- [class MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md)
  A call graph node that describes a function call and its inputs.
- [class MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md)
  An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [protocol MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md)
  A protocol to identify types that customize how the Metal compiler stitches a function together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingnode)*