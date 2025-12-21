# device

**Framework**: Compositor Services  
**Kind**: property

The GPU device that the layer renderer uses for drawing operations

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

#### Discussion

You can inspect the device for any information you might need. The system uses it to create the textures for drawing, and also to create synchronization events for the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/device)*