# logicalAnd(_:ordering:)

**Framework**: Synchronization  
**Kind**: method

Perform an atomic logical AND operation and return the old and new value, applying the specified memory ordering.

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
@discardableResult
func logicalAnd(_ operand: Bool, ordering: AtomicUpdateOrdering) -> (oldValue: Bool, newValue: Bool)
```

#### Return Value

A tuple with the old value before the operation a the new value after the operation.

## Parameters

- `operand`: A boolean value.
- `ordering`: The memory ordering to apply on this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomic/logicaland(_:ordering:))*