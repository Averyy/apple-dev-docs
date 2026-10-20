# SCNFilterMode.none

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

No texture filtering is applied.

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
case none
```

```c
SCNFilterModeNone
```

#### Discussion

Only valid for the [`mipFilter`](../scnmaterialproperty/mipfilter.md) property, specifying that SceneKit should not use mip mapping.

## See Also

### Constants
- [SCNFilterMode.nearest](./nearest.md)
  Texture filtering returns the color from only one texel, whose location is nearest to the coordinates being sampled.
- [SCNFilterMode.linear](./linear.md)
  Texture filtering sample texels from the neighborhood of the coordinates being sampled and linearly interpolates their colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfiltermode/none)*