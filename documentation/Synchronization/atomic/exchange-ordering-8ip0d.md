# exchange(_:ordering:)

**Framework**: Synchronization  
**Kind**: method

Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.

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
func exchange(_ desired: consuming Value, ordering: AtomicUpdateOrdering) -> Value
```

#### Return Value

The original value.

## Parameters

- `desired`: The desired new value.
- `ordering`: The memory ordering to apply on this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomic/exchange(_:ordering:)-8ip0d)*