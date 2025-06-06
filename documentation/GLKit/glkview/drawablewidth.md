# drawableWidth

**Framework**: GLKit  
**Kind**: property

The width, in pixels, of the underlying framebuffer object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var drawableWidth: Int { get }
```

#### Discussion

The height and width of the underlying framebuffer object is calculated automatically by the view object based on its [`bounds`](https://developer.apple.com/documentation/UIKit/UIView/bounds) and [`contentScaleFactor`](https://developer.apple.com/documentation/UIKit/UIView/contentScaleFactor) properties and change whenever either of those properties change. Your application never directly adjusts the size of the framebuffer object. Instead, your application should read the [`drawableHeight`](glkview/drawableheight.md) and [`drawableWidth`](glkview/drawablewidth.md) properties and use those to configure its OpenGL ES rendering code. For example, you might use the [`drawableHeight`](glkview/drawableheight.md) and [`drawableWidth`](glkview/drawablewidth.md) properties to set the OpenGL ES viewport, determining the size and complexity of the art assets to load, and so on.

## See Also

- [var drawableHeight: Int](glkview/drawableheight.md)
  The height, in pixels, of the underlying framebuffer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/drawablewidth)*