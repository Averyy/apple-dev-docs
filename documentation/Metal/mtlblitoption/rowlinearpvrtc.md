# rowLinearPVRTC

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

A blit option that copies PVRTC data between a texture and a buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var rowLinearPVRTC: MTLBlitOption { get }
```

```c
MTLBlitOptionRowLinearPVRTC
```

## Discussion

The PowerVR Texture Compression (PVRTC) format arranges blocks linearly in memory in row-major order, similar to other compressed texture formats. You can pass this option to some methods that copy data between a buffer and a texture, including the following:

- [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:options:)`](../mtlblitcommandencoder/copy%28from,sourceoffset,sourcebytesperrow,sourcebytesperimage,sourcesize,to,destinationslice,destinationlevel,destinationorigin,options%29.md)
- [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](../mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationoffset,destinationbytesperrow,destinationbytesperimage,options%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitoption/rowlinearpvrtc)*