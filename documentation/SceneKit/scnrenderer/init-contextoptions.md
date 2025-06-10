# init(context:options:)

**Framework**: SceneKit  
**Kind**: init

Creates a renderer with the specified OpenGL context.

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
convenience init(context: CGLContextObj?, options: [AnyHashable : Any]? = nil)
```

#### Return Value

A new renderer object.

#### Discussion

Use this initializer to create a SceneKit renderer that draws into OpenGL context your app already uses to draw other content. To tell SceneKit to render your content, call the [`SCNRenderer`](scnrenderer.md) or [`SCNRenderer`](scnrenderer.md) method.

## Parameters

- `context`: An OpenGL rendering context: either a   reference (in macOS) or an   object (in iOS).
- `options`: An optional dictionary for future extensions.

## See Also

- [convenience init(device: (any MTLDevice)?, options: [AnyHashable : Any]?)](scnrenderer/init(device:options:).md)
  Creates a renderer with the specified Metal device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/init(context:options:))*