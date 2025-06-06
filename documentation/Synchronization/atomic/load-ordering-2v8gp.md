# load(ordering:)

**Framework**: Synchronization  
**Kind**: method

Atomically loads and returns the current value, applying the specified memory ordering.

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
func load(ordering: AtomicLoadOrdering) -> Value
```

#### Return Value

The current value.

## Parameters

- `ordering`: The memory ordering to apply on this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomic/load(ordering:)-2v8gp)*