# dispatch_source_cancel

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.

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
extern void dispatch_source_cancel(dispatch_source_t source);
```

#### Discussion

Cancellation prevents any further invocation of the event handler block for the specified dispatch source, but does not interrupt an event handler block that is already in progress. The optional cancellation handler is submitted to the target queue once the event handler block has been completed.

The cancellation handler is submitted to the source’s target queue when the source’s event handler has finished, indicating that it is safe to close the source’s handle (file descriptor or mach port).

The optional cancellation handler is submitted to the dispatch source object’s target queue only after the system has released all of its references to any underlying system objects (file descriptors or mach ports). Thus, the cancellation handler is a convenient place to close or deallocate such system objects. Note that it is invalid to close a file descriptor or deallocate a mach port currently being tracked by a dispatch source object before the cancellation handler is invoked.

## Parameters

- `source`: The dispatch source to be canceled. This parameter cannot be `NULL`.

## See Also

### Related Documentation
- [dispatch_source_set_cancel_handler](./dispatch_source_set_cancel_handler.md)
  Sets the cancellation handler block for the given dispatch source.
### Canceling a Dispatch Source
- [dispatch_source_testcancel](./dispatch_source_testcancel.md)
  Tests whether the given dispatch source has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_cancel)*