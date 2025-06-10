# SparseGetStateSize_Float(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the size in bytes necessary for a call to the single-precision sparse iterate method.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseGetStateSize_Float(_ method: SparseIterativeMethod, _ preconditioner: Bool, _ m: Int32, _ n: Int32, _ nrhs: Int32) -> Int
```

#### Return Value

The size of the required state space, in bytes.

## Parameters

- `method`: The method to return required state space size for.
- `preconditioner`: Set to   if your subsequent calls to   use a preconditioner.
- `m`: The number of rows in matrix  .
- `n`: The number of columns in matrix  .
- `nrhs`: The number of columns in matrices   and  .

## See Also

- [func SparseGetStateSize_Double(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_double(_:_:_:_:_:).md)
  Returns the size in bytes necessary for a call to the double-precision sparse iterate method.
- [func SparseGetStateSize_Complex_Double(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_complex_double(_:_:_:_:_:).md)
  Returns size in bytes of state space required for call to `SparseIterate()` for complex double values.
- [func SparseGetStateSize_Complex_Float(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_complex_float(_:_:_:_:_:).md)
  Returns size in bytes of state space required for call to `SparseIterate()` for complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegetstatesize_float(_:_:_:_:_:))*