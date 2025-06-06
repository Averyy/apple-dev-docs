# kCVReturnInvalidPoolAttributes

**Framework**: Core Video  
**Kind**: var

A buffer pool cannot be created with the specified attributes.

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
var kCVReturnInvalidPoolAttributes: CVReturn { get }
```

## See Also

- [var kCVReturnRetry: CVReturn](kcvreturnretry.md)
  A scan hasn’t completely traversed the `CVBufferPool` due to a concurrent operation.
- [var kCVReturnPoolAllocationFailed: CVReturn](kcvreturnpoolallocationfailed.md)
  Allocation for a buffer pool failed, most likely due to a lack of resources. Check to make sure your parameters are in range.
- [var kCVReturnWouldExceedAllocationThreshold: CVReturn](kcvreturnwouldexceedallocationthreshold.md)
  Allocation for a pixel buffer failed because the threshold value set for the [`kCVPixelBufferPoolAllocationThresholdKey`](kcvpixelbufferpoolallocationthresholdkey.md) key in the [`CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_:_:_:_:)`](cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:).md) function would be surpassed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvreturninvalidpoolattributes)*