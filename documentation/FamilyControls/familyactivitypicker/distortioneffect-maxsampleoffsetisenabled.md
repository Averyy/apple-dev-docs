# distortionEffect(_:maxSampleOffset:isEnabled:)

**Framework**: FamilyControls  
**Kind**: method

Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
nonisolated
func distortionEffect(_ shader: Shader, maxSampleOffset: CGSize, isEnabled: Bool = true) -> some View
```

#### Return Value

A new view that renders `self` with the shader applied as a distortion effect.

#### Discussion

For a shader function to act as a distortion effect it must have a function signature matching:

```swift
[[ stitchable ]] float2 name(float2 position, args...)
```

where `position` is the user-space coordinates of the destination pixel applied to the shader. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the user-space coordinates of the corresponding source pixel.

> ❗ **Important**: Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

## Parameters

- `shader`: The shader to apply as a distortion effect.
- `maxSampleOffset`: The maximum distance in each axis between   the returned source pixel position and the destination pixel   position, for all source pixels.
- `isEnabled`: Whether the effect is enabled or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/distortioneffect(_:maxsampleoffset:isenabled:))*