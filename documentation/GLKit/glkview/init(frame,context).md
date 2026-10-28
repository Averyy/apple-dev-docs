# init(frame:context:)

**Framework**: GLKit  
**Kind**: init  
**Role**: Initializer

Initializes a new view.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init(frame: CGRect, context: EAGLContext)
```

```objc
- (instancetype) initWithFrame:(CGRect) frame context:(EAGLContext *) context;
```

## Return Value

An initialized view object or `nil` if the object couldn’t be created.

## Parameters

- `frame`: The frame rectangle for the view, measured in points. The origin of the frame is relative to the superview in which you plan to add it. This method uses the frame rectangle to set the[`center`](../../UIKit/uiview/center.md) and [`bounds`](../../UIKit/uiview/bounds.md) properties accordingly.
- `context`: An OpenGL ES context used to store the framebuffer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/init(frame:context:))*