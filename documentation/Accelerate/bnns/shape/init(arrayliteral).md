# init(arrayLiteral:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new shape with the specified size.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
init(arrayLiteral: BNNS.Shape.ArrayLiteralElement...)
```

## Discussion

This initializer returns a shape with the default layout for the rank that’s equal to the count of `arrayLiteral`. The default layouts for each dimensionality are:

- **1D**: [`BNNS.DataLayout.vector`](../datalayout/vector.md)
- **2D**: [`BNNS.DataLayout.matrixFirstMajor`](../datalayout/matrixfirstmajor.md)
- **3D**: [`BNNS.DataLayout.tensor3DFirstMajor`](../datalayout/tensor3dfirstmajor.md)
- **4D**: [`BNNS.DataLayout.tensor4DFirstMajor`](../datalayout/tensor4dfirstmajor.md)
- **5D**: [`BNNS.DataLayout.tensor5DFirstMajor`](../datalayout/tensor5dfirstmajor.md)
- **6D**: [`BNNS.DataLayout.tensor6DFirstMajor`](../datalayout/tensor6dfirstmajor.md)
- **7D**: [`BNNS.DataLayout.tensor7DFirstMajor`](../datalayout/tensor7dfirstmajor.md)
- **8D**: [`BNNS.DataLayout.tensor8DFirstMajor`](../datalayout/tensor8dfirstmajor.md)

## Parameters

- `arrayLiteral`: An array that specifies the number of values in each dimension.

## See Also

### Creating a Shape
- [init([Int], dataLayout: BNNS.DataLayout?, stride: [Int]?)](./init%28_,datalayout,stride%29.md)
  Returns a new shape with the specified size, data layout, and stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/shape/init(arrayliteral:))*