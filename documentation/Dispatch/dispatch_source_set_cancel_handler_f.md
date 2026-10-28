# dispatch_source_set_cancel_handler_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Sets the cancellation handler function for the given dispatch source.

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
extern void dispatch_source_set_cancel_handler_f(dispatch_source_t source, dispatch_function_t handler);
```

## Discussion

The cancellation handler (if specified) is submitted to the source’s target queue in response to a call to [`dispatch_source_cancel`](./dispatch_source_cancel.md) when the system has released all references to the source’s underlying handle and the source’s event handler block has returned.

> ❗ **Important**:  To safely close a file descriptor or destroy a Mach port, a cancellation handler is required for the source for that descriptor or port. Closing the descriptor or port before the cancellation handler runs can result in a race condition. If a new descriptor is allocated with the same value as the recently closed descriptor while the source’s event handler is still running, the event handler may read/write data using the wrong descriptor.

## Parameters

- `source`: The dispatch source to modify. This parameter cannot be `NULL`.
- `handler`: The cancellation handler function to submit to the source’s target queue. The context parameter passed to the event handler function is the current context of the dispatch source at the time the handler call is made.

## See Also

### Managing Event Handlers
- [dispatch_source_set_registration_handler_f](./dispatch_source_set_registration_handler_f.md)
  Sets the registration handler function for the given dispatch source.
- [dispatch_source_set_registration_handler](./dispatch_source_set_registration_handler.md)
  Sets the registration handler block for the given dispatch source.
- [dispatch_source_set_event_handler_f](./dispatch_source_set_event_handler_f.md)
  Sets the event handler function for the given dispatch source.
- [dispatch_source_set_event_handler](./dispatch_source_set_event_handler.md)
  Sets the event handler block for the given dispatch source.
- [dispatch_source_set_cancel_handler](./dispatch_source_set_cancel_handler.md)
  Sets the cancellation handler block for the given dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_set_cancel_handler_f)*