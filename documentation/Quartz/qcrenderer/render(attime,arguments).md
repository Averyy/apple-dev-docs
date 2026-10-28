# render(atTime:arguments:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Renders a frame of a composition at the specified time.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func render(atTime time: TimeInterval, arguments: [AnyHashable : Any]!) -> Bool
```

```objc
- (BOOL) renderAtTime:(NSTimeInterval) time arguments:(NSDictionary *) arguments;
```

## Return Value

[`true`](../../Swift/true.md) if successful.

## Discussion

You need to call this method each time you want to render a frame of the composition.

All OpenGL states are preserved  *except* the following:

- States defined by `GL_CURRENT_BIT`
- Textures on each unit and the environment mode
- Matrix mode

If you are using double buffers, keep in mind that the `renderAtTime:arguments:` method does not swap the front and back buffers of the OpenGL context. You must perform the swap yourself by calling the OpenGL command `flushBuffer` on the context associated with the renderer.

If you are interleaving OpenGL code with rendering of a composition, make sure that the OpenGL context is current. If you are using the [`NSOpenGLContext`](../../AppKit/nsopenglcontext.md) class, call the [`makeCurrentContext()`](../../AppKit/nsopenglcontext/makecurrentcontext%28%29.md) method prior to rendering. If you are using the CGL API, call the function `CGLSetCurrentContext(_:)`.

## Parameters

- `time`: The time, in seconds, at which  to render a composition frame. The time must be a positive value or zero.
- `arguments`: An optional dictionary that can have any of the entries defined in [Rendering Arguments](../rendering-arguments.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/render(attime:arguments:))*