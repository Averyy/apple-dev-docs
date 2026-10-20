# SCNView.Option

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Dictionary keys specifying initialization options, used when initializing a SceneKit view.

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
struct Option
```

```c
typedef NSString * SCNViewOption;
```

## Topics

### View Options
- [static let preferLowPowerDevice: SCNView.Option](./option/preferlowpowerdevice.md)
  An option for whether to select low-power-usage devices for Metal rendering.
- [static let preferredDevice: SCNView.Option](./option/preferreddevice.md)
  The device to use for Metal rendering.
- [static let preferredRenderingAPI: SCNView.Option](./option/preferredrenderingapi.md)
  The rendering API to use for rendering the view (for example, Metal or OpenGL).
### Initializers
- [init(rawValue: String)](./option/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Initializing a SceneKit View
- [init(frame: CGRect, options: [String : Any]?)](./init%28frame,options%29.md)
  Initializes and returns a newly allocated SceneKit view object with the specified frame rectangle and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/option)*