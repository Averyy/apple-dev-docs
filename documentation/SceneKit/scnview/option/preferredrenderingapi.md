# preferredRenderingAPI

**Framework**: SceneKit  
**Kind**: property

The rendering API to use for rendering the view (for example, Metal or OpenGL).

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
static let preferredRenderingAPI: SCNView.Option
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing one of the values listed in [`SCNRenderingAPI`](scnrenderingapi.md). You can also set this option from the inspector in Interface Builder.

SceneKit attempts to initialize a view using the preferred API you specify in the [`SCNView`](scnview.md) initializer; if the current device does not support the preferred API, SceneKit automatically falls back to a supported API. After initialization, use the [`renderingAPI`](scnscenerenderer/renderingapi.md) property to find out whether a fallback occurred. For example, if you specify the [`SCNRenderingAPI.metal`](scnrenderingapi/metal.md) option when initializing a view on an iOS device that does not support Metal, SceneKit defaults to the [`SCNRenderingAPI.openGLES2`](scnrenderingapi/opengles2.md) option instead.

## See Also

- [static let preferLowPowerDevice: SCNView.Option](scnview/option/preferlowpowerdevice.md)
  An option for whether to select low-power-usage devices for Metal rendering.
- [static let preferredDevice: SCNView.Option](scnview/option/preferreddevice.md)
  The device to use for Metal rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/option/preferredrenderingapi)*