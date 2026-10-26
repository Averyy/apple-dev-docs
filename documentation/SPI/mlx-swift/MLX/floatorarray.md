---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/floatorarray"
framework: "mlx-swift/MLX"
---

# FloatOrArray

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Parameter for taking a single or multiple Float values.

## Declaration

```swift
enum FloatOrArray
```

#### Overview

For example the numeric parameters here are all [`FloatOrArray`](./floatorarray.md):

```swift
Upsample(scaleFactor: 10.5)
Upsample(scaleFactor: [4.5, 3.5])
```

##### See Also:

- [`IntOrArray`](./intorarray.md)

## Topics

### Enumeration Cases
- [FloatOrArray.array(_:)](./floatorarray/array%28_%29.md)
- [FloatOrArray.float(_:)](./floatorarray/float%28_%29.md)
### Initializers
- [init(Float)](./floatorarray/init%28_%29-6jpxa.md)
- [init([Float])](./floatorarray/init%28_%29-85l5q.md)
- [init(arrayLiteral: Float...)](./floatorarray/init%28arrayliteral%29.md)
- [init(floatLiteral: Float)](./floatorarray/init%28floatliteral%29.md)
### Instance Properties
- [var asArray: [Float]](./floatorarray/asarray.md)
- [var count: Int](./floatorarray/count.md)
### Instance Methods
- [func asArray(dimensions: Int) -> [Float]](./floatorarray/asarray%28dimensions%29.md)

## Relationships

### Conforms To
- Swift.ExpressibleByArrayLiteral
- Swift.ExpressibleByFloatLiteral
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Parameter Types
- [struct IntOrPair](./intorpair.md)
  Parameter for convolutions allowing single integers or tuples.
- [struct IntOrTriple](./intortriple.md)
  Parameter for convolutions allowing single integers or triples.
- [enum IntOrArray](./intorarray.md)
  Parameter for convolutions allowing single integers or arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/floatorarray)*