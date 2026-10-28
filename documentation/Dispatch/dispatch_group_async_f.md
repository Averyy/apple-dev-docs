# dispatch_group_async_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits an application-defined function to a dispatch queue and associates it with the specified dispatch group.

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
extern void dispatch_group_async_f(dispatch_group_t group, dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Discussion

Submits an application-defined function to a dispatch queue and associates it with the given dispatch group. The dispatch group can be used to wait for the completion of the application-defined functions it references.

## Parameters

- `group`: A dispatch group to associate the submitted function with. The group is retained by the system until the application-defined function has run to completion. This parameter cannot be `NULL`.
- `queue`: The dispatch queue to which the function is submitted for asynchronous invocation. The queue is retained by the system until the application-defined function has run to completion. This parameter cannot be `NULL`.
- `context`: The application-defined context parameter to pass to the application-defined function.
- `work`: The application-defined function to invoke on the target queue. The first parameter passed to this function is the value in the `context` parameter.

## See Also

### Adding Work to the Group
- [dispatch_group_async](./dispatch_group_async.md)
  Schedules a block asynchronously for execution and simultaneously associates it with the specified dispatch group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_group_async_f)*