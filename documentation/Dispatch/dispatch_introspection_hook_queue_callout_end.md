# dispatch_introspection_hook_queue_callout_end

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_introspection_hook_queue_callout_end(dispatch_queue_t queue, void *context, dispatch_function_t function);
```

## See Also

### Introspecting a Dispatch Object
- [dispatch_introspection_hook_queue_create](./dispatch_introspection_hook_queue_create.md)
- [dispatch_introspection_hook_queue_destroy](./dispatch_introspection_hook_queue_destroy.md)
- [dispatch_introspection_hook_queue_item_enqueue](./dispatch_introspection_hook_queue_item_enqueue.md)
- [dispatch_introspection_hook_queue_item_dequeue](./dispatch_introspection_hook_queue_item_dequeue.md)
- [dispatch_introspection_hook_queue_callout_begin](./dispatch_introspection_hook_queue_callout_begin.md)
- [dispatch_introspection_hook_queue_item_complete](./dispatch_introspection_hook_queue_item_complete.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_introspection_hook_queue_callout_end)*