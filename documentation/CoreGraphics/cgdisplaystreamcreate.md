# CGDisplayStreamCreate

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

## Declaration

```c
extern CGDisplayStreamRefCGDisplayStreamCreate(CGDirectDisplayID display, size_t outputWidth, size_t outputHeight, int32_t pixelFormat, CFDictionaryRef properties, CGDisplayStreamFrameAvailableHandler handler);
```

## Return Value

The new CGDisplayStream object.

## Discussion

Creates a new CGDisplayStream intended to be used with a CFRunLoop

This function creates a new CGDisplayStream that is to be used to get a stream of frame updates from a particular display.

‘BGRA’ Packed Little Endian ARGB8888 ‘l10r’ Packed Little Endian ARGB2101010 ‘420v’ 2-plane “video” range YCbCr 4:2:0 ‘420f’ 2-plane “full” range YCbCr 4:2:0

## Parameters

- `display`: The CGDirectDisplayID to use as the source for generated frames
- `outputWidth`: The output width (in pixels, not points) of the frames to be generated.  Must not be zero.
- `outputHeight`: The output height (in pixels, not points) of the frames to be generated.  Must not be zero.
- `pixelFormat`: The desired CoreVideo/CoreMedia-style pixel format of the output IOSurfaces.  The currently supported values are:
- `properties`: Any optional properties of the CGDisplayStream
- `handler`: A block that will be called for frame deliver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamcreate)*