# init(_:)

**Framework**: Accelerate  
**Kind**: init

Creates a threading model constant.

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
init(_ rawValue: UInt32)
```

## Parameters

- `rawValue`: A raw unsigned-integer value.

## See Also

- [init(rawValue: UInt32)](blas_threading/init(rawvalue:).md)
  Creates a threading model constant with an unsigned-integer value.
- [var rawValue: UInt32](blas_threading/rawvalue.md)
  The raw value that represents the threading model.
- [var BLAS_THREADING_MULTI_THREADED: BLAS_THREADING](blas_threading_multi_threaded.md)
  A constant that specifies that the Accelerate framework decides whether BLAS and LAPACK execute on single or multiple threads.
- [var BLAS_THREADING_SINGLE_THREADED: BLAS_THREADING](blas_threading_single_threaded.md)
  A constant that specifies BLAS and LAPACK execute on a single thread only.
- [var BLAS_THREADING_MAX_OPTIONS: BLAS_THREADING](blas_threading_max_options.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blas_threading/init(_:))*