# renderOptions

**Framework**: RealityKit  
**Kind**: property

The render options that configure the view’s AR session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency var renderOptions: ARView.RenderOptions { get set }
```

## Mentions

- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)

#### Discussion

RealityKit applies effects like camera grain, motion blur, and depth of field to the render to make the AR experience more immersive. Each effect causes your virtual content to better blend in with live images from the camera in some way.

To disable an effect, you add an option from the [`ARView.RenderOptions`](arview/renderoptions-swift.struct.md) option set to the view’s [`renderOptions`](arview/renderoptions-swift.property.md) property:

```swift
arView.renderOptions.insert(.disableMotionBlur) // Turn off motion blur.
```

When you create an AR view, the system automatically adds certain render options to disable effects that might be too demanding for the GPU hardware on which your app is running. But you can modify the [`renderOptions`](arview/renderoptions-swift.property.md) set at any time to enable or disable any particular effect, depending on the needs of your app.

To decide whether to use an effect, consider both its visual impact on your app, and its computational cost. Check the cost by measuring your app’s CPU and GPU utilization with the effect enabled across all the devices your app supports, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

## See Also

- [var session: ARSession](arview/session.md)
  The AR session that supports the view’s rendering.
- [var automaticallyConfigureSession: Bool](arview/automaticallyconfiguresession.md)
  An indication of whether to use an automatically configured AR session.
- [var renderCallbacks: ARView.RenderCallbacks](arview/rendercallbacks-swift.property.md)
  A container that holds the view’s render callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.property)*