# QCPlugInTextureReleaseCallback

**Framework**: Quartz  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
typealias QCPlugInTextureReleaseCallback = (CGLContextObj?, GLuint, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct _CGLContextObject *, unsigned int, void *) QCPlugInTextureReleaseCallback;
```

## See Also

### Data Types
- [typealias QCPlugInBufferReleaseCallback](./qcpluginbufferreleasecallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugintexturereleasecallback)*