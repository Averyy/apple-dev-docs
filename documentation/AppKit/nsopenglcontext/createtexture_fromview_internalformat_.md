# createTexture:fromView:internalFormat:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new texture from the contents of the specified view.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```objc
- (void) createTexture:(GLenum) target fromView:(NSView *) view internalFormat:(GLenum) format;
```

#### Discussion

The new texture is assigned the identifier in the `target` parameter and is associated with the receiver’s context.

## Parameters

- `target`: The identifier for the new texture.
- `view`: The view to use to generate the texture. This parameter must be either an `NSOpenGLView` object or some other kind of `NSView` object that’s associated with an `NSOpenGLContext` object.
- `format`: The format for the texture, interpreted as a `GLenum` data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/createtexture:fromview:internalformat:)*