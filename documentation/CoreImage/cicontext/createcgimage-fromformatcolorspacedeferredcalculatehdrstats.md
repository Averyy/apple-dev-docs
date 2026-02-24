# createCGImage(_:from:format:colorSpace:deferred:calculateHDRStats:)

**Framework**: Core Image  
**Kind**: method

Creates a Core Graphics image from a region of a Core Image image instance with an option for calculating HDR statistics.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func createCGImage(_ image: CIImage, from fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool, calculateHDRStats: Bool) -> CGImage?
```

#### Return Value

 Returns a new `CGImage` instance. You are responsible for releasing the returned image when you no longer need it. The returned value will be `null` if the extent is empty or too big.

## Parameters

- `image`: A [`CIImage`](ciimage.md) image instance for which to create a `CGImage`.
- `fromRect`: The `CGRect` region of the `image` to use. This region relative to the cartesean coordinate system of `image`. This region will be intersected with integralized and intersected with `image.extent`.
- `format`: A [`CIFormat`](ciformat.md) to specify the pixel format of the created `CGImage`. For example, if `kCIFormatRGBX16` is specified, then the created `CGImage` will be 16 bits-per-component and opaque.
- `colorSpace`: The `CGColorSpace` for the output image. This color space must have either `CGColorSpaceModel.rgb` or `CGColorSpaceModel.monochrome` and be compatible with the specified pixel format.
- `deferred`: Controls when Core Image renders `image`. - True: rendering of `image` is deferred until the created `CGImage` rendered.
- False: the `image` is rendered immediately.
- `calculateHDRStats`: Controls if Core Image calculates HDR statistics. - True: Core Image will immediately render `image`, calculate the HDR statistics and create a `CGImage` that has the calculated values.
- False:  the created `CGImage` will not have any HDR statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/createcgimage(_:from:format:colorspace:deferred:calculatehdrstats:))*