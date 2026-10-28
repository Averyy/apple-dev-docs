# Dispatch Objects

**Framework**: Dispatch  
**Role**: API Collection

The basic behaviors supported by all dispatch types.

## Overview

There are many types of dispatch objects, including [`dispatch_queue_t`](./dispatch_queue_t.md), [`dispatch_group_t`](./dispatch_group_t.md), and [`dispatch_source_t`](./dispatch_source_t.md). The base dispatch object interfaces allow you to manage memory, pause and resume execution, define object context, log task data, and more.

By default, dispatch objects are declared as Objective-C types when you build them with an Objective-C compiler. This behavior lets you adopt ARC and enable memory leak checks by the static analyzer. It also lets you add your objects to Cocoa collections.

## Topics

### Activating, Suspending, and Resuming the Object
- [func activate()](./dispatchobject/activate%28%29.md)
  Activates the dispatch object.
- [func suspend()](./dispatchobject/suspend%28%29.md)
  Suspends the invocation of block objects on a dispatch object.
- [func resume()](./dispatchobject/resume%28%29.md)
  Resumes the invocation of block objects on a dispatch object.
- [typealias dispatch_object_t](./dispatch_object_t.md)
  A dispatch object.
### Changing the Assigned Target Queue
- [func setTarget(queue: dispatch_queue_t?)](./dispatchobject/settarget%28queue%29.md)
  Specifies the dispatch queue on which to perform work associated with the current object.
### Updating Contextual Data
- [dispatch_get_context](./dispatch_get_context.md)
  Returns the application-defined context of an object.
- [dispatch_set_context](./dispatch_set_context.md)
  Associates an application-defined context with the object.
### Managing Memory
- [dispatch_retain](./dispatch_retain.md)
  Increments the reference count (the retain count) of a dispatch object.
- [dispatch_release](./dispatch_release.md)
  Decrements the reference count (the retain count) of a dispatch object.
- [dispatch_set_finalizer_f](./dispatch_set_finalizer_f.md)
  Sets the finalizer function for a dispatch object.
### Introspecting a Dispatch Object
- [dispatch_introspection_hook_queue_create](./dispatch_introspection_hook_queue_create.md)
- [dispatch_introspection_hook_queue_destroy](./dispatch_introspection_hook_queue_destroy.md)
- [dispatch_introspection_hook_queue_item_enqueue](./dispatch_introspection_hook_queue_item_enqueue.md)
- [dispatch_introspection_hook_queue_item_dequeue](./dispatch_introspection_hook_queue_item_dequeue.md)
- [dispatch_introspection_hook_queue_callout_begin](./dispatch_introspection_hook_queue_callout_begin.md)
- [dispatch_introspection_hook_queue_callout_end](./dispatch_introspection_hook_queue_callout_end.md)
- [dispatch_introspection_hook_queue_item_complete](./dispatch_introspection_hook_queue_item_complete.md)

## See Also

### Dispatch Objects
- [class DispatchObject](./dispatchobject.md)
  The base class for most dispatch types.
- [enum DispatchPredicate](./dispatchpredicate.md)
  Logical conditions to evaluate within a given execution context.
- [func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)](./dispatchprecondition%28condition%29.md)
  Checks a dispatch condition necessary for further execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-objects)*