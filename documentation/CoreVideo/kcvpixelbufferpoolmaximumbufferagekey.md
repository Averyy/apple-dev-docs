# kCVPixelBufferPoolMaximumBufferAgeKey

**Framework**: Core Video  
**Kind**: var

The key you use to set the maximum allowable age for a buffer in the pixel buffer pool.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCVPixelBufferPoolMaximumBufferAgeKey: CFString
```

#### Discussion

This value for this key is of type [`CFAbsoluteTime`](https://developer.apple.com/documentation/CoreFoundation/CFAbsoluteTime).

## See Also

- [let kCVPixelBufferPoolMinimumBufferCountKey: CFString](kcvpixelbufferpoolminimumbuffercountkey.md)
  The minimum number of buffers allowed in the pixel buffer pool.
- [let kCVPixelBufferPoolAllocationThresholdKey: CFString](kcvpixelbufferpoolallocationthresholdkey.md)
  The key you use to set the auxiliary attributes dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolmaximumbufferagekey)*