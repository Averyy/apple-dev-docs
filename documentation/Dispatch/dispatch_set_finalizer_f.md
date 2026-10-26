# dispatch_set_finalizer_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Sets the finalizer function for a dispatch object.

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
extern void dispatch_set_finalizer_f(dispatch_object_t object, dispatch_function_t finalizer);
```

#### Discussion

The finalizer for a  dispatch object is invoked on that object’s target queue after all references to the object are released. The application can use the finalizer to release any resources associated with the object, such as the object’s application-defined context. The context parameter passed to the finalizer function is the current context of the dispatch object at the time the finalizer call is made. The finalizer is not called if the application-defined context is `NULL`.

## Parameters

- `object`: The dispatch object to modify. This parameter cannot be `NULL`.
- `finalizer`: The finalizer function pointer.

## See Also

### Managing Memory
- [dispatch_retain](./dispatch_retain.md)
  Increments the reference count (the retain count) of a dispatch object.
- [dispatch_release](./dispatch_release.md)
  Decrements the reference count (the retain count) of a dispatch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_set_finalizer_f)*