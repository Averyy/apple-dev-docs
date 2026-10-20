# SCNBlendMode.multiply

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Blend by multiplying the source color with the background color.

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
case multiply
```

```c
SCNBlendModeMultiply
```

#### Discussion

This mode results in colors that are at least as dark as either of the two contributing colors.

## See Also

### Constants
- [SCNBlendMode.alpha](./alpha.md)
  Blend by multiplying source and destination color values by their corresponding alpha values.
- [SCNBlendMode.add](./add.md)
  Blend by adding the source color to the destination color.
- [SCNBlendMode.subtract](./subtract.md)
  Blend by subtracting the source color from the destination color.
- [SCNBlendMode.screen](./screen.md)
  Blend by multiplying the inverse of the source color with the inverse of the destination color.
- [SCNBlendMode.replace](./replace.md)
  Blend by replacing the destination color with the source color, ignoring alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnblendmode/multiply)*