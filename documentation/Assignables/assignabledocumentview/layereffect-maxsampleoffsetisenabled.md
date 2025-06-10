# layerEffect(_:maxSampleOffset:isEnabled:)

**Framework**: Assignables  
**Kind**: method

Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func layerEffect(_ shader: Shader, maxSampleOffset: CGSize, isEnabled: Bool = true) -> some View
```

#### Return Value

A new view that renders `self` with the shader applied as a distortion effect.

#### Discussion

For a shader function to act as a layer effect it must have a function signature matching:

```None
[[ stitchable ]] half4 name(float2 position,
  SwiftUI::Layer layer, args...)
```

where `position` is the user-space coordinates of the destination pixel applied to the shader, and `layer` is a subregion of the rasterized contents of `self`. `args...` should be compatible with the uniform arguments bound to `shader`.

The `SwiftUI::Layer` type is defined in the `<SwiftUI/SwiftUI.h>` header file. It exports a single `sample()` function that returns a linearly-filtered pixel value from a position in the source content, as a premultiplied RGBA pixel value:

```None
namespace SwiftUI {
  struct Layer {
    half4 sample(float2 position) const;
  };
};
```

The function should return the color mapping to the destination pixel, typically by sampling one or more pixels from `layer` at location(s) derived from `position` and them applying some kind of transformation to produce a new color.

> ❗ **Important**: Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

## Parameters

- `shader`: The shader to apply as a layer effect.
- `maxSampleOffset`: If the shader function samples from the   layer at locations not equal to the destination position,   this value must specify the maximum sampling distance in   each axis, for all source pixels.
- `isEnabled`: Whether the effect is enabled or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/layereffect(_:maxsampleoffset:isenabled:))*