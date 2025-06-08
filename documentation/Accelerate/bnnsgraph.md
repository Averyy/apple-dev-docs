# BNNSGraph

**Framework**: Accelerate  
**Kind**: enum

An enumeration that acts as a namespace for the Swift overlays to BNNS Graph.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
enum BNNSGraph
```

## Topics

### Compiling a graph object and creating a context
- [BNNSGraph.Context](bnnsgraph/context.md)
  A wrapper around a compiled graph object that adds a required modifiable context to support dynamically sized models and set execute-time options.
### Protocols
- [BNNSGraph.PointerArgument](bnnsgraph/pointerargument.md)
  A type that BNNS Graph accepts as an input-output argument.
### Structures
- [BNNSGraph.CompileOptions](bnnsgraph/compileoptions.md)
  The compilation options that BNNS uses when compiling a source mlmodelc file to a graph object.
- [BNNSGraph.Shape](bnnsgraph/shape.md)
  The specification of the shape of an argument.
### Enumerations
- [BNNSGraph.Error](bnnsgraph/error.md)
  Error codes that a graph context throws.

## See Also

- [enum BNNS](bnns.md)
  An enumeration that acts as a namespace for Swift overlays to BNNS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph)*