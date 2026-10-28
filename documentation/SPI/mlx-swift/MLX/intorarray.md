---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/intorarray"
framework: "mlx-swift/MLX"
---

# IntOrArray

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Parameter for convolutions allowing single integers or arrays.

## Declaration

```swift
enum IntOrArray
```

## Overview

For example the numeric parameters here are all [`IntOrArray`](./intorarray.md):

```swift
convGeneral(input, weights, strides: 3, padding: [2, 2, 1, 0, 0], ...)
```

### See Also:

- [`IntOrPair`](./intorpair.md)
- [`FloatOrArray`](./floatorarray.md)

## Topics

### Enumeration Cases
- [IntOrArray.array(_:)](./intorarray/array%28_%29.md)
- [IntOrArray.int(_:)](./intorarray/int%28_%29.md)
### Initializers
- [init(Int)](./intorarray/init%28_%29-2osb4.md)
- [init([Int])](./intorarray/init%28_%29-6u5zd.md)
- [init(arrayLiteral: Int...)](./intorarray/init%28arrayliteral%29.md)
- [init(integerLiteral: Int)](./intorarray/init%28integerliteral%29.md)
### Instance Properties
- [var asArray: [Int]](./intorarray/asarray.md)
- [var asInt32Array: [Int32]](./intorarray/asint32array.md)
- [var count: Int](./intorarray/count.md)

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
- [struct IntOrTriple](./intortriple.md)
  Parameter for convolutions allowing single integers or triples.
- [enum FloatOrArray](./floatorarray.md)
  Parameter for taking a single or multiple Float values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/intorarray)*