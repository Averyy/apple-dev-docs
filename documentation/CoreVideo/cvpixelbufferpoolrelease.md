# CVPixelBufferPoolRelease

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Releases a pixel buffer pool.

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
extern void CVPixelBufferPoolRelease(CVPixelBufferPoolRef pixelBufferPool);
```

## Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except it’s `NULL` safe.

## Parameters

- `pixelBufferPool`: The pixel buffer pool that you want to release.

## See Also

### Retaining and releasing pools
- [CVPixelBufferPoolRetain](./cvpixelbufferpoolretain.md)
  Retains the pixel buffer pool that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolrelease)*