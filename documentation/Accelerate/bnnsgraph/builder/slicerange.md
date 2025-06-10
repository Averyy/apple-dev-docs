# BNNSGraph.Builder.SliceRange

**Framework**: Accelerate  
**Kind**: struct

A structure that represents a range.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct SliceRange
```

#### Overview

You can use standard Swift range operators to specify the range in slice operation. However, the `BNNSGraph.Builder.SliceRange` structure provides additional functionality:

- You can specify a `stop` that’s less that the `start` value.
- You can supply negative `startIndex` and `endIndex` values to indicate the index is relative to the end of sequence
- You can specify the stride.
- You can specify an `UnboundedRange` with the `fillAll` constant.

For example, the following code shows a slice operation that selects dimensions using a `SliceRange`, a Swift range, and an integer.

```None
    let slice = src[BNNSGraph.Builder.SliceRange(startIndex: 1,
                                                 endIndex: -1),
                    5 ... 20,
                    3]
```

## Topics

### Initializers
- [init(startIndex: Int, endIndex: Int)](bnnsgraph/builder/slicerange/init(startindex:endindex:).md)
  Returns a new slice range structure.
### Instance Properties
- [let endIndex: Int](bnnsgraph/builder/slicerange/endindex.md)
- [let startIndex: Int](bnnsgraph/builder/slicerange/startindex.md)
### Type Properties
- [static let fillAll: BNNSGraph.Builder.SliceRange](bnnsgraph/builder/slicerange/fillall.md)
  The same as the ellipsis literal `...` used to indicate unspecified dimensions of the tensor.

## Relationships

### Conforms To
- [BNNSGraph.Builder.SliceIndex](bnnsgraph/builder/sliceindex.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/slicerange)*