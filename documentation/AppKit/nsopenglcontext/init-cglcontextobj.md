# init(cglContextObj:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns an OpenGL context object using an existing CGL context.

**Availability**:
- macOS 10.6+

## Declaration

```swift
init?(cglContextObj context: CGLContextObj)
```

#### Return Value

An initialized context.

#### Discussion

If your application already has a CGL context, you can wrap a [`NSOpenGLContext`](nsopenglcontext.md) object around it using this method. This method retains the CGL context by calling `CGLRetainContext(_:)`.

Only one [`NSOpenGLContext`](nsopenglcontext.md) object can wrap a specific context.

Your application should not call `CGLDestroyContext(_:)` to dispose of the CGL context. Instead, your application should call `CGLReleaseContext(_:)` to decrement its reference count.

## Parameters

- `context`: The CGL context to wrap inside the   object.

## See Also

- [init?(format: NSOpenGLPixelFormat, share: NSOpenGLContext?)](nsopenglcontext/init(format:share:).md)
  Returns an OpenGL context object initialized with the specified pixel format information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/init(cglcontextobj:))*