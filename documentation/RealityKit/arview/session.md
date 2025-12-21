# session

**Framework**: RealityKit  
**Kind**: property

The AR session that supports the view’s rendering.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency dynamic var session: ARSession { get set }
```

#### Discussion

RealityKit automatically creates a default session that the view manages. If you have an existing or custom session, setting it as the view’s session replaces the default session. If you replace the default session, you need to start it by calling [`run(_:options:)`](https://developer.apple.com/documentation/ARKit/ARSession/run(_:options:)). See [`automaticallyConfigureSession`](arview/automaticallyconfiguresession.md) for more details.

When [`automaticallyConfigureSession`](arview/automaticallyconfiguresession.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the default value is an [`ARWorldTrackingConfiguration`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration).

## See Also

- [var automaticallyConfigureSession: Bool](arview/automaticallyconfiguresession.md)
  An indication of whether to use an automatically configured AR session.
- [var renderOptions: ARView.RenderOptions](arview/renderoptions-swift.property.md)
  The render options that configure the view’s AR session.
- [var renderCallbacks: ARView.RenderCallbacks](arview/rendercallbacks-swift.property.md)
  A container that holds the view’s render callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/session)*