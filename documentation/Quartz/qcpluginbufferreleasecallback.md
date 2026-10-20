# QCPlugInBufferReleaseCallback

**Framework**: Quartz  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
typealias QCPlugInBufferReleaseCallback = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(const void *, void *) QCPlugInBufferReleaseCallback;
```

## See Also

### Data Types
- [typealias QCPlugInTextureReleaseCallback](./qcplugintexturereleasecallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginbufferreleasecallback)*