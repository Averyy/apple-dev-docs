# dispatch_source_set_event_handler

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Sets the event handler block for the given dispatch source.

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
extern void dispatch_source_set_event_handler(dispatch_source_t source, dispatch_block_t handler);
```

## Discussion

The event handler (if specified) is submitted to the source’s target queue in response to the arrival of an event.

## Parameters

- `source`: The dispatch source to modify. This parameter cannot be `NULL`.
- `handler`: The event handler block to submit to the source’s target queue. This function performs a `Block_copy` on behalf of the caller, and `Block_release` on the previous handler (if any). This parameter cannot be `NULL`.

## See Also

### Managing Event Handlers
- [dispatch_source_set_registration_handler_f](./dispatch_source_set_registration_handler_f.md)
  Sets the registration handler function for the given dispatch source.
- [dispatch_source_set_registration_handler](./dispatch_source_set_registration_handler.md)
  Sets the registration handler block for the given dispatch source.
- [dispatch_source_set_event_handler_f](./dispatch_source_set_event_handler_f.md)
  Sets the event handler function for the given dispatch source.
- [dispatch_source_set_cancel_handler_f](./dispatch_source_set_cancel_handler_f.md)
  Sets the cancellation handler function for the given dispatch source.
- [dispatch_source_set_cancel_handler](./dispatch_source_set_cancel_handler.md)
  Sets the cancellation handler block for the given dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_set_event_handler)*