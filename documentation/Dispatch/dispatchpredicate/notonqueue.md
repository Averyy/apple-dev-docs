# DispatchPredicate.notOnQueue(_:)

**Framework**: Dispatch  
**Kind**: case

A predicate that indicates the evaluated context is not the associated dispatch queue.

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
case notOnQueue(DispatchQueue)
```

## See Also

- [DispatchPredicate.onQueue(_:)](dispatchpredicate/onqueue(_:).md)
  A predicate that indicates the evaluated context is the associated dispatch queue.
- [DispatchPredicate.onQueueAsBarrier(_:)](dispatchpredicate/onqueueasbarrier(_:).md)
  A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchpredicate/notonqueue(_:))*