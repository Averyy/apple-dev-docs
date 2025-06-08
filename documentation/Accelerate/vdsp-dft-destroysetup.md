# vDSP_DFT_DestroySetup

**Framework**: Accelerate  
**Kind**: func

Releases a single-precision setup structure.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
void vDSP_DFT_DestroySetup(vDSP_DFT_Setup __Setup);
```

#### Discussion

Destroying a setup with shared data is safe; this function only releases memory that’s not needed by other undestroyed setups.

> **Note**:  This function isn’t fully thread-safe. You must not call this function concurrently with any function that uses the setup structure or any other setup structure that shares its underlying storage.

## Parameters

- `__Setup`: The setup structure to destroy.

## See Also

- [vDSP_DFT_DestroySetupD](vdsp_dft_destroysetupd.md)
  Releases a double-precision setup structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_destroysetup)*