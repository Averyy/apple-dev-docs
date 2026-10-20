# session

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

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

RealityKit automatically creates a default session that the view manages. If you have an existing or custom session, setting it as the view’s session replaces the default session. If you replace the default session, you need to start it by calling [`run(_:options:)`](../../ARKit/arsession/run%28_,options%29.md). See [`automaticallyConfigureSession`](./automaticallyconfiguresession.md) for more details.

When [`automaticallyConfigureSession`](./automaticallyconfiguresession.md) is [`true`](../../Swift/true.md), the default value is an [`ARWorldTrackingConfiguration`](../../ARKit/arworldtrackingconfiguration.md).

## See Also

### Configuring the AR session
- [var automaticallyConfigureSession: Bool](./automaticallyconfiguresession.md)
  An indication of whether to use an automatically configured AR session.
- [var renderOptions: ARView.RenderOptions](./renderoptions-swift.property.md)
  The render options that configure the view’s AR session.
- [var renderCallbacks: ARView.RenderCallbacks](./rendercallbacks-swift.property.md)
  A container that holds the view’s render callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/session)*