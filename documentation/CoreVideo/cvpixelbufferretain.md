# CVPixelBufferRetain

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retains a pixel buffer.

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
extern CVPixelBufferRefCVPixelBufferRetain(CVPixelBufferRef texture);
```

## Return Value

For convenience, the same pixel buffer you want to retain.

## Discussion

This function is equivalent to `CFRetain`, but is `NULL` safe.

## Parameters

- `texture`: The pixel buffer that you want to retain.

## See Also

### Retaining and Releasing Pixel Buffers
- [CVPixelBufferRelease](./cvpixelbufferrelease.md)
  Releases a pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferretain)*