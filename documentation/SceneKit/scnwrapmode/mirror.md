# SCNWrapMode.mirror

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Texture sampling of texture coordinates outside range from `0.0` to `1.0` should behave as if the range reverses before repeating.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
case mirror
```

```c
SCNWrapModeMirror
```

## Mentions

- [SCNMirror](../scnmirror.md)

## Discussion

Texture sampling in areas of the material whose texture coordinates would fall outside from `0.0` to `1.0` results in tiling both texture image and its mirror image across the surface using the material.

## See Also

### Constants
- [SCNWrapMode.clamp](./clamp.md)
  Texture coordinates are clamped to the range from `0.0` to `1.0`, inclusive.
- [SCNWrapMode.repeat](./repeat.md)
  Texture sampling uses only the fractional part of texture coordinates, passing through the range from `0.0` to (but not including) `1.0`.
- [SCNWrapMode.clampToBorder](./clamptoborder.md)
  Texture sampling uses texture colors for coordinates in the range from `0.0` to `1.0` (inclusive) and the material property’s [`borderColor`](../scnmaterialproperty/bordercolor.md) value otherwise.
- [SCNClamp](../scnclamp.md)
  Equivalent to [`SCNWrapMode.clamp`](./clamp.md).
- [SCNRepeat](../scnrepeat.md)
  Equivalent to [`SCNWrapMode.repeat`](./repeat.md).
- [SCNClampToBorder](../scnclamptoborder.md)
  Equivalent to [`SCNWrapMode.clampToBorder`](./clamptoborder.md).
- [SCNMirror](../scnmirror.md)
  Equivalent to [`SCNWrapMode.mirror`](./mirror.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnwrapmode/mirror)*