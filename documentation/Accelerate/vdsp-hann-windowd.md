# vDSP_hann_windowD

**Framework**: Accelerate  
**Kind**: func

Creates a double-precision Hann window.

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
extern void vDSP_hann_windowD(double * __C, vDSP_Length __N, int __Flag);
```

#### Discussion

The [`vDSP_hann_window`](vdsp_hann_window.md) and [`vDSP_hann_windowD`](vdsp_hann_windowd.md) functions create a Hann window vector using the following operation:

```swift
If Flag & vDSP_HALF_WINDOW:
    Length = (N+1)/2;
Else
    Length = N;

If Flag & vDSP_HANN_NORM:
    W = .8165;
Else
    W = .5;

for (n = 0; n < Length; ++n)
    C[n] = W * (1 - cos(2*pi*n/N));
```

Use [`vDSP_vmulD`](vdsp_vmuld.md) to multiply the Hann window result by a noninteger-periodic signal prior to a Fourier transform.

The following code shows how to generate a Hann window:

```swift
let n = vDSP_Length(1024)
var c = [Double](repeating: 0,
                 count: Int(n))

vDSP_hann_windowD(&c,
                  n,
                  Int32(vDSP_HANN_DENORM))
```

The following illustrates the values of the output vector, `c`:

![Visualization of a Hann window.](https://docs-assets.developer.apple.com/published/e79c7c67e6b7c717006b927e62cd2c88/media-3368167%402x.png)

## Parameters

- `__C`: The output vector.
- `__N`: The number of elements in the output vector.
- `__Flag`: A value that specifies the type of window that the function creates.

## See Also

- [vDSP_blkman_window](vdsp_blkman_window.md)
  Creates a single-precision Blackman window.
- [vDSP_blkman_windowD](vdsp_blkman_windowd.md)
  Creates a double-precision Blackman window.
- [vDSP_hamm_window](vdsp_hamm_window.md)
  Creates a single-precision Hamming window.
- [vDSP_hamm_windowD](vdsp_hamm_windowd.md)
  Creates a double-precision Hamming window.
- [vDSP_hann_window](vdsp_hann_window.md)
  Creates a single-precision Hann window.
- [var vDSP_HALF_WINDOW: Int](vdsp_half_window.md)
  Specifies that the window should only contain the bottom half of the values (`0` to `(N+1)/2`).
- [var vDSP_HANN_DENORM: Int](vdsp_hann_denorm.md)
  Specifies a denormalized Hann window.
- [var vDSP_HANN_NORM: Int](vdsp_hann_norm.md)
  Specifies a normalized Hann window


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_hann_windowd)*