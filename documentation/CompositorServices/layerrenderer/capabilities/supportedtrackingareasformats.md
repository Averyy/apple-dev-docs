# supportedTrackingAreasFormats

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

An array of tracking areas formats that the layer supports for its textures.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var supportedTrackingAreasFormats: [MTLPixelFormat] { get }
```

#### Discussion

The pixel formats in this property tell you which pixel arrangements and characteristics the layer supports for its tracking areas textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportedtrackingareasformats)*