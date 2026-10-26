# dispatch_retain

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Increments the reference count (the retain count) of a dispatch object.

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
extern void dispatch_retain(dispatch_object_t object);
```

#### Discussion

Calls to this function must be balanced with calls to [`dispatch_release`](./dispatch_release.md). If  multiple subsystems of your application share a dispatch object, each subsystem should call [`dispatch_retain`](./dispatch_retain.md) to register its interest in the object.  The object is deallocated only when all subsystems have released their interest in the dispatch source.

Note that your application does not need to retain or release the global (main and concurrent) dispatch queues.

> ❗ **Important**:  If your app is built with a deployment target of macOS 10.8 and later or iOS v6.0 and later, dispatch queues are typically managed by ARC, so you do not need to retain or release the dispatch queues.
>
> For compatibility with existing code, this behavior is configurable. See `GCD Objects and Automatic Reference Counting` for details.

## Parameters

- `object`: The object to retain. This parameter cannot be `NULL`.

## See Also

### Managing Memory
- [dispatch_release](./dispatch_release.md)
  Decrements the reference count (the retain count) of a dispatch object.
- [dispatch_set_finalizer_f](./dispatch_set_finalizer_f.md)
  Sets the finalizer function for a dispatch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_retain)*