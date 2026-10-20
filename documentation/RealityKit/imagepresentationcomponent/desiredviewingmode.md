# desiredViewingMode

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The user-selected preferred content viewing mode.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var desiredViewingMode: ImagePresentationComponent.ViewingMode
```

#### Discussion

The `viewingMode` property will update to this value if it is valid for this component’s content, otherwise a suitable fallback will be used.

## See Also

### Setting and discovering viewing modes
- [ImagePresentationComponent.ViewingMode](./viewingmode-swift.struct.md)
  Image content’s rendering mode.
- [var viewingMode: ImagePresentationComponent.ViewingMode](./viewingmode-swift.property.md)
  The currently active viewing mode of the presented image.
- [var availableViewingModes: Set<ImagePresentationComponent.ViewingMode>](./availableviewingmodes.md)
  The currently valid viewing modes for the image being presented.
- [static func supportedViewingModes(for: CGImageSource) -> Set<ImagePresentationComponent.ViewingMode>](./supportedviewingmodes%28for%29-7za1y.md)
  The viewing modes supported by the provided image source.
- [static func supportedViewingModes(for: CGImageSource) -> Set<ImagePresentationComponent.ViewingMode>](./supportedviewingmodes%28for%29-7za1y.md)
  The viewing modes supported by the provided image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/desiredviewingmode)*