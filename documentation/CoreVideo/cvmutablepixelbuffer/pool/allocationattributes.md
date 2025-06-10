# CVMutablePixelBuffer.Pool.AllocationAttributes

**Framework**: Core Video  
**Kind**: struct

Controls how new pixel buffers are allocated when `CVMutablePixelBuffer/Pool/mutablePixelBuffer(with:)` is called.

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
struct AllocationAttributes
```

## Topics

### Initializers
- [init(allocationThreshold: Int?)](cvmutablepixelbuffer/pool/allocationattributes/init(allocationthreshold:).md)
### Instance Properties
- [var allocationThreshold: Int?](cvmutablepixelbuffer/pool/allocationattributes/allocationthreshold.md)
  A new pixel buffer will not be allocated if the pool already has this many or more pixel buffers allocated. This does not prevent already-allocated buffers from being recycled. If this causes allocation failure, then `CVMutablePixelBuffer/Pool/mutablePixelBuffer(allocationThreshold:)` throws [`wouldExceedAllocationThreshold`](cverror/wouldexceedallocationthreshold.md).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/allocationattributes)*