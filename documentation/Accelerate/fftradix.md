# FFTRadix

**Framework**: Accelerate  
**Kind**: typealias

The radix of the FFT decomposition.

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
typealias FFTRadix = Int32
```

#### Discussion

Pass an `FFTRadix` value as an argument to [`vDSP_create_fftsetup`](https://developer.apple.com/documentation/kernel/1580009-vdsp_create_fftsetup) or [`vDSP_create_fftsetupD`](vdsp_create_fftsetupd.md).

## See Also

- [typealias FFTSetup](fftsetup.md)
  An opaque type that contains setup information for a single-precision FFT transform.
- [typealias FFTSetupD](fftsetupd.md)
  An opaque type that contains setup information for a double-precision FFT transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/fftradix)*