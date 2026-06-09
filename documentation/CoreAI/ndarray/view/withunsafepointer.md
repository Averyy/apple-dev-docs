# withUnsafePointer(_:)

**Framework**: Core AI  
**Kind**: method

Invokes the provided closure with the backing data and memory layout of this view.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withUnsafePointer<R, E>(_ body: (UnsafePointer<Element>, Span<Int>, Span<Int>) throws(E) -> R) throws(E) -> R where E : Error
```

#### Return Value

The value returned by the closure.

#### Discussion

- body: The closure to be invoked with a pointer to the first element, as well as shape and strides of the view.

> **Note**: This function is intended for situations where you may not be working with contiguous layouts, and as such cannot use `contiguousElements`. You are responsible for reading the `strides` passed in when indexing the backing data. If the view has an [`interleaveLayout`](ndarray/view/interleavelayout.md), the strides for that dimension are block strides and must be interpreted accordingly — see [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view/withunsafepointer(_:))*