# CVPixelBufferPoolRetain

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retains the pixel buffer pool that you specify.

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
extern CVPixelBufferPoolRefCVPixelBufferPoolRetain(CVPixelBufferPoolRef pixelBufferPool);
```

#### Return Value

The same pixel buffer pool that you specified.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except it’s `NULL` safe.

## Parameters

- `pixelBufferPool`: The pixel buffer pool that you want to retain.

## See Also

### Retaining and releasing pools
- [CVPixelBufferPoolRelease](./cvpixelbufferpoolrelease.md)
  Releases a pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolretain)*