# trackingAreasTextures

**Framework**: Compositor Services  
**Kind**: property

Use the returned texture in your render pipeline to store the tracking areas ID used for hover effects and indirect gestures. The layer’s texture topology determines the layout and content for each texture. The drawable’s views contain information about how those views map to the textures.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var trackingAreasTextures: [any MTLTexture] { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/trackingareastextures)*