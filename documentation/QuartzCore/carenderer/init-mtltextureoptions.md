# init(mtlTexture:options:)

**Framework**: Core Animation  
**Kind**: init

Creates a layer renderer from a Metal texture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(mtlTexture tex: any MTLTexture, options dict: [AnyHashable : Any]? = nil)
```

## See Also

- [init(cglContext: UnsafeMutableRawPointer, options: [AnyHashable : Any]?)](carenderer/init(cglcontext:options:).md)
  Creates and returns a `CARenderer` instance with the render target specified by the Core OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer/init(mtltexture:options:))*