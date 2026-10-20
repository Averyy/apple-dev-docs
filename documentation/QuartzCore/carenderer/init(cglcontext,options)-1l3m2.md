# init(cglContext:options:)

**Framework**: Core Animation  
**Kind**: init  
**Role**: Initializer

Creates and returns a `CARenderer` instance with the render target specified by the Core OpenGL context.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init(cglContext ctx: UnsafeMutableRawPointer, options dict: [AnyHashable : Any]? = nil)
```

```objc
+ (CARenderer *) rendererWithCGLContext:(void *) ctx options:(NSDictionary *) dict;
```

#### Return Value

A new instance of `CARenderer` that will use `ctx` as the render target.

## Parameters

- `ctx`: A Core OpenGL render context that is used as the render target.
- `dict`: A dictionary of optional parameters.

## See Also

### Creating a Renderer
- [init(mtlTexture: any MTLTexture, options: [AnyHashable : Any]?)](./init%28mtltexture,options%29-1cr0b.md)
  Creates a layer renderer from a Metal texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer/init(cglcontext:options:)-1l3m2)*