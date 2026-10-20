# DispatchPredicate.onQueue(_:)

**Framework**: Dispatch  
**Kind**: case  
**Role**: Case

A predicate that indicates the evaluated context is the associated dispatch queue.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS
- watchOS 3.0+

## Declaration

```swift
case onQueue(DispatchQueue)
```

## See Also

### Predicates
- [DispatchPredicate.onQueueAsBarrier(_:)](./onqueueasbarrier%28_%29.md)
  A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.
- [DispatchPredicate.notOnQueue(_:)](./notonqueue%28_%29.md)
  A predicate that indicates the evaluated context is not the associated dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchpredicate/onqueue(_:))*