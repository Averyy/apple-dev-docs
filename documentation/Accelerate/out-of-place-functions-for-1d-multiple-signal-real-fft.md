# Out-of-Place Functions for 1D Multiple-Signal Real FFT

**Framework**: Accelerate

Perform fast Fourier transforms out of place on multiple-signal 1D real data.

#### Overview

The functions in this group use the following operation for a forward real-to-complex transform:

```c
N = 1 << Log2N;

// Repeat M times:
for (m = 0; m < M; ++m)
{
     scale = 2;

     // Define a real vector, h:
     for (j = 0; j < N/2; ++j)
     {
         h[2*j + 0] = A->realp[m*IMA + j*IA];
         h[2*j + 1] = A->imagp[m*IMA + j*IA];
     }

     // Perform Discrete Fourier Transform.
     for (k = 0; k < N; ++k)
         H[k] = scale *
             sum(h[j] * e**(-Direction*2*pi*i*j*k/N), 0 <= j < N);

     // Pack DC and Nyquist components into initial elements.
     C->realp[m*IMC + 0*IC] = Re(H[ 0 ]).
     C->imagp[m*IMC + 0*IC] = Re(H[N/2]).

     // Store regular components:
     for (k = 1; k < N/2; ++k)
     {
         C->realp[m*IMC + k*IC] = Re(H[k]);
         C->imagp[m*IMC + k*IC] = Im(H[k]);
     }
}

```

The functions in this group use the following operation for an inverse complex-to-real transform:

```c
N = 1 << Log2N;

scale = 1./N;

// Repeat M times:
for (m = 0; m < M; ++m)
{

    // Define a complex vector, h:
    h[ 0 ] = A->realp[m*IMA + 0*IA];
    h[N/2] = A->imagp[m*IMA + 0*IA];
    for (j = 1; j < N/2; ++j)
    {
        h[ j ] = A->realp[m*IMA + j*IA]
           + i * A->imagp[m*IMA + j*IA];
        h[N-j] = conj(h[j]);
    }

    // Perform Discrete Fourier Transform.
    for (k = 0; k < N; ++k)
        H[k] = scale *
            sum(h[j] * e**(-Direction*2*pi*i*j*k/N), 0 <= j < N);

    // Coerce real results into complex structure:
    for (k = 0; k < N/2; ++k)
    {
        C->realp[m*IMC + k*IC] = H[2*k+0];
        C->imagp[m*IMC + k*IC] = H[2*k+1];
    }
}


```

The temporary buffer versions perform the same operation but use a temporary buffer for improved performance.

## Topics

### Out-of-Place FFT Functions
- [vDSP_fftm_zrop](vdsp_fftm_zrop.md)
  Computes a forward or inverse out-of-place, single-precision real FFT on multiple signals.
- [vDSP_fftm_zropD](vdsp_fftm_zropd.md)
  Computes a forward or inverse out-of-place, double-precision real FFT on multiple signals.
### Out-of-Place FFT Functions with Temporary Buffer
- [vDSP_fftm_zropt](vdsp_fftm_zropt.md)
  Computes a forward or inverse out-of-place, single-precision real FFT on multiple signals using a temporary buffer.
- [vDSP_fftm_zroptD](vdsp_fftm_zroptd.md)
  Computes a forward or inverse out-of-place, double-precision real FFT on multiple signals using a temporary buffer.

## See Also

- [In-Place Functions for 1D Multiple-Signal Real FFT](in-place-functions-for-1d-multiple-signal-real-fft.md)
  Perform fast Fourier transforms in place on multiple-signal 1D real data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/out-of-place-functions-for-1d-multiple-signal-real-fft)*