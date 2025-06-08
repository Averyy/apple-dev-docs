# FFTSetupD

**Framework**: Accelerate  
**Kind**: typealias

An opaque type that contains setup information for a double-precision FFT transform.

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
typealias FFTSetupD = OpaquePointer
```

#### Discussion

Call the [`vDSP_create_fftsetupD`](vdsp_create_fftsetupd.md) function to create a setup structure, and calll [`vDSP_destroy_fftsetupD`](vdsp_destroy_fftsetupd.md) to deallocate a setup structure.

## See Also

- [typealias FFTSetup](fftsetup.md)
  An opaque type that contains setup information for a single-precision FFT transform.
- [typealias FFTRadix](fftradix.md)
  The radix of the FFT decomposition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/fftsetupd)*