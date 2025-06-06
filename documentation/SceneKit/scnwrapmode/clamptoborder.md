# SCNWrapMode.clampToBorder

**Framework**: SceneKit  
**Kind**: case

Texture sampling uses texture colors for coordinates in the range from `0.0` to `1.0` (inclusive) and the material property’s [`borderColor`](scnmaterialproperty/bordercolor.md) value otherwise.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case clampToBorder
```

## Mentions

- [SCNClampToBorder](scnclamptoborder.md)

#### Discussion

Texture sampling in areas whose texture coordinates would fall outside this range uses the [`borderColor`](scnmaterialproperty/bordercolor.md) property instead of texel colors from the texture image.

## See Also

- [SCNWrapMode.clamp](scnwrapmode/clamp.md)
  Texture coordinates are clamped to the range from `0.0` to `1.0`, inclusive.
- [SCNWrapMode.repeat](scnwrapmode/repeat.md)
  Texture sampling uses only the fractional part of texture coordinates, passing through the range from `0.0` to (but not including) `1.0`.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnwrapmode/clamptoborder)*