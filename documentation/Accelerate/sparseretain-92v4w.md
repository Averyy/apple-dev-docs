# SparseRetain(_:)

**Framework**: Accelerate  
**Kind**: func

Increase reference count on a numeric factorization object, returning a copy.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseRetain(_ NumericFactor: SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float
```

#### Return Value

A copy of NumericFactor.

## Parameters

- `NumericFactor`: The symbolic factorization to increase the underlying   reference count of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseretain(_:)-92v4w)*