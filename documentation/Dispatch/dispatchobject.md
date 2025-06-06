# DispatchObject

**Framework**: Dispatch  
**Kind**: class

The base class for most dispatch types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class DispatchObject
```

#### Overview

There are many types of dispatch objects, including [`DispatchQueue`](dispatchqueue.md), [`DispatchGroup`](dispatchgroup.md), and [`DispatchSource`](dispatchsource.md). The base dispatch object interfaces allow you to manage memory, pause and resume execution, define object context, log task data, and more.

## Topics

### Activating, Suspending, and Resuming
- [func activate()](dispatchobject/activate.md)
  Activates the dispatch object.
- [func resume()](dispatchobject/resume.md)
  Resumes the invocation of block objects on a dispatch object.
- [func suspend()](dispatchobject/suspend.md)
  Suspends the invocation of block objects on a dispatch object.
### Changing the Assigned Target Queue
- [func setTarget(queue: dispatch_queue_t?)](dispatchobject/settarget(queue:).md)
  Specifies the dispatch queue on which to perform work associated with the current object.

## Relationships

### Inherits From
- [OS_object](../os/OS_object.md)
### Inherited By
- [DispatchGroup](dispatchgroup.md)
- [DispatchIO](dispatchio.md)
- [DispatchQueue](dispatchqueue.md)
- [DispatchSemaphore](dispatchsemaphore.md)
- [DispatchSource](dispatchsource.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum DispatchPredicate](dispatchpredicate.md)
  Logical conditions to evaluate within a given execution context.
- [func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)](dispatchprecondition(condition:).md)
  Checks a dispatch condition necessary for further execution.
- [Dispatch Objects](dispatch-objects.md)
  The basic behaviors supported by all dispatch types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchobject)*