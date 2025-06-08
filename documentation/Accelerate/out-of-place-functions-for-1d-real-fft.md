# Out-of-Place Functions for 1D Real FFT

**Framework**: Accelerate

Perform fast Fourier transforms out of place on 1D real data.

#### Overview

The functions in this group use the following operation for a forward real-to-complex transform:

```c
N = 1 << Log2N;

scale = 2;

// Define a real vector, h:
for (j = 0; j < N/2; ++j)
{
    h[2*j + 0] = A->realp[j*IA];
    h[2*j + 1] = A->imagp[j*IA];
}

// Perform Discrete Fourier Transform.
for (k = 0; k < N; ++k)
    H[k] = scale *
        sum(h[j] * e**(-Direction*2*pi*i*j*k/N), 0 <= j < N);

// Pack DC and Nyquist components into C->realp[0] and C->imagp[0].
C->realp[0*IC] = Re(H[ 0 ]).
C->imagp[0*IC] = Re(H[N/2]).

// Store regular components:
for (k = 1; k < N/2; ++k)
{
    C->realp[k*IC] = Re(H[k]);
    C->imagp[k*IC] = Im(H[k]);
}

```

The functions in this group use the following operation for an inverse complex-to-real transform:

```c
N = 1 << Log2N;

scale = 1./N;

// Define a complex vector, h:
h[ 0 ] = A->realp[0*IA];
h[N/2] = A->imagp[0*IA];
for (j = 1; j < N/2; ++j)
{
    h[ j ] = A->realp[j*IA] + i * A->imagp[j*IA];
    h[N-j] = conj(h[j]);
}

// Perform Discrete Fourier Transform.
for (k = 0; k < N; ++k)
    H[k] = scale *
        sum(h[j] * e**(-Direction*2*pi*i*j*k/N), 0 <= j < N);

// Coerce real results into complex structure:
for (k = 0; k < N/2; ++k)
{
    C->realp[k*IC] = H[2*k+0];
    C->imagp[k*IC] = H[2*k+1];
}

```

The temporary buffer versions perform the same operation but use a temporary buffer for improved performance.

## Topics

### Out-of-Place FFT Functions
- [vDSP_fft_zrop](vdsp_fft_zrop.md)
  Computes a forward or inverse out-of-place, single-precision real FFT.
- [vDSP_fft_zropD](vdsp_fft_zropd.md)
  Computes a forward or inverse out-of-place, double-precision real FFT.
### Out-of-Place FFT Functions with Temporary Buffer
- [vDSP_fft_zropt](vdsp_fft_zropt.md)
  Computes a forward or inverse out-of-place, single-precision real FFT using a temporary buffer.
- [vDSP_fft_zroptD](vdsp_fft_zroptd.md)
  Computes a forward or inverse out-of-place, double-precision real FFT using a temporary buffer.

## See Also

- [In-Place Functions for 1D Real FFT](in-place-functions-for-1d-real-fft.md)
  Perform fast Fourier transforms in place on 1D real data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/out-of-place-functions-for-1d-real-fft)*