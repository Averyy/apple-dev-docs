# drawableWidth

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The width, in pixels, of the underlying framebuffer object.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var drawableWidth: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger drawableWidth;
```

#### Discussion

The height and width of the underlying framebuffer object is calculated automatically by the view object based on its [`bounds`](../../UIKit/uiview/bounds.md) and [`contentScaleFactor`](../../UIKit/uiview/contentscalefactor.md) properties and change whenever either of those properties change. Your application never directly adjusts the size of the framebuffer object. Instead, your application should read the [`drawableHeight`](./drawableheight.md) and [`drawableWidth`](./drawablewidth.md) properties and use those to configure its OpenGL ES rendering code. For example, you might use the [`drawableHeight`](./drawableheight.md) and [`drawableWidth`](./drawablewidth.md) properties to set the OpenGL ES viewport, determining the size and complexity of the art assets to load, and so on.

## See Also

### Read-only Framebuffer Properties
- [var drawableHeight: Int](./drawableheight.md)
  The height, in pixels, of the underlying framebuffer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/drawablewidth)*