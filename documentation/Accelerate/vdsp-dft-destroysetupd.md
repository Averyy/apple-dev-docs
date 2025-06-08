# vDSP_DFT_DestroySetupD

**Framework**: Accelerate  
**Kind**: func

Releases a double-precision setup structure.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
void vDSP_DFT_DestroySetupD(vDSP_DFT_SetupD __Setup);
```

#### Discussion

Destroying a setup with shared data is safe; this function only releases memory that’s not needed by other undestroyed setups.

> **Note**:  This function isn’t fully thread-safe. You must not call this function concurrently with any function that uses the setup structure or any other setup structure that shares its underlying storage.

## Parameters

- `__Setup`: The setup structure to destroy.

## See Also

- [vDSP_DFT_DestroySetup](vdsp_dft_destroysetup.md)
  Releases a single-precision setup structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_destroysetupd)*