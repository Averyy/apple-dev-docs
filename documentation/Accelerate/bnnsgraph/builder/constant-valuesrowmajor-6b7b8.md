# constant(values:rowMajor:)

**Framework**: Accelerate  
**Kind**: method

Returns a rank 2 tensor from an array of arrays.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func constant(values: Array<Array<Float>>, rowMajor: Bool = false) -> BNNSGraph.Builder.Tensor<Float>
```

#### Discussion

> **Note**: Each sub-array must contain the same number of elements.

The following code shows how to use this function to multiply two 2x2 matrices:

```None
   let xValues = [[1, 2],
                  [3, 4]] as [[Float]]
   let yValues = [[5, 6],
                  [7, 8]] as [[Float]]

   let context = try BNNSGraph.makeContext {
       builder in

       let x = builder.constant(values: xValues)
       let y = builder.constant(values: yValues)

       let z = x.matmul(other: y)

       return [z] // On return, `z` equals `[19.0, 22.0, 43.0, 50.0]`.
   }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/constant(values:rowmajor:)-6b7b8)*