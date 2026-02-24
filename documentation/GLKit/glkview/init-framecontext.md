# init(frame:context:)

**Framework**: GLKit  
**Kind**: init

Initializes a new view.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
init(frame: CGRect, context: EAGLContext)
```

#### Return Value

An initialized view object or `nil` if the object couldn’t be created.

## Parameters

- `frame`: The frame rectangle for the view, measured in points. The origin of the frame is relative to the superview in which you plan to add it. This method uses the frame rectangle to set the[`center`](https://developer.apple.com/documentation/UIKit/UIView/center) and [`bounds`](https://developer.apple.com/documentation/UIKit/UIView/bounds) properties accordingly.
- `context`: An OpenGL ES context used to store the framebuffer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/init(frame:context:))*