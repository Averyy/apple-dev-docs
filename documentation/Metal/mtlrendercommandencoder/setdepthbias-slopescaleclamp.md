# setDepthBias(_:slopeScale:clamp:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setDepthBias(_ depthBias: Float, slopeScale: Float, clamp: Float)
```

#### Discussion

Call this method to have the render pipeline apply a bias to the rasterized depth after the clipping stage. The bias affects both depth testing and the values the render pipeline writes to the depth render target. If you don’t explicitly call this method, the pipeline doesn’t apply a scale or a bias to a depth value.

> **Note**:  A depth bias only influences triangle primitives, but doesn’t apply to points or lines.

You can use a slope-scaled bias to fine-tune shadow maps and avoid artifacts. Depth artifacts typically come from polygons that exist in the same plane or when a polygon shadows itself, also known as . The pipeline calculates the bias value differently depending on the data type of the depth pixel format (see [`MTLPixelFormat`](mtlpixelformat.md)).

For unsigned normal or (`Unorm`) pixel formats, the pipeline calculates the bias with a formula that consists of the following definitions:

- The `r` constant is the smallest positive value possible for a depth render target.
- The `maxSlope` variable is the largest possible slope of the depth value at a pixel.

```other
bias = (depthBias * r) + (slopeScale * maxSlope)
```

For floating-point (`Float`) pixel formats, the pipeline calculates the bias with a formula that consists of the following definitions:

- The `z` variable is the largest absolute-value vertex depth of the vertices that belong to the primitive.
- The `r` constant is the number of mantissa bits of the floating-point pixel format (not counting the `hidden` bit).
- The `maxSlope` variable is the largest possible slope of the depth value at a pixel.

```other
// Get the depth of the vertex within a primitive that has the largest (absolute value) depth.
z = largestAbsoluteDepth(primitive)

// The exponent for 2 is equal to e^(z - r).
exponent = exp(z - r)

// Calculate the bias.
bias = (depthBias * pow(2, exponent)) + (slopeScale * maxSlope)
```

The render pipeline clamps the final bias value if `clamp` isn’t zero.

```other
if (clamp > 0.0) {
    bias = min(clamp, bias)
} else if (clamp < 0.0) {
    bias = max(clamp, bias)
}
```

If `clamp` is greater than zero, the pipeline sets the final bias to `clamp` when the formula’s value is greater than `clamp`. If `clamp` is less than zero, the pipeline set the final bias value to `clamp` when the formula’s value is less than `clamp`.

The pipeline adds the final bias value to the depth value, but only if `depthBias` or `slopeScale` is nonzero.

```other
if (depthBias != 0.0 || slopeScale != 0.0) {
    depth += bias
}
```

## Parameters

- `depthBias`: A constant bias the render pipeline applies to all fragments.
- `slopeScale`: A bias coefficient that scales with the depth of the primitive relative to the camera.
- `clamp`: You can disable the bias clamping functionality by passing  .

## See Also

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtlrendercommandencoder/setdepthstencilstate(_:).md)
  Configures the combined depth and stencil state.
- [func setDepthClipMode(MTLDepthClipMode)](mtlrendercommandencoder/setdepthclipmode(_:).md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](mtlrendercommandencoder/setstencilreferencevalues(front:back:).md)
  Configures different comparison values for front- and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:))*