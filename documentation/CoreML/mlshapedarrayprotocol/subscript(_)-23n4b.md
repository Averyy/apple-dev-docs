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
subscript(sliceRange: Range<Int>) -> MLShapedArraySlice<Self.Scalar> { get set }
```

#### Overview

This overrides the method from Collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(_:)-23n4b)*