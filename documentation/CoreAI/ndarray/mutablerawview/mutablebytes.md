# mutableBytes

**Framework**: Core AI  
**Kind**: property

A mutable span over the backing bytes of this tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
var mutableBytes: MutableRawSpan { mutating get }
```

#### Discussion

> **Note**: When accessing the bytes directly you are responsible for interpreting the layout of the tensor according to the `strides` property of this view. This means you must either ensure the logical elements are contiguous, or dynamically handle nontrivial striding. If the view has an [`interleaveLayout`](ndarray/mutablerawview/interleavelayout.md), the strides for that dimension are block strides and must be interpreted accordingly — see [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview/mutablebytes)*