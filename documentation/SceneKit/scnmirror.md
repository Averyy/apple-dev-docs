# SCNMirror

**Framework**: SceneKit

Equivalent to [`SCNWrapMode.mirror`](scnwrapmode/mirror.md).

#### Overview

Deprecated in OS X v10.9. Use [`SCNWrapMode.mirror`](scnwrapmode/mirror.md) instead.

## See Also

- [SCNWrapMode.clamp](scnwrapmode/clamp.md)
  Texture coordinates are clamped to the range from `0.0` to `1.0`, inclusive.
- [SCNWrapMode.repeat](scnwrapmode/repeat.md)
  Texture sampling uses only the fractional part of texture coordinates, passing through the range from `0.0` to (but not including) `1.0`.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmirror)*