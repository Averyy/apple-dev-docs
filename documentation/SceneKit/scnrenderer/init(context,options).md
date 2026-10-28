# init(context:options:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a renderer with the specified OpenGL context.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS*

```swift
convenience init(context: EAGLContext?, options: [AnyHashable : Any]? = nil)
```

*macOS*

```swift
convenience init(context: CGLContextObj?, options: [AnyHashable : Any]? = nil)
```

*iOS, iPadOS, Mac Catalyst, tvOS*

```objc
+ (instancetype) rendererWithContext:(EAGLContext *) context options:(NSDictionary *) options;
```

*macOS*

```objc
+ (instancetype) rendererWithContext:(CGLContextObj) context options:(NSDictionary *) options;
```

## Return Value

A new renderer object.

## Discussion

Use this initializer to create a SceneKit renderer that draws into OpenGL context your app already uses to draw other content. To tell SceneKit to render your content, call the [`SCNRenderer`](../scnrenderer.md) or [`SCNRenderer`](../scnrenderer.md) method.

## Parameters

- `context`: An OpenGL rendering context: either a [`cglContextObj`](../../AppKit/nsopenglcontext/cglcontextobj.md) reference (in macOS) or an [`EAGLContext`](../../OpenGLES/eaglcontext.md) object (in iOS).
- `options`: An optional dictionary for future extensions.

## See Also

### Creating a Renderer
- [convenience init(device: (any MTLDevice)?, options: [AnyHashable : Any]?)](./init%28device,options%29.md)
  Creates a renderer with the specified Metal device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/init(context:options:))*