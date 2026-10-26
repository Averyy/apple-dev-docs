# dispatch_release

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Decrements the reference count (the retain count) of a dispatch object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_release(dispatch_object_t object);
```

#### Discussion

A dispatch object is asynchronously deallocated once all references to it are released (the reference count becomes zero). When your application no longer needs a dispatch object that it has created, it should call this function to release its interest in the object and allow its memory to be deallocated when appropriate. Note that GCD does not guarantee that a given client has the last or only reference to a given object.

> ❗ **Important**:  If your app is built with a deployment target of macOS 10.8 and later or iOS v6.0 and later, dispatch queues are typically managed by ARC, so you do not need to retain or release the dispatch queues.
>
> For compatibility with existing code, this behavior is configurable. See `GCD Objects and Automatic Reference Counting` for details.

Your application does not need to retain or release the global (main and concurrent) dispatch queues; calling this function on global dispatch queues has no effect.

> ❗ **Important**:  It is a programmer error to call this function on an object that is currently suspended, because suspension implies that there is still work to be done. Therefore, always balance calls to [`suspend()`](./dispatchobject/suspend%28%29.md) and [`resume()`](./dispatchobject/resume%28%29.md) so that the dispatch object is fully resumed when the last reference is released. The behavior when releasing the last reference to a dispatch object while it is in a suspended state is undefined.

## Parameters

- `object`: The object to release. This parameter cannot be `NULL`.

## See Also

### Managing Memory
- [dispatch_retain](./dispatch_retain.md)
  Increments the reference count (the retain count) of a dispatch object.
- [dispatch_set_finalizer_f](./dispatch_set_finalizer_f.md)
  Sets the finalizer function for a dispatch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_release)*