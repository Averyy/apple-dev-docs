# init(format:share:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns an OpenGL context object initialized with the specified pixel format information.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
init?(format: NSOpenGLPixelFormat, share: NSOpenGLContext?)
```

```objc
- (instancetype) initWithFormat:(NSOpenGLPixelFormat *) format shareContext:(NSOpenGLContext *) share;
```

## Return Value

An `NSOpenGLContext` object initialized with the specified parameters, or `nil` if the object could not be created.

## Discussion

If the parameters contain invalid information, this method returns `nil`. This may happen if one of the following situations occurs:

- The `format` parameter is `nil` or contains an invalid pixel format.
- The `share` parameter is not `nil` and contains an invalid context.
- The `share` parameter contains a context with a pixel format that is incompatible with the one in `format`.

Pixel formats are incompatible if they use different renderers; this can happen if, for example, one format required an accumulation buffer that could only be provided by the software renderer, and the other format did not.

## Parameters

- `format`: The pixel format to request for the OpenGL graphics context.
- `share`: Another OpenGL graphics context whose texture namespace and display lists you want to share with the receiver. If you do not want to share those features with another graphics context, you may pass `nil` for this parameter.

## See Also

### Creating Contexts
- [init?(cglContextObj: CGLContextObj)](./init%28cglcontextobj%29-30lqr.md)
  Initializes and returns an OpenGL context object using an existing CGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/init(format:share:))*