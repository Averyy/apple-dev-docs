# generateFlippedRasterizationRateMaps

**Framework**: Compositor Services  
**Kind**: property

A Boolean value that indicates whether the layer renderer provides rasterization rate maps flipped around the y-axis.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var generateFlippedRasterizationRateMaps: Bool { get set }
```

#### Discussion

When foveation is enabled and the value of this property is `true`, the layer renderer generates both flipped and nonflipped rasterization rate maps. When the value of this property is `false`, the layer renderer generates only the nonflipped rasterization rate maps. The default value of this property is `false`.

To generate flipped rasterization rate maps, the system must perform extra computational work during your app’s render loop. Enable this support only if your drawing engine requires these extra rate maps and you can afford the extra cost.

## See Also

- [var isFoveationEnabled: Bool](layerrenderer/configuration-swift.struct/isfoveationenabled.md)
  A value that indicates if the layer is using variable rasterization rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/generateflippedrasterizationratemaps)*