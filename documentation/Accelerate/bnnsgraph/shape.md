# BNNSGraph.Shape

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

The specification of the shape of an argument.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS
- watchOS 11.0+

## Declaration

```swift
struct Shape
```

## Overview

The [`setDynamicShapes(_:forFunction:)`](./context/setdynamicshapes%28_,forfunction%29.md) function uses arrays of [`BNNSGraph.Shape`](./shape.md) structures as its input and output. This structure wraps the C API [`bnns_graph_shape_t`](../bnns_graph_shape_t.md) type and derives its rank from the number of elements in the [`dimensions`](./shape/dimensions.md) array.

## Topics

### Creating a shape structure
- [init(arrayLiteral: Int...)](./shape/init%28arrayliteral%29.md)
  Creates a shape structure from the given array literal.
- [init([Int])](./shape/init%28_%29.md)
  Creates a shape structure from the given array elements.
### Querying a shape structure’s properties
- [var dimensions: [Int]](./shape/dimensions.md)
  An array that contains the dimensions of the shape structure.
### Type Aliases
- [BNNSGraph.Shape.ArrayLiteralElement](./shape/arrayliteralelement.md)
  The type of the elements of an array literal.

## Relationships

### Conforms To
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)

## See Also

### Specifying and querying a graph context’s properties
- [func setDynamicShapes([BNNSGraph.Shape], forFunction: String?) async throws -> [BNNSGraph.Shape]](./context/setdynamicshapes%28_,forfunction%29.md)
  Specifies the dynamic shapes for a graph and, if possible, infers the output shapes.
- [func argumentCount(forFunction: String?) -> Int](./context/argumentcount%28forfunction%29.md)
  Returns the number of arguments for the given function argument.
- [func argumentNames(forFunction: String?) -> [String]](./context/argumentnames%28forfunction%29.md)
  Returns the names of arguments for the given function argument.
- [func argumentPosition(forFunction: String?, argument: String) -> Int](./context/argumentposition%28forfunction,argument%29.md)
  Returns the index into the arguments array for the given function argument.
- [var functionCount: Int](./context/functioncount.md)
  The number of input arguments for the given function argument.
- [var functionNames: [String]](./context/functionnames.md)
  Returns the names of callable functions in the graph.
- [var checkForNaNsAndInfinities: Bool](./context/checkfornansandinfinities.md)
  A Boolean value that specifies that the context checks intermediate tensors for NaNs and infinities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/shape)*