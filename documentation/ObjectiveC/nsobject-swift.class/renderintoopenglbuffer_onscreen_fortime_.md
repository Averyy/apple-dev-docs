# renderIntoOpenGLBuffer:onScreen:forTime:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Called for each frame to be sent to Messages. This method will not be called on the main thread.

**Availability**:
- macOS 10.5+ - Deprecated in 10.9

## Declaration

```objc
- (BOOL) renderIntoOpenGLBuffer:(CVOpenGLBufferRef) buffer onScreen:(int *) screenInOut forTime:(CVTimeStamp *) timeStamp;
```

## Return Value

 Return `YES` if the buffer was successfully filled with new frame data. Return `NO` if nothing has changed or an error was encountered.

## Parameters

- `buffer`: The OpenGL buffer to fill. The receiver should call `CVOpenGLBufferAttach()`, then render.
- `screenInOut`: The recommended virtual screen number to pass to `CVOpenGLBufferAttach()` for maximum efficiency. The delegate may use a different screen number, but must write that value back into screenInOut before returning.
- `timeStamp`: The frame time for which the buffer should be rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/renderintoopenglbuffer:onscreen:fortime:)*