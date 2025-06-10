# allocationThreshold

**Framework**: Core Video  
**Kind**: property

A new pixel buffer will not be allocated if the pool already has this many or more pixel buffers allocated. This does not prevent already-allocated buffers from being recycled. If this causes allocation failure, then `CVMutablePixelBuffer/Pool/mutablePixelBuffer(allocationThreshold:)` throws [`wouldExceedAllocationThreshold`](cverror/wouldexceedallocationthreshold.md).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var allocationThreshold: Int?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/allocationattributes/allocationthreshold)*