---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/intorpair"
framework: "mlx-swift/MLX"
---

# IntOrPair

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Parameter for convolutions allowing single integers or tuples.

## Declaration

```swift
struct IntOrPair
```

## Overview

For example the numeric parameters here are all [`IntOrPair`](./intorpair.md):

```swift
conv2d(input, weights, stride: 3, padding: [2, 2], padding: .init((2, 3)))
```

### See Also:

- [`IntOrArray`](./intorarray.md)

## Topics

### Initializers
- [init(some Collection<Int>)](./intorpair/init%28_%29-2bpnr.md)
- [init((Int, Int))](./intorpair/init%28_%29-4gcmc.md)
- [init(Int)](./intorpair/init%28_%29-650zv.md)
- [init(arrayLiteral: Int...)](./intorpair/init%28arrayliteral%29.md)
- [init(integerLiteral: Int)](./intorpair/init%28integerliteral%29.md)
### Instance Properties
- [var first: Int](./intorpair/first.md)
- [var second: Int](./intorpair/second.md)
- [let values: (Int, Int)](./intorpair/values.md)

## Relationships

### Conforms To
- Swift.ExpressibleByArrayLiteral
- Swift.ExpressibleByIntegerLiteral
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Parameter Types
- [struct IntOrTriple](./intortriple.md)
  Parameter for convolutions allowing single integers or triples.
- [enum IntOrArray](./intorarray.md)
  Parameter for convolutions allowing single integers or arrays.
- [enum FloatOrArray](./floatorarray.md)
  Parameter for taking a single or multiple Float values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/intorpair)*