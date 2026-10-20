# min(_:ordering:)

**Framework**: Synchronization  
**Kind**: method

Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.

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
func min(_ operand: UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)
```

#### Return Value

A tuple containing the original value before the operation and the new value after the operation.

## Parameters

- `operand`: An integer value.
- `ordering`: The memory ordering to apply on this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomic/min(_:ordering:)-8k42m)*