# init(mtlTexture:options:)

**Framework**: Core Animation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (CARenderer *) rendererWithMTLTexture:(id<MTLTexture>) tex options:(NSDictionary *) dict;
```

## See Also

### Creating a Renderer
- [init(cglContext: UnsafeMutableRawPointer, options: [AnyHashable : Any]?)](./init%28cglcontext,options%29-1l3m2.md)
  Creates and returns a `CARenderer` instance with the render target specified by the Core OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer/init(mtltexture:options:)-1cr0b)*