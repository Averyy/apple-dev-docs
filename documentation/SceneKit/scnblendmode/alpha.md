# SCNBlendMode.alpha

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Blend by multiplying source and destination color values by their corresponding alpha values.

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
case alpha
```

```c
SCNBlendModeAlpha
```

## Discussion

This mode is the default value of the [`blendMode`](../scnmaterial/blendmode.md) property.

## See Also

### Constants
- [SCNBlendMode.add](./add.md)
  Blend by adding the source color to the destination color.
- [SCNBlendMode.subtract](./subtract.md)
  Blend by subtracting the source color from the destination color.
- [SCNBlendMode.multiply](./multiply.md)
  Blend by multiplying the source color with the background color.
- [SCNBlendMode.screen](./screen.md)
  Blend by multiplying the inverse of the source color with the inverse of the destination color.
- [SCNBlendMode.replace](./replace.md)
  Blend by replacing the destination color with the source color, ignoring alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnblendmode/alpha)*