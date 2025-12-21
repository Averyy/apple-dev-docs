# renderbufferStorage(_:from:)

**Framework**: OpenGL ES  
**Kind**: method

Binds a drawable object’s storage to an OpenGL ES renderbuffer object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
func renderbufferStorage(_ target: Int, from drawable: (any EAGLDrawable)?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

To create a renderbuffer that can be presented to the screen, you bind the renderbuffer and then allocate shared storage for it by calling this method. This method call replaces the call normally made to `glRenderbufferStorage`. A renderbuffer whose storage has been allocated with this method can later be displayed with a call to [`presentRenderbuffer(_:)`](eaglcontext/presentrenderbuffer(_:).md).

The width, height, and internal color buffer format are derived from the characteristics of the drawable object. You may override the internal color buffer format by adding an [`kEAGLDrawablePropertyColorFormat`](keagldrawablepropertycolorformat.md) key to the [`drawableProperties`](eagldrawable/drawableproperties.md) dictionary of the drawable object before calling this method.

To specify that the OpenGL ES renderbuffer should be detached from the drawable object, call this method with the `drawable` parameter set to `nil`.

##### Special Considerations

In iOS 6.0 and later, this method automatically flushes the OpenGL ES command buffer, making it unsuitable to call repeatedly in performance-critical code.

## Parameters

- `target`: The OpenGL ES binding point for a currently bound renderbuffer. The value of this parameter must be   (or   in an OpenGL ES 1.1 context).
- `drawable`: An object managing the data store for the renderbuffer. In iOS, the value of this parameter must be a   object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/renderbufferstorage(_:from:))*