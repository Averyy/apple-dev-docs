# SCNView.Option

**Framework**: SceneKit  
**Kind**: struct

Dictionary keys specifying initialization options, used when initializing a SceneKit view.

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
struct Option
```

## Topics

### View Options
- [static let preferLowPowerDevice: SCNView.Option](scnview/option/preferlowpowerdevice.md)
  An option for whether to select low-power-usage devices for Metal rendering.
- [static let preferredDevice: SCNView.Option](scnview/option/preferreddevice.md)
  The device to use for Metal rendering.
- [static let preferredRenderingAPI: SCNView.Option](scnview/option/preferredrenderingapi.md)
  The rendering API to use for rendering the view (for example, Metal or OpenGL).
### Initializers
- [init(rawValue: String)](scnview/option/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(frame: CGRect, options: [String : Any]?)](scnview/init(frame:options:).md)
  Initializes and returns a newly allocated SceneKit view object with the specified frame rectangle and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/option)*