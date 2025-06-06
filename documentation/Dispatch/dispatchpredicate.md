# DispatchPredicate

**Framework**: Dispatch  
**Kind**: enum

Logical conditions to evaluate within a given execution context.

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
enum DispatchPredicate
```

#### Overview

You use dispatch predicates with the [`dispatchPrecondition(condition:)`](dispatchprecondition(condition:).md) method.

## Topics

### Predicates
- [DispatchPredicate.onQueue(_:)](dispatchpredicate/onqueue(_:).md)
  A predicate that indicates the evaluated context is the associated dispatch queue.
- [DispatchPredicate.onQueueAsBarrier(_:)](dispatchpredicate/onqueueasbarrier(_:).md)
  A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.
- [DispatchPredicate.notOnQueue(_:)](dispatchpredicate/notonqueue(_:).md)
  A predicate that indicates the evaluated context is not the associated dispatch queue.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [class DispatchObject](dispatchobject.md)
  The base class for most dispatch types.
- [func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)](dispatchprecondition(condition:).md)
  Checks a dispatch condition necessary for further execution.
- [Dispatch Objects](dispatch-objects.md)
  The basic behaviors supported by all dispatch types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchpredicate)*