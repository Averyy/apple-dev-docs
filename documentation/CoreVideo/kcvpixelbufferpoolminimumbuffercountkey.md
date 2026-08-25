# kCVPixelBufferPoolMinimumBufferCountKey

**Framework**: Core Video  
**Kind**: var

The key that sets the minimum number of pixel buffers in the pool.

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
let kCVPixelBufferPoolMinimumBufferCountKey: CFString
```

#### Discussion

Include this key in the pool attributes dictionary you pass to [`CVPixelBufferPoolCreate(_:_:_:_:)`](cvpixelbufferpoolcreate(_:_:_:_:).md).

## See Also

- [let kCVPixelBufferPoolMaximumBufferAgeKey: CFString](kcvpixelbufferpoolmaximumbufferagekey.md)
  The key that sets how long the pool keeps an unused buffer before it ages out.
- [let kCVPixelBufferPoolAllocationThresholdKey: CFString](kcvpixelbufferpoolallocationthresholdkey.md)
  The key that limits the number of pixel buffers the pool allocates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolminimumbuffercountkey)*