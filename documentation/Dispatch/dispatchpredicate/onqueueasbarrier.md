# DispatchPredicate.onQueueAsBarrier(_:)

**Framework**: Dispatch  
**Kind**: case

A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
case onQueueAsBarrier(DispatchQueue)
```

#### Discussion

For more information about barrier operations, see `[`barrier`](dispatchworkitemflags/barrier.md)`.

## See Also

- [DispatchPredicate.onQueue(_:)](dispatchpredicate/onqueue(_:).md)
  A predicate that indicates the evaluated context is the associated dispatch queue.
- [DispatchPredicate.notOnQueue(_:)](dispatchpredicate/notonqueue(_:).md)
  A predicate that indicates the evaluated context is not the associated dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchpredicate/onqueueasbarrier(_:))*