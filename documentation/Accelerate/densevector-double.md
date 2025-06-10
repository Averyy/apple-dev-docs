# DenseVector_Double

**Framework**: Accelerate  
**Kind**: struct

A structure that contains a dense vector of double-precision, floating-point values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct DenseVector_Double
```

## Mentions

- [Solving systems using direct methods](solving-systems-using-direct-methods.md)
- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)

#### Overview

You typically use dense vectors to represent the unknowns vector, , and the right-hand-side vector, , in the matrix equation  A [`DenseVector_Double`](densevector_double.md) structure provides a pointer to its underlying data and a count of its number of elements.

The following code shows an example of how to create a dense vector structure from an array of double-precision values. In this case, use [`withUnsafeMutableBufferPointer(_:)`](acceleratemutablebuffer/withunsafemutablebufferpointer(_:).md) to pass a pointer to your collection. The [`DenseVector_Double`](densevector_double.md) structure is valid only during the execution of the closure. Don’t store or return the structure for later use.

```swift
var vectorValues: [Double] = [10, 20, 30, 40]
let vectorValuesCount = Int32(vectorValues.count)

vectorValues.withUnsafeMutableBufferPointer { vectorValuesPtr in
    
    let vector = DenseVector_Double(count: vectorValuesCount,
                                    data: vectorValuesPtr.baseAddress!)
    
    // Perform operations using `vector`.
}
```

## Topics

### Initializers
- [init(count: Int32, data: UnsafeMutablePointer<Double>)](densevector_double/init(count:data:).md)
  Creates a new vector of double-precision values.
### Inspecting a Vector’s Structure and Data
- [var count: Int32](densevector_double/count.md)
  The number of items in the vector.
- [var data: UnsafeMutablePointer<Double>](densevector_double/data.md)
  The array of double-precision, floating-point values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct DenseMatrix_Double](densematrix_double.md)
  A structure that contains a dense matrix of double-precision, floating-point values.
- [struct DenseMatrix_Float](densematrix_float.md)
  A structure that contains a dense matrix of single-precision, floating-point values.
- [struct DenseVector_Float](densevector_float.md)
  A structure that contains a dense vector of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/densevector_double)*