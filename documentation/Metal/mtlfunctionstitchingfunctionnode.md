# MTLFunctionStitchingFunctionNode

**Framework**: Metal  
**Kind**: class

A call graph node that describes a function call and its inputs.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MTLFunctionStitchingFunctionNode
```

#### Overview

When the Metal device object evaluates the function graph to compile the stitched function, it evaluates the nodes stored in the [`arguments`](mtlfunctionstitchingfunctionnode/arguments.md) property that it hasn’t already evaluated, and then calls the function specified by [`name`](mtlfunctionstitchingfunctionnode/name.md) to generate the node’s output.

If the function has side effects on the input data, use the [`controlDependencies`](mtlfunctionstitchingfunctionnode/controldependencies.md) property on other nodes to specify whether the Metal device object needs to evaluate this node first.

## Topics

### Initializing a function node
- [init(name: String, arguments: [any MTLFunctionStitchingNode], controlDependencies: [MTLFunctionStitchingFunctionNode])](mtlfunctionstitchingfunctionnode/init(name:arguments:controldependencies:).md)
  Creates a new function node.
### Configuring a function node
- [var name: String](mtlfunctionstitchingfunctionnode/name.md)
  The name of the function to call.
- [var arguments: [any MTLFunctionStitchingNode]](mtlfunctionstitchingfunctionnode/arguments.md)
  An ordered list of the nodes that provide the function’s arguments.
- [var controlDependencies: [MTLFunctionStitchingFunctionNode]](mtlfunctionstitchingfunctionnode/controldependencies.md)
  The list of nodes that need to execute before executing the node.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MTLFunctionStitchingNode](mtlfunctionstitchingnode.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md)
  Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [class MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md)
  A description of a new library of procedurally generated functions.
- [class MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md)
  A description of a new stitched function.
- [class MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md)
  A call graph node that describes an input to the call graph.
- [protocol MTLFunctionStitchingNode](mtlfunctionstitchingnode.md)
  A protocol to identify call graph nodes.
- [class MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md)
  An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [protocol MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md)
  A protocol to identify types that customize how the Metal compiler stitches a function together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode)*