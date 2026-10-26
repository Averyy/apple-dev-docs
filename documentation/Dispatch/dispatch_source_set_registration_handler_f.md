# dispatch_source_set_registration_handler_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Sets the registration handler function for the given dispatch source.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_source_set_registration_handler_f(dispatch_source_t source, dispatch_function_t handler);
```

#### Discussion

The registration handler (if specified) is submitted to the source’s target queue as soon as the source has been fully set up and is ready to start delivering events. The set up of a dispatch source’s underlying event-delivery mechanism occurs asynchronously. Installing a registration handler is a way to be notified when that set up is complete and the dispatch source is ready to start delivering events.

After your operation handler is executed, the dispatch source uninstalls it. Thus, registration handlers are executed only once after you resume the dispatch source.

If you install a registration handler on a dispatch source that is already set up and running, your handler is invoked immediately.

## Parameters

- `source`: The dispatch source to modify. This parameter cannot be `NULL`.
- `handler`: The registration handler function to install. The previous registration handler (if any) is released before the new one is installed. The context parameter passed to the event handler function is the current context of the dispatch source at the time the handler call is made. This parameter can be `NULL`.

## See Also

### Managing Event Handlers
- [dispatch_source_set_registration_handler](./dispatch_source_set_registration_handler.md)
  Sets the registration handler block for the given dispatch source.
- [dispatch_source_set_event_handler_f](./dispatch_source_set_event_handler_f.md)
  Sets the event handler function for the given dispatch source.
- [dispatch_source_set_event_handler](./dispatch_source_set_event_handler.md)
  Sets the event handler block for the given dispatch source.
- [dispatch_source_set_cancel_handler_f](./dispatch_source_set_cancel_handler_f.md)
  Sets the cancellation handler function for the given dispatch source.
- [dispatch_source_set_cancel_handler](./dispatch_source_set_cancel_handler.md)
  Sets the cancellation handler block for the given dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_set_registration_handler_f)*