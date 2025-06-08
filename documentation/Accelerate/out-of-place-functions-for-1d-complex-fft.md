# Out-of-Place Functions for 1D Complex FFT

**Framework**: Accelerate

Perform fast Fourier transforms out of place on 1D complex data.

#### Overview

The functions in this group use the following operation for a complex-to-complex transform:

```c
N = 1 << Log2N;

scale = 0 < Direction ? 1 : 1./N;

// Define a complex vector, h:
for (j = 0; j < N; ++j)
    h[j] = A->realp[j*IA] + i * A->imagp[j*IA];

// Perform Discrete Fourier Transform.
for (k = 0; k < N; ++k)
    H[k] = scale * sum(h[j] * e**(-Direction*2*pi*i*j*k/N), 0 <= j < N);

// Store result.
for (k = 0; k < N; ++k)
{
    C->realp[k*IC] = Re(H[k]);
    C->imagp[k*IC] = Im(H[k]);
}

```

The temporary buffer versions perform the same operation but use a temporary buffer for improved performance.

## Topics

### Out-of-Place FFT Functions
- [vDSP_fft_zop](vdsp_fft_zop.md)
  Computes a forward or inverse out-of-place, single-precision complex FFT.
- [vDSP_fft_zopD](vdsp_fft_zopd.md)
  Computes a forward or inverse out-of-place, double-precision complex FFT.
### Out-of-Place FFT Functions with Temporary Buffer
- [vDSP_fft_zopt](vdsp_fft_zopt.md)
  Computes a forward or inverse out-of-place, single-precision complex FFT using a temporary buffer.
- [vDSP_fft_zoptD](vdsp_fft_zoptd.md)
  Computes a forward or inverse out-of-place, double-precision complex FFT using a temporary buffer.
### Fixed-Length FFT Functions
- [vDSP_FFT16_copv](vdsp_fft16_copv.md)
  Performs a 16-element FFT on interleaved-complex data.
- [vDSP_FFT32_copv](vdsp_fft32_copv.md)
  Performs a 32-element FFT on interleaved-complex data.
- [vDSP_FFT16_zopv](vdsp_fft16_zopv.md)
  Performs a 16-element FFT on split-complex data.
- [vDSP_FFT32_zopv](vdsp_fft32_zopv.md)
  Performs a 32-element FFT on split-complex data.
### Radix 3 and Radix 5 FFT Functions
- [vDSP_fft3_zop](vdsp_fft3_zop.md)
  Computes a single-precision out-of-place radix-3 complex FFT, either forward or inverse.
- [vDSP_fft3_zopD](vdsp_fft3_zopd.md)
  Computes a double-precision out-of-place radix-3 complex FFT, either forward or inverse.
- [vDSP_fft5_zop](vdsp_fft5_zop.md)
  Computes a single-precision out-of-place radix-5 complex FFT, either forward or inverse.
- [vDSP_fft5_zopD](vdsp_fft5_zopd.md)
  Computes a double-precision out-of-place radix-5 complex FFT, either forward or inverse.

## See Also

- [In-Place Functions for 1D Complex FFT](in-place-functions-for-1d-complex-fft.md)
  Perform fast Fourier transforms in place on 1D complex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/out-of-place-functions-for-1d-complex-fft)*