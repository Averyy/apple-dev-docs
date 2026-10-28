# .>=(_:_:)

**Framework**: Core ML  
**Kind**: op  
**Role**: Operator

Computes element-wise greater than or equal to comparison between two tensors.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func .>= (lhs: MLTensor, rhs: some MLTensorScalar & Numeric) -> MLTensor
```

**Other overloads**:

```swift
static func .>= (lhs: MLTensor, rhs: MLTensor) -> MLTensor
```

## Return Value

A Boolean tensor where each element is true if the left hand side tensor is greater than, or equal, to the corresponding element of the right hand side, and false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/'._=(_:_:)-2zak0)*