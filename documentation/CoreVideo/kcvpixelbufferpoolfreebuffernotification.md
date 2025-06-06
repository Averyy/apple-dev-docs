# kCVPixelBufferPoolFreeBufferNotification

**Framework**: Core Video  
**Kind**: var

A notification that the system posts if a buffer becomes available after it fails to create a pixel buffer with auxiliary attributes because it exceeded the threshold you specified.

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
let kCVPixelBufferPoolFreeBufferNotification: CFString
```

#### Discussion

The system posts this notification if a buffer becomes available after the [`CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_:_:_:_:)`](cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:).md) function fails because the system exceeds the threshold you set for the [`kCVPixelBufferPoolAllocationThresholdKey`](kcvpixelbufferpoolallocationthresholdkey.md) key. The system won’t post this notification if you don’t set a value for the [`kCVPixelBufferPoolAllocationThresholdKey`](kcvpixelbufferpoolallocationthresholdkey.md) key for the `auxAttributes` parameter of the [`CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_:_:_:_:)`](cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolfreebuffernotification)*