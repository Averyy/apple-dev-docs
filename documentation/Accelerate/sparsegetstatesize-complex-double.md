# SparseGetStateSize_Complex_Double(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns size in bytes of state space required for call to `SparseIterate()` for complex double values.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseGetStateSize_Complex_Double(_ method: SparseIterativeMethod, _ preconditioner: Bool, _ m: Int32, _ n: Int32, _ nrhs: Int32) -> Int
```

#### Return Value

Size of state space required in bytes.

## Parameters

- `method`: (Input) Method to return required state space size for.
- `preconditioner`: (Input) True if a preconditioner will be supplied,   false otherwise.
- `m`: (Input) Number of entries in right-hand side (rows in matrix  ).
- `n`: (Input) Number of variables to solve for (columns in matrix  ).
- `nrhs`: (Input) Number of right-hand sides to be solved for.

## See Also

- [func SparseGetStateSize_Double(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_double(_:_:_:_:_:).md)
  Returns the size in bytes necessary for a call to the double-precision sparse iterate method.
- [func SparseGetStateSize_Float(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_float(_:_:_:_:_:).md)
  Returns the size in bytes necessary for a call to the single-precision sparse iterate method.
- [func SparseGetStateSize_Complex_Float(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_complex_float(_:_:_:_:_:).md)
  Returns size in bytes of state space required for call to `SparseIterate()` for complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegetstatesize_complex_double(_:_:_:_:_:))*