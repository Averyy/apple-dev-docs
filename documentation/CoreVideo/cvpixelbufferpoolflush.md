# CVPixelBufferPoolFlush(_:_:)

**Framework**: Core Video  
**Kind**: func

Frees pixel buffers from the pool based on the options that you specify.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func CVPixelBufferPoolFlush(_ pool: CVPixelBufferPool, _ options: CVPixelBufferPoolFlushFlags)
```

## Parameters

- `pool`: The pixel buffer pool to free.
- `options`: Set to   to free all unused buffers regardless of their age. Pass an empty set to free only all aged-out buffers, or set it to   to free all unused buffers regardless of age.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflush(_:_:))*