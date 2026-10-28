# presentRenderbuffer(_:)

**Framework**: OpenGL ES  
**Kind**: method  
**Role**: Instance Method

Displays a renderbuffer’s contents on screen.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func presentRenderbuffer(_ target: Int) -> Bool
```

```objc
- (BOOL) presentRenderbuffer:(NSUInteger) target;
```

## Return Value

[`true`](../../Swift/true.md) if successful; otherwise, [`false`](../../Swift/false.md).

## Discussion

The renderbuffer to be displayed must have been allocated storage using the [`renderbufferStorage(_:from:)`](./renderbufferstorage%28_,from%29.md) method. The exact semantics for how and when the renderbuffer contents are displayed is controlled by the drawable object.

> ❗ **Important**:  The contents of the renderbuffer may be altered after the renderbuffer is presented to the screen. After presenting the renderbuffer, your application must  *completely* redraw the contents of the renderbuffer before presenting it again. To preserve the contents of the renderbuffer you may set the [`kEAGLDrawablePropertyRetainedBacking`](../keagldrawablepropertyretainedbacking.md) key of the `drawableProperties` dictionary to [`true`](../../Swift/true.md). Setting the key to [`true`](../../Swift/true.md) may result in reduced graphics performance and increased memory usage. Therefore, choose this setting only when you need the renderbuffer’s contents to remain unchanged.

## Parameters

- `target`: The OpenGL ES binding point for a currently bound renderbuffer. The value of this parameter must be `GL_RENDERBUFFER` (or `GL_RENDERBUFFER_OES` in an OpenGL ES 1.1 context).

## See Also

### Related Documentation
- [func renderbufferStorage(Int, from: (any EAGLDrawable)?) -> Bool](./renderbufferstorage%28_,from%29.md)
  Binds a drawable object’s storage to an OpenGL ES renderbuffer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/presentrenderbuffer(_:))*