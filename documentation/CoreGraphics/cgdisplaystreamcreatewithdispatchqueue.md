# CGDisplayStreamCreateWithDispatchQueue

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

## Declaration

```c
extern CGDisplayStreamRefCGDisplayStreamCreateWithDispatchQueue(CGDirectDisplayID display, size_t outputWidth, size_t outputHeight, int32_t pixelFormat, CFDictionaryRef properties, dispatch_queue_t queue, CGDisplayStreamFrameAvailableHandler handler);
```

## Return Value

The new CGDisplayStream object.

## Discussion

Creates a new CGDisplayStream intended to be serviced by a block handler

This function creates a new CGDisplayStream that is to be used to get a stream of frame updates from a particular display.

## Parameters

- `display`: The CGDirectDisplayID to use as the source for generated frames
- `outputWidth`: The output width (in pixels, not points) of the frames to be generated.  Must not be zero.
- `outputHeight`: The output height (in pixels, not points) of the frames to be generated.  Must not be zero.
- `pixelFormat`: The desired CoreVideo/CoreMedia-style pixel format of the output IOSurfaces
- `properties`: Any optional properties of the CGDisplayStream
- `queue`: The dispatch_queue_t that will be used to invoke the callback handler.
- `handler`: A block that will be called for frame deliver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamcreatewithdispatchqueue)*