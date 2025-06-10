# init(cglContext:options:)

**Framework**: Core Animation  
**Kind**: init

Creates and returns a `CARenderer` instance with the render target specified by the Core OpenGL context.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
init(cglContext ctx: UnsafeMutableRawPointer, options dict: [AnyHashable : Any]? = nil)
```

#### Return Value

A new instance of `CARenderer` that will use `ctx` as the render target.

## Parameters

- `ctx`: A Core OpenGL render context that is used as the render target.
- `dict`: A dictionary of optional parameters.

## See Also

- [init(mtlTexture: any MTLTexture, options: [AnyHashable : Any]?)](carenderer/init(mtltexture:options:).md)
  Creates a layer renderer from a Metal texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer/init(cglcontext:options:))*