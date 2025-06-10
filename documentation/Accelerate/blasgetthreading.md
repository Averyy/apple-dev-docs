# BLASGetThreading()

**Framework**: Accelerate  
**Kind**: func

Returns the current BLAS and LAPACK threading model.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func BLASGetThreading() -> BLAS_THREADING
```

#### Return Value

A constant that represents the current BLAS and LAPACK threading model.

## See Also

- [struct BLAS](blas.md)
  An enumeration that acts as a namespace for Swift overlays to BLAS.
- [func BLASSetThreading(BLAS_THREADING) -> Int32](blassetthreading(_:).md)
  Sets the BLAS and LAPACK threading model.
- [struct BLAS_THREADING](blas_threading.md)
  Constants that describe the BLAS and LAPACK threading model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blasgetthreading())*