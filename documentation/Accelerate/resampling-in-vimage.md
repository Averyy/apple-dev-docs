# Resampling in vImage

**Framework**: Accelerate

Learn how vImage resamples image data during geometric operations.

#### Overview

Most vImage geometric functions use resampling kernels, which combine data from a target pixel and other nearby pixels to calculate a value for the destination pixel. Resampling image data reduces unwanted artifacts, like interference patterns, in the destination image.

This procedure is somewhat similar to that used for convolution. However—in contrast to convolution—for geometric operations, the resampling kernel itself is resampled during the process of pairing kernel values against the sampled pixel data. The kernel is evaluated at both fractional and integral pixel locations. This has implications for the nature of the kernel—which must be supplied as a function rather than as a matrix. A resampling kernel function is also called a resampling filter, or simply a filter.

For almost all geometric operations, vImage supplies a default resampling filter unless you set the flag [`kvImageHighQualityResampling`](kvimagehighqualityresampling.md), in which case vImage uses a higher-quality filter. However, the performance of that filter may be slower.

The reflection and high-level rotation functions don’t resample. The shear functions can either use a default resampling filter or, if you require more control, a custom filter that you provide.

## See Also

- [Image shearing](image-shearing.md)
  Shear images horizontally and vertically.
- [Reducing artifacts with custom resampling filters](reducing-artifacts-with-custom-resampling-filters.md)
  Implement custom linear interpolation to prevent the ringing effects associated with scaling an image with the default Lanczos algorithm.
- [Image shearing](image-shearing.md)
  Shear images horizontally and vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/resampling-in-vimage)*