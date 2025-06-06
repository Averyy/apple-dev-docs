# ARView.RenderCallbacks

**Framework**: RealityKit  
**Kind**: struct

A container that holds the view’s render callbacks.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct RenderCallbacks
```

#### Overview

Render callbacks are closures RealityKit calls at predefined times. You can use render callbacks to modify the results of RealityKit’s rendering. If you assign a function or closure to any of the contained callback properties, RealityKit calls that function or closure at a predefined time. Setting the [`postProcess`](arview/rendercallbacks-swift.struct/postprocess.md) property, for example, causes RealityKit to call the assigned function or closure every frame, after RealityKit renders the scene, but before it displays it.

## Topics

### Creating a callback object
- [init()](arview/rendercallbacks-swift.struct/init.md)
  Creates a new object.
### Register callback closures
- [var prepareWithDevice: ((any MTLDevice) -> Void)?](arview/rendercallbacks-swift.struct/preparewithdevice.md)
  A callback function for doing initial setup work.
- [var postProcess: ((ARView.PostProcessContext) -> Void)?](arview/rendercallbacks-swift.struct/postprocess.md)
  A callback function for implementing postprocess effects.

## See Also

- [Postprocessing effects](postprocessing-effects.md)
  Create special rendering effects for your RealityKit scenes.
- [ARView.PostProcessContext](arview/postprocesscontext.md)
  An object the framework uses to pass data to a postprocess callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/rendercallbacks-swift.struct)*