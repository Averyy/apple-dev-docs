# vDSP_DFT_Interleaved_Setup

**Framework**: Accelerate  
**Kind**: typealias

An opaque type that contains setup information for an interleaved single-precision discrete Fourier transform (DFT).

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
typealias vDSP_DFT_Interleaved_Setup = OpaquePointer
```

#### Discussion

Call the [`vDSP_DFT_Interleaved_CreateSetup(_:_:_:_:)`](vdsp_dft_interleaved_createsetup(_:_:_:_:).md) function to initialize and allocate a new setup object. Call [`vDSP_DFT_Interleaved_DestroySetup(_:)`](vdsp_dft_interleaved_destroysetup(_:).md) to free the resources associated with a setup object.

## See Also

- [typealias vDSP_DFT_Interleaved_SetupD](vdsp_dft_interleaved_setupd.md)
  An opaque type that contains setup information for an interleaved double-precision discrete Fourier transform (DFT).
- [typealias vDSP_DFT_Setup](vdsp_dft_setup.md)
  An opaque type that contains setup information for a single-precision discrete Fourier transform (DFT).
- [typealias vDSP_DFT_SetupD](vdsp_dft_setupd.md)
  An opaque type that contains setup information for a double-precision discrete Fourier transform (DFT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_interleaved_setup)*