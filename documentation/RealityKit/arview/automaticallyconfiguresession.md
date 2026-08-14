# automaticallyConfigureSession

**Framework**: RealityKit  
**Kind**: property

An indication of whether to use an automatically configured AR session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency var automaticallyConfigureSession: Bool { get set }
```

#### Discussion

When enabled, the [`ARView`](arview.md) automatically runs an `RealityKit/ARSession` with a default configuration. RealityKit updates that configuration based  on t camera mode and scene anchors. When disabled, you need to provide a configuration object and run the session manually.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var session: ARSession](arview/session.md)
  The AR session that supports the view’s rendering.
- [var renderOptions: ARView.RenderOptions](arview/renderoptions-swift.property.md)
  The render options that configure the view’s AR session.
- [var renderCallbacks: ARView.RenderCallbacks](arview/rendercallbacks-swift.property.md)
  A container that holds the view’s render callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/automaticallyconfiguresession)*