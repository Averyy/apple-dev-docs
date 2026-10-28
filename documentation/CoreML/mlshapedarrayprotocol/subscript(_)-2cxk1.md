# subscript(_:)

**Framework**: Core ML  
**Kind**: subscript  
**Role**: Instance Subscript

A slice of the shaped array for the selected leading axes.

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
subscript(indices: Int...) -> MLShapedArraySlice<Self.Scalar> { get set }
```

## Overview

The slice has a rank of `self.rank - indices.count`. For example, given a shaped array `m` with the shape being `[3, 3]`, `m[1]` returns a slice of shape `[3]` with the contents labeld as `x` below.

```
 O  O  O
 x  x  x
 O  O  O
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(_:)-2cxk1)*