# vDSP_vfrac

**Framework**: Accelerate  
**Kind**: func

Truncates the elements of a single-precision vector to fractions.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vfrac(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Performs the following operation:

![mathematical formula](https://docs-assets.developer.apple.com/published/14a99da22cbc363d1a460e38c918a74b/media-2557732%402x.png)

The “function” truncate(x) is the integer farthest from 0 but not farther than x. Thus, for example, `vDSP_vFrac(-3.25)` produces the result -0.25.

Sets each element of vector `C` to the signed fractional part of the corresponding element of `A`.

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for 
- `__C`: Single-precision real output vector
- `__IC`: Stride for 
- `__N`: The number of elements to process

## See Also

- [vDSP_vfracD](vdsp_vfracd.md)
  Truncates the elements of a double-precision vector to fractions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfrac)*