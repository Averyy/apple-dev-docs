# BNNSGraph.Builder.SliceRange

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that represents a range.

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
struct SliceRange
```

## Overview

You can use standard Swift range operators to specify the range in slice operation. However, the `BNNSGraph.Builder.SliceRange` structure provides additional functionality:

- You can specify a `stop` that’s less that the `start` value.
- You can supply negative `startIndex` and `endIndex` values to indicate the index is relative to the end of sequence
- You can specify the stride.
- You can specify an `UnboundedRange` with the `fillAll` constant.

For example, the following code shows a slice operation that selects dimensions using a `SliceRange`, a Swift range, and an integer.

```
    let slice = src[BNNSGraph.Builder.SliceRange(startIndex: 1,
                                                 endIndex: -1),
                    5 ... 20,
                    3]
```

## Topics

### Initializers
- [init(startIndex: Int, endIndex: Int)](./slicerange/init%28startindex,endindex%29.md)
  Returns a new slice range structure.
### Instance Properties
- [let endIndex: Int](./slicerange/endindex.md)
- [let startIndex: Int](./slicerange/startindex.md)
### Type Properties
- [static let fillAll: BNNSGraph.Builder.SliceRange](./slicerange/fillall.md)
  The same as the ellipsis literal `...` used to indicate unspecified dimensions of the tensor.

## Relationships

### Conforms To
- [BNNSGraph.Builder.SliceIndex](./sliceindex.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/slicerange)*