# SCNWrapMode.repeat

**Framework**: SceneKit  
**Kind**: case

Texture sampling uses only the fractional part of texture coordinates, passing through the range from `0.0` to (but not including) `1.0`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case `repeat`
```

## Mentions

- [SCNRepeat](scnrepeat.md)

#### Discussion

Texture sampling in areas of the material whose texture coordinates would fall outside from `0.0` to `1.0` results in tiling the texture image across the surface using the material.

## See Also

- [SCNWrapMode.clamp](scnwrapmode/clamp.md)
  Texture coordinates are clamped to the range from `0.0` to `1.0`, inclusive.
- [SCNWrapMode.clampToBorder](scnwrapmode/clamptoborder.md)
  Texture sampling uses texture colors for coordinates in the range from `0.0` to `1.0` (inclusive) and the material property’s [`borderColor`](scnmaterialproperty/bordercolor.md) value otherwise.
- [SCNWrapMode.mirror](scnwrapmode/mirror.md)
  Texture sampling of texture coordinates outside range from `0.0` to `1.0` should behave as if the range reverses before repeating.
- [SCNClamp](scnclamp.md)
  Equivalent to [`SCNWrapMode.clamp`](scnwrapmode/clamp.md).
- [SCNRepeat](scnrepeat.md)
  Equivalent to [`SCNWrapMode.repeat`](scnwrapmode/repeat.md).
- [SCNClampToBorder](scnclamptoborder.md)
  Equivalent to [`SCNWrapMode.clampToBorder`](scnwrapmode/clamptoborder.md).
- [SCNMirror](scnmirror.md)
  Equivalent to [`SCNWrapMode.mirror`](scnwrapmode/mirror.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnwrapmode/repeat)*