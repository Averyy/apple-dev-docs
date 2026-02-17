# add(_:ordering:)

**Framework**: Synchronization  
**Kind**: method

Perform an atomic add operation and return the old and new value, applying the specified memory ordering.

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
func add(_ operand: UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)
```

#### Return Value

A tuple containing the original value before the operation and the new value after the operation.

#### Discussion

> **Note**: This operation checks for overflow at runtime and will trap if an overflow does occur. In `-Ounchecked` builds, overflow checking is not performed. The need to check for overflow means that this operation is typically compiled into a compare-exchange loop. For use cases that require a direct atomic addition, see the `wrappingAdd` operation: it avoids the loop, but in exchange it allows silent wraps on overflow.

## Parameters

- `operand`: An integer value.
- `ordering`: The memory ordering to apply on this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomic/add(_:ordering:)-4dpjd)*