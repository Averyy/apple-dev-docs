# SCNBlendMode.add

**Framework**: SceneKit  
**Kind**: case

Blend by adding the source color to the destination color.

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
case add
```

#### Discussion

This mode results in a brightening effect that can be useful for making objects appear to glow relative to their surroundings.

## See Also

- [SCNBlendMode.alpha](scnblendmode/alpha.md)
  Blend by multiplying source and destination color values by their corresponding alpha values.
- [SCNBlendMode.subtract](scnblendmode/subtract.md)
  Blend by subtracting the source color from the destination color.
- [SCNBlendMode.multiply](scnblendmode/multiply.md)
  Blend by multiplying the source color with the background color.
- [SCNBlendMode.screen](scnblendmode/screen.md)
  Blend by multiplying the inverse of the source color with the inverse of the destination color.
- [SCNBlendMode.replace](scnblendmode/replace.md)
  Blend by replacing the destination color with the source color, ignoring alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnblendmode/add)*