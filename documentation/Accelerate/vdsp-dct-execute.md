# vDSP_DCT_Execute

**Framework**: Accelerate  
**Kind**: func

Calculates the discrete cosine transform for a vector.

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
void vDSP_DCT_Execute(const struct vDSP_DFT_SetupStruct * __Setup, const float * __Input, float * __Output);
```

#### Discussion

In-place operation is supported.

## Parameters

- `__Setup`: A DCT setup object returned by a call to 
- `__Input`: Single-precision input vector that contains the number of elements specified in the setup structure.
- `__Output`: Single-precision output vector that contains the number of elements specified in the setup structure.

## See Also

- [vDSP_DCT_CreateSetup](vdsp_dct_createsetup.md)
  Builds a data structure that contains precalculated data to perform a discrete cosine transform.
- [enum vDSP_DCT_Type](vdsp_dct_type.md)
  Constants that indicate the type for a discrete cosine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dct_execute)*