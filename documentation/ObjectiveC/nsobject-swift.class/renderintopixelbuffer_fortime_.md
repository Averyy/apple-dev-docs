# renderIntoPixelBuffer:forTime:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.5+ - Deprecated in 10.9

## Declaration

```objc
- (BOOL) renderIntoPixelBuffer:(CVPixelBufferRef) buffer forTime:(CVTimeStamp *) timeStamp;
```

## Return Value

Return YES if the buffer was successfully filled with new frame data. Return NO if nothing has changed or an error was encountered.

## Discussion

Called for each frame to be sent to Messages. This method will not be called on the main thread.

## Parameters

- `buffer`: The pixel buffer to fill. The dimensions can vary: use CVPixelBufferGetWidth() and CVPixelBufferGetHeight() every time.
- `timeStamp`: The frame time for which the buffer should be rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/renderintopixelbuffer:fortime:)*