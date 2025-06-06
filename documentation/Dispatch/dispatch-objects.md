# Dispatch Objects

**Framework**: Dispatch

The basic behaviors supported by all dispatch types.

#### Overview

There are many types of dispatch objects, including [`dispatch_queue_t`](dispatch_queue_t.md), [`dispatch_group_t`](dispatch_group_t.md), and [`dispatch_source_t`](dispatch_source_t.md). The base dispatch object interfaces allow you to manage memory, pause and resume execution, define object context, log task data, and more.

By default, dispatch objects are declared as Objective-C types when you build them with an Objective-C compiler. This behavior lets you adopt ARC and enable memory leak checks by the static analyzer. It also lets you add your objects to Cocoa collections.

## Topics

### Activating, Suspending, and Resuming the Object
- [func activate()](dispatchobject/activate.md)
  Activates the dispatch object.
- [func suspend()](dispatchobject/suspend.md)
  Suspends the invocation of block objects on a dispatch object.
- [func resume()](dispatchobject/resume.md)
  Resumes the invocation of block objects on a dispatch object.
- [typealias dispatch_object_t](dispatch_object_t.md)
  A dispatch object.
### Changing the Assigned Target Queue
- [func setTarget(queue: dispatch_queue_t?)](dispatchobject/settarget(queue:).md)
  Specifies the dispatch queue on which to perform work associated with the current object.

## See Also

- [class DispatchObject](dispatchobject.md)
  The base class for most dispatch types.
- [enum DispatchPredicate](dispatchpredicate.md)
  Logical conditions to evaluate within a given execution context.
- [func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)](dispatchprecondition(condition:).md)
  Checks a dispatch condition necessary for further execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-objects)*