# CVPixelBufferRelease

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Releases a pixel buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CVPixelBufferRelease(CVPixelBufferRef texture);
```

#### Discussion

This function is equivalent to `CFRelease`, but is `NULL` safe.

## Parameters

- `texture`: The pixel buffer that you want to release.

## See Also

### Retaining and Releasing Pixel Buffers
- [CVPixelBufferRetain](./cvpixelbufferretain.md)
  Retains a pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferrelease)*