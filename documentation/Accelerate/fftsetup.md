# FFTSetup

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

An opaque type that contains setup information for a single-precision FFT transform.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias FFTSetup = OpaquePointer
```

```c
typedef struct OpaqueFFTSetup * FFTSetup;
```

#### Discussion

Call the [`vDSP_create_fftsetup`](../kernel/api-1580009-vdsp_create_fftsetup.md) function to create a setup structure, and calll [`vDSP_destroy_fftsetup`](../kernel/api-1579978-vdsp_destroy_fftsetup.md) to deallocate a setup structure.

## See Also

### FFT Setup
- [typealias FFTSetupD](./fftsetupd.md)
  An opaque type that contains setup information for a double-precision FFT transform.
- [typealias FFTRadix](./fftradix.md)
  The radix of the FFT decomposition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/fftsetup)*