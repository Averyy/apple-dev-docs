# presentRenderbuffer(_:)

**Framework**: OpenGL ES  
**Kind**: method

Displays a renderbuffer’s contents on screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
func presentRenderbuffer(_ target: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The renderbuffer to be displayed must have been allocated storage using the [`renderbufferStorage(_:from:)`](eaglcontext/renderbufferstorage(_:from:).md) method. The exact semantics for how and when the renderbuffer contents are displayed is controlled by the drawable object.

> ❗ **Important**:  The contents of the renderbuffer may be altered after the renderbuffer is presented to the screen. After presenting the renderbuffer, your application must   redraw the contents of the renderbuffer before presenting it again. To preserve the contents of the renderbuffer you may set the [`kEAGLDrawablePropertyRetainedBacking`](keagldrawablepropertyretainedbacking.md) key of the `drawableProperties` dictionary to [`true`](https://developer.apple.com/documentation/swift/true). Setting the key to [`true`](https://developer.apple.com/documentation/swift/true) may result in reduced graphics performance and increased memory usage. Therefore, choose this setting only when you need the renderbuffer’s contents to remain unchanged.

## Parameters

- `target`: The OpenGL ES binding point for a currently bound renderbuffer. The value of this parameter must be   (or   in an OpenGL ES 1.1 context).

## See Also

- [func renderbufferStorage(Int, from: (any EAGLDrawable)?) -> Bool](eaglcontext/renderbufferstorage(_:from:).md)
  Binds a drawable object’s storage to an OpenGL ES renderbuffer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/presentrenderbuffer(_:))*