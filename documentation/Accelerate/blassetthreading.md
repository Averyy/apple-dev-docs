# BLASSetThreading(_:)

**Framework**: Accelerate  
**Kind**: func

Sets the BLAS and LAPACK threading model.

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
func BLASSetThreading(_ threading: BLAS_THREADING) -> Int32
```

#### Return Value

`0` on success or `-1` if the current platform doesn’t support the threading model.

#### Discussion

This function sets the threading model for subsequent calls into BLAS and LAPACK.

This setting is per thread, and Accelerate saves it in a thread-local variable.

## Parameters

- `threading`: A constant that specifies the threading model.

## See Also

- [struct BLAS](blas.md)
  An enumeration that acts as a namespace for Swift overlays to BLAS.
- [func BLASGetThreading() -> BLAS_THREADING](blasgetthreading().md)
  Returns the current BLAS and LAPACK threading model.
- [struct BLAS_THREADING](blas_threading.md)
  Constants that describe the BLAS and LAPACK threading model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blassetthreading(_:))*