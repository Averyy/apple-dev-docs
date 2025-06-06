# MTLStitchedLibraryDescriptor

**Framework**: Metal  
**Kind**: class

A description of a new library of procedurally generated functions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MTLStitchedLibraryDescriptor
```

#### Overview

An [`MTLStitchedLibraryDescriptor`](mtlstitchedlibrarydescriptor.md) describes a library of new stitched functions. A  is a visible function you create by composing other Metal shader functions together in a function graph.

Configure a stitched library descriptor by assigning an array of one or more [`MTLFunctionStitchingGraph`](mtlfunctionstitchinggraph.md) instances, each describing a stitched function, to the [`functionGraphs`](mtlstitchedlibrarydescriptor/functiongraphs.md) property. Then assign an [`MTLFunction`](mtlfunction.md) array that includes all the functions the graphs depend on to the [`functions`](mtlstitchedlibrarydescriptor/functions.md) property.

Create a stitched library from the descriptor by passing it to the [`makeLibrary(stitchedDescriptor:)`](mtldevice/makelibrary(stitcheddescriptor:).md) method of an [`MTLDevice`](mtldevice.md). You can change the descriptor to create other libraries without affecting any existing ones.

## Topics

### Configuring a Stitched Library
- [var functions: [any MTLFunction]](mtlstitchedlibrarydescriptor/functions.md)
  The list of functions for creating the stitched library.
- [var functionGraphs: [MTLFunctionStitchingGraph]](mtlstitchedlibrarydescriptor/functiongraphs.md)
  The function graphs that define the new stitched library’s functions.
### Instance Properties
- [var binaryArchives: [any MTLBinaryArchive]](mtlstitchedlibrarydescriptor/binaryarchives.md)
- [var options: MTLStitchedLibraryOptions](mtlstitchedlibrarydescriptor/options.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md)
  Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [class MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md)
  A description of a new stitched function.
- [class MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md)
  A call graph node that describes an input to the call graph.
- [class MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md)
  A call graph node that describes a function call and its inputs.
- [protocol MTLFunctionStitchingNode](mtlfunctionstitchingnode.md)
  A protocol to identify call graph nodes.
- [class MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md)
  An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [protocol MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md)
  A protocol to identify types that customize how the Metal compiler stitches a function together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstitchedlibrarydescriptor)*