# EAGLDrawable

**Framework**: OpenGL ES  
**Kind**: protocol

iOS objects that implement the `EAGLDrawable` protocol can be used as a rendering surface and displayed to the screen by an `EAGLContext` object. In iOS 2.0, this protocol is implemented only by the `CAEAGLLayer` class, but in the future other classes may choose to implement the protocol. The `EAGLDrawable` protocol is not intended to be implemented by objects outside of the iOS.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
protocol EAGLDrawable
```

## Topics

### Drawable Properties
- [var drawableProperties: [String : Any]?](eagldrawable/drawableproperties.md)
  A dictionary of values that specify the desired characteristics of the drawable surface.
### Constants
- [Drawable Property Keys](drawable-property-keys.md)
  Keys to specify in the `drawableProperties` dictionary.
- [Color Formats](color-formats.md)
  Color formats that can be specified under the `kEAGLDrawablePropertyColorFormat` key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eagldrawable)*