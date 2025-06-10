# BLAS.ThreadingModel

**Framework**: Accelerate  
**Kind**: struct

Constants that describe the BLAS and LAPACK threading model.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct ThreadingModel
```

#### Overview

Use the threading model constants to specify whether BLAS and LAPACK operations run in a single thread or multiple threads. Specify the single-threaded model if your app uses its own threading mechanism.

## Topics

### Specifying a threading model
- [static let multiThreaded: BLAS.ThreadingModel](blas/threadingmodel-swift.struct/multithreaded.md)
  A constant that specifies that the Accelerate framework decides whether BLAS and LAPACK execute on single or multiple threads.
- [static let singleThreaded: BLAS.ThreadingModel](blas/threadingmodel-swift.struct/singlethreaded.md)
  A constant that specifies BLAS and LAPACK execute on a single thread only.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [static var threadingModel: BLAS.ThreadingModel](blas/threadingmodel-swift.type.property.md)
  The BLAS and LAPACK threading model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blas/threadingmodel-swift.struct)*