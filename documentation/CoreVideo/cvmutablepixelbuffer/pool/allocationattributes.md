# CVMutablePixelBuffer.Pool.AllocationAttributes

**Framework**: Core Video  
**Kind**: struct

Controls how new pixel buffers are allocated when `CVMutablePixelBuffer/Pool/mutablePixelBuffer(with:)` is called.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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