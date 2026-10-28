# DispatchPredicate

**Framework**: Dispatch  
**Kind**: enum  
**Role**: Enumeration

Logical conditions to evaluate within a given execution context.

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
enum DispatchPredicate
```

## Overview

You use dispatch predicates with the [`dispatchPrecondition(condition:)`](./dispatchprecondition%28condition%29.md) method.

## Topics

### Predicates
- [DispatchPredicate.onQueue(_:)](./dispatchpredicate/onqueue%28_%29.md)
  A predicate that indicates the evaluated context is the associated dispatch queue.
- [DispatchPredicate.onQueueAsBarrier(_:)](./dispatchpredicate/onqueueasbarrier%28_%29.md)
  A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.
- [DispatchPredicate.notOnQueue(_:)](./dispatchpredicate/notonqueue%28_%29.md)
  A predicate that indicates the evaluated context is not the associated dispatch queue.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Dispatch Objects
- [class DispatchObject](./dispatchobject.md)
  The base class for most dispatch types.
- [func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)](./dispatchprecondition%28condition%29.md)
  Checks a dispatch condition necessary for further execution.
- [Dispatch Objects](./dispatch-objects.md)
  The basic behaviors supported by all dispatch types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchpredicate)*