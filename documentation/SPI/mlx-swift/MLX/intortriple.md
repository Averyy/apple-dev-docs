---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/intortriple"
framework: "mlx-swift/MLX"
---

# IntOrTriple

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Parameter for convolutions allowing single integers or triples.

## Declaration

```swift
struct IntOrTriple
```

#### Overview

For example the numeric parameters here are all [`IntOrTriple`](./intortriple.md):

```swift
conv3d(input, weights, stride: 3, padding: [2, 2, 1], padding: .init((2, 3, 1)))
```

##### See Also:

- [`IntOrPair`](./intorpair.md)

## Topics

### Initializers
- [init(Int)](./intortriple/init%28_%29-3b97h.md)
- [init(some Collection<Int>)](./intortriple/init%28_%29-76q0.md)
- [init((Int, Int, Int))](./intortriple/init%28_%29-7f0c9.md)
- [init(arrayLiteral: Int...)](./intortriple/init%28arrayliteral%29.md)
- [init(integerLiteral: Int)](./intortriple/init%28integerliteral%29.md)
### Instance Properties
- [var first: Int](./intortriple/first.md)
- [var second: Int](./intortriple/second.md)
- [var third: Int](./intortriple/third.md)
- [let values: (Int, Int, Int)](./intortriple/values.md)

## Relationships

### Conforms To
- Swift.ExpressibleByArrayLiteral
- Swift.ExpressibleByIntegerLiteral
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Parameter Types
- [struct IntOrPair](./intorpair.md)
  Parameter for convolutions allowing single integers or tuples.
- [enum IntOrArray](./intorarray.md)
  Parameter for convolutions allowing single integers or arrays.
- [enum FloatOrArray](./floatorarray.md)
  Parameter for taking a single or multiple Float values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/intortriple)*