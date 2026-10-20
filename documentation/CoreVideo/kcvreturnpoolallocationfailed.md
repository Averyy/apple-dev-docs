# kCVReturnPoolAllocationFailed

**Framework**: Core Video  
**Kind**: var  
**Role**: Global Variable

Allocation for a buffer pool failed, most likely due to a lack of resources. Check to make sure your parameters are in range.

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
var kCVReturnPoolAllocationFailed: CVReturn { get }
```

```c
kCVReturnPoolAllocationFailed
```

## See Also

### Buffer Pool
- [var kCVReturnRetry: CVReturn](./kcvreturnretry.md)
  A scan hasn’t completely traversed the `CVBufferPool` due to a concurrent operation.
- [var kCVReturnInvalidPoolAttributes: CVReturn](./kcvreturninvalidpoolattributes.md)
  A buffer pool cannot be created with the specified attributes.
- [var kCVReturnWouldExceedAllocationThreshold: CVReturn](./kcvreturnwouldexceedallocationthreshold.md)
  Allocation for a pixel buffer failed because the threshold value set for the [`kCVPixelBufferPoolAllocationThresholdKey`](./kcvpixelbufferpoolallocationthresholdkey.md) key in the [`CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_:_:_:_:)`](./cvpixelbufferpoolcreatepixelbufferwithauxattributes%28_,_,_,_%29.md) function would be surpassed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvreturnpoolallocationfailed)*