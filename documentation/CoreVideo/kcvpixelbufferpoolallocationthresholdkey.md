# kCVPixelBufferPoolAllocationThresholdKey

**Framework**: Core Video  
**Kind**: var

The key you use to set the auxiliary attributes dictionary.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCVPixelBufferPoolAllocationThresholdKey: CFString
```

#### Discussion

Use this key to set `auxAttributes` in [`CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_:_:_:_:)`](cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:).md).

The value for this key specifies that the system shouldn’t allocate a new pixel buffer if the pool already holds at least the specified number of allocated pixel buffers. This key doesn’t prevent the system from recycling allocated buffers. If this key causes [`CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_:_:_:_:)`](cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:).md) to fail, it returns the [`kCVReturnWouldExceedAllocationThreshold`](kcvreturnwouldexceedallocationthreshold.md) result code.

## See Also

- [let kCVPixelBufferPoolMinimumBufferCountKey: CFString](kcvpixelbufferpoolminimumbuffercountkey.md)
  The minimum number of buffers allowed in the pixel buffer pool.
- [let kCVPixelBufferPoolMaximumBufferAgeKey: CFString](kcvpixelbufferpoolmaximumbufferagekey.md)
  The key you use to set the maximum allowable age for a buffer in the pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolallocationthresholdkey)*