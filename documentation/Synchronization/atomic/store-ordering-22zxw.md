# store(_:ordering:)

**Framework**: Synchronization  
**Kind**: method

Atomically sets the current value to `desired`, applying the specified memory ordering.

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
func store(_ desired: consuming Value, ordering: AtomicStoreOrdering)
```

## Parameters

- `desired`: The desired new value.
- `ordering`: The memory ordering to apply on this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomic/store(_:ordering:)-22zxw)*