# BLAS

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

An enumeration that acts as a namespace for Swift overlays to BLAS.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS 15.0+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BLAS
```

#### Overview

The [`BLAS`](./blas.md) enumeration provides methods and structures that offer a Swift-friendly API for Basic Linear Algebra Subprograms (BLAS) and Linear Algebra PACKage (LAPACK) operations.

## Topics

### Setting the BLAS and LAPACK threading model
- [static var threadingModel: BLAS.ThreadingModel](./blas/threadingmodel-swift.type.property.md)
  The BLAS and LAPACK threading model.
- [struct ThreadingModel](./blas/threadingmodel-swift.struct.md)
  Constants that describe the BLAS and LAPACK threading model.

## See Also

### Specifying the threading model
- [func BLASSetThreading(BLAS_THREADING) -> Int32](./blassetthreading%28_%29.md)
  Sets the BLAS and LAPACK threading model.
- [func BLASGetThreading() -> BLAS_THREADING](./blasgetthreading%28%29.md)
  Returns the current BLAS and LAPACK threading model.
- [struct BLAS_THREADING](./blas_threading.md)
  Constants that describe the BLAS and LAPACK threading model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blas)*