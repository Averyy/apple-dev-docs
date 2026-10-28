# subscript(_:)

**Framework**: Core ML  
**Kind**: subscript  
**Role**: Instance Subscript

A slice of the shaped array for the specified ranges.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
subscript(sliceRanges: any MLShapedArrayRangeExpression...) -> MLShapedArraySlice<Self.Scalar> { get set }
```

## Overview

When the range expression array is shorter than the rank, the remaining axes are fully selected. For example, given a shaped array `m` of shape `[2, 3]`, `m[0..<1]` results in a slice with shape `[1, 3]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(_:)-2hc37)*