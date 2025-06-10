# supportsFoveation

**Framework**: Compositor Services  
**Kind**: property

A Boolean value that indicates whether the layer supports variable rasterization rates.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var supportsFoveation: Bool { get }
```

#### Discussion

Foveation support lets you reduce the amount of high-resolution drawing you do. When foveation support is available, the system provides a variable rasterization rate map that defines the content resolution in different parts of the texture. This map allows you to render content in someone’s peripheral vision at a lower resolution than content in the center of their vision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportsfoveation)*