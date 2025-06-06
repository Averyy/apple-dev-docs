# BNNSGraph.Shape

**Framework**: Accelerate  
**Kind**: struct

The specification of the shape of an argument.

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
struct Shape
```

#### Overview

The [`setDynamicShapes(_:forFunction:)`](bnnsgraph/context/setdynamicshapes(_:forfunction:).md) function uses arrays of [`BNNSGraph.Shape`](bnnsgraph/shape.md) structures as its input and output. This structure wraps the C API [`bnns_graph_shape_t`](bnns_graph_shape_t.md) type and derives its rank from the number of elements in the [`dimensions`](bnnsgraph/shape/dimensions.md) array.

## Topics

### Creating a shape structure
- [init(arrayLiteral: Int...)](bnnsgraph/shape/init(arrayliteral:).md)
  Creates a shape structure from the given array literal.
- [init([Int])](bnnsgraph/shape/init(_:).md)
  Creates a shape structure from the given array elements.
### Querying a shape structure’s properties
- [var dimensions: [Int]](bnnsgraph/shape/dimensions.md)
  An array that contains the dimensions of the shape structure.
### Type Aliases
- [BNNSGraph.Shape.ArrayLiteralElement](bnnsgraph/shape/arrayliteralelement.md)
  The type of the elements of an array literal.

## Relationships

### Conforms To
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)

## See Also

- [func setBatchSize(Int, forFunction: String?) async](bnnsgraph/context/setbatchsize(_:forfunction:).md)
  Sets the batch size for a graph.
- [func setDynamicShapes([BNNSGraph.Shape], forFunction: String?) async throws -> [BNNSGraph.Shape]](bnnsgraph/context/setdynamicshapes(_:forfunction:).md)
  Specifies the dynamic shapes for a graph and, if possible, infers the output shapes.
- [func argumentCount(forFunction: String?) -> Int](bnnsgraph/context/argumentcount(forfunction:).md)
  Returns the number of arguments for the given function argument.
- [func argumentNames(forFunction: String?) -> [String]](bnnsgraph/context/argumentnames(forfunction:).md)
  Returns the names of arguments for the given function argument.
- [func argumentPosition(forFunction: String?, argument: String) -> Int](bnnsgraph/context/argumentposition(forfunction:argument:).md)
  Returns the index into the arguments array for the given function argument.
- [var functionCount: Int](bnnsgraph/context/functioncount.md)
  The number of input arguments for the given function argument.
- [var functionNames: [String]](bnnsgraph/context/functionnames.md)
  Returns the names of callable functions in the graph.
- [var checkForNaNsAndInfinities: Bool](bnnsgraph/context/checkfornansandinfinities.md)
  A Boolean value that specifies that the context checks intermediate tensors for NaNs and infinities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/shape)*