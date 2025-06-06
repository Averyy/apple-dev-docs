# wrappingAdd(_:ordering:)

**Framework**: Synchronization  
**Kind**: method

Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.

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
func wrappingAdd(_ operand: UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)
```

#### Return Value

A tuple containing the original value before the operation and the new value after the operation.

#### Discussion

> **Note**: This operation silently wraps around on overflow, like the `&+` operator does on `UInt8` values.

This operation silently wraps around on overflow, like the `&+` operator does on `UInt8` values.

## Parameters

- `operand`: An integer value.
- `ordering`: The memory ordering to apply on this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomic/wrappingadd(_:ordering:)-ussb)*