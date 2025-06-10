# BLAS_THREADING

**Framework**: Accelerate  
**Kind**: struct

Constants that describe the BLAS and LAPACK threading model.

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
struct BLAS_THREADING
```

#### Overview

Use the threading model constants to specify whether BLAS and LAPACK operations run in a single thread or multiple threads. Specify the single-threaded model if your app uses its own threading mechanism.

## Topics

### Specifying a threading model
- [init(UInt32)](blas_threading/init(_:).md)
  Creates a threading model constant.
- [init(rawValue: UInt32)](blas_threading/init(rawvalue:).md)
  Creates a threading model constant with an unsigned-integer value.
- [var rawValue: UInt32](blas_threading/rawvalue.md)
  The raw value that represents the threading model.
- [var BLAS_THREADING_MULTI_THREADED: BLAS_THREADING](blas_threading_multi_threaded.md)
  A constant that specifies that the Accelerate framework decides whether BLAS and LAPACK execute on single or multiple threads.
- [var BLAS_THREADING_SINGLE_THREADED: BLAS_THREADING](blas_threading_single_threaded.md)
  A constant that specifies BLAS and LAPACK execute on a single thread only.
- [var BLAS_THREADING_MAX_OPTIONS: BLAS_THREADING](blas_threading_max_options.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct BLAS](blas.md)
  An enumeration that acts as a namespace for Swift overlays to BLAS.
- [func BLASSetThreading(BLAS_THREADING) -> Int32](blassetthreading(_:).md)
  Sets the BLAS and LAPACK threading model.
- [func BLASGetThreading() -> BLAS_THREADING](blasgetthreading().md)
  Returns the current BLAS and LAPACK threading model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blas_threading)*