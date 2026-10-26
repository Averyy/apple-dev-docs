# getOpenGLBufferContext:pixelFormat:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.5+ - Deprecated in 10.9

## Declaration

```objc
- (void) getOpenGLBufferContext:(CGLContextObj*) contextOut pixelFormat:(CGLPixelFormatObj*) pixelFormatOut;
```

#### Discussion

This method is optional. Called once after setVideoDataSource:, if implemented.

## Parameters

- `contextOut`: The OpenGL context to be used for the CVOpenGLBufferRef instances passed to renderIntoOpenGLBuffer:onScreen:forTime:.
- `pixelFormatOut`: The OpenGL pixel format to be used for the CVOpenGLBufferRef instances passed to renderIntoOpenGLBuffer:onScreen:forTime:.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/getopenglbuffercontext:pixelformat:)*