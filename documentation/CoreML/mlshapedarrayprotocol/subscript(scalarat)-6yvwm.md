# subscript(scalarAt:)

**Framework**: Core ML  
**Kind**: subscript  
**Role**: Instance Subscript

The scalar value at the indices.

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
subscript(scalarAt indices: Int...) -> Self.Scalar { get set }
```

## Overview

The subscript returns scalar value of the slice pointed by the specified indices. It raises a runtime error if the specified indices is not a scalar.

## Parameters

- `indices`: The indices to a scalar


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(scalarat:)-6yvwm)*