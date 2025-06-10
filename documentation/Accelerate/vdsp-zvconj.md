# vDSP_zvconj

**Framework**: Accelerate  
**Kind**: func

Calculates the complex conjugate of the values in a single-precision vector using the specified stride.

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
extern void vDSP_zvconj(const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Conjugates elements of vector `A`, leaving results in `C`.

![mathematical formula](https://docs-assets.developer.apple.com/published/b5c598a2773138a40a69df93621b0776/media-2557733%402x.png)

## Parameters

- `__A`: Single-precision complex input vector
- `__IA`: Stride for 
- `__C`: Single-precision complex output vector
- `__IC`: Stride for 
- `__N`: The number of elements to process

## See Also

- [vDSP_zvconjD](vdsp_zvconjd.md)
  Calculates the complex conjugate of the values in a double-precision vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvconj)*