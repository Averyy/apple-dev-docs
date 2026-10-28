# copyAttributesFromContext:withMask:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Copies selected groups of state variables to the OpenGL context.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (void) copyAttributesFromContext:(NSOpenGLContext *) context withMask:(GLbitfield) mask;
```

## Discussion

Not all values for OpenGL states can be copied. For example, the pixel pack and unpack state, render mode state, and select and feedback state are not copied. The state that can be copied is exactly the state that is manipulated by the OpenGL call `glPushAttrib`.

## Parameters

- `context`: The OpenGL graphics context containing the desired state variables.
- `mask`: A bitfield containing a bitwise OR of the same symbolic names that are passed to the OpenGL call `glPushAttrib`. The single symbolic constant `GL_ALL_ATTRIB_BITS` can be used to copy the maximum possible portion of the rendering state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/copyattributesfromcontext:withmask:)*