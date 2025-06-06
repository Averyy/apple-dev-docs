# init(device:options:)

**Framework**: SceneKit  
**Kind**: init

Creates a renderer with the specified Metal device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(device: (any MTLDevice)?, options: [AnyHashable : Any]? = nil)
```

#### Return Value

A new renderer object.

#### Discussion

Use this initializer to create a SceneKit renderer that draws into the rendering targets your app already uses to draw other content. For the `device` parameter, pass the [`MTLDevice`](https://developer.apple.com/documentation/Metal/MTLDevice) object your app uses for drawing. Then, to tell SceneKit to render your content, call the [`SCNRenderer`](scnrenderer.md) method, providing a command buffer and render pass descriptor for SceneKit to use in its rendering.

## Parameters

- `device`: A Metal device.
- `options`: An optional dictionary for future extensions.

## See Also

- [convenience init(context: EAGLContext?, options: [AnyHashable : Any]?)](scnrenderer/init(context:options:).md)
  Creates a renderer with the specified OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/init(device:options:))*