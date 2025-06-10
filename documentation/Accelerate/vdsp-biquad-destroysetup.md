# vDSP_biquad_DestroySetup

**Framework**: Accelerate  
**Kind**: func

Destroys a single-precision biquadratic filter setup object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_biquad_DestroySetup(vDSP_biquad_Setup __setup);
```

#### Discussion

This function frees all resources associated with a `vDSP_biquad_Setup` object previously created through a call to [`vDSP_biquad_CreateSetup`](vdsp_biquad_createsetup.md).

## Parameters

- `__setup`: The object to be destroyed; a setup created by  .

## See Also

- [vDSP_biquad_DestroySetupD](vdsp_biquad_destroysetupd.md)
  Destroys a double-precision biquadratic filter setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquad_destroysetup)*