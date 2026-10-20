# constant(_:dataType:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Creates a constant operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func constant(_ scalar: Double, dataType: MPSDataType) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) constantWithScalar:(double) scalar dataType:(MPSDataType) dataType;
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `scalar`: The scalar value to fill the entire tensor values with.
- `dataType`: The dataType of the constant tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/constant(_:datatype:))*