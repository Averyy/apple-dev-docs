# SparseGetInertia(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the inertia of an LDLT factorization in complex float.

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
func SparseGetInertia(_ Factored: SparseOpaqueFactorization_Complex_Float, _ num_positive: UnsafeMutablePointer<Int32>, _ num_zero: UnsafeMutablePointer<Int32>, _ num_negative: UnsafeMutablePointer<Int32>) -> Int32
```

#### Return Value

0 on success, non-zero on error

#### Discussion

For a given LDLT factorization, this function returns the number of negative, zero and positive pivots taken during the factorization. Note that in some cases, particularly when eigenvalues are close to zero, the computed numerical inertia may not be an accurate reflection of the true inertia of the system, and in particular can be highly dependent on the zeroTolerance (and to a less degree the pivotTolerance) specified in the factorization options.

This call is only supported for factorizations of type `SparseFactorizationLDLTTPP`.

## Parameters

- `Factored`: The factorization to be queried.
- `num_positive`: Upon return   has been set to the number   of positive pivots.
- `num_zero`: Upon return   has been set to the number   of zero pivots.
- `num_negative`: Upon return   has been set to the number   of negative pivots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegetinertia(_:_:_:_:)-6ca5h)*