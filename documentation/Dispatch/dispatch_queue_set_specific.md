# dispatch_queue_set_specific

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Sets the key/value data for the specified dispatch queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_queue_set_specific(dispatch_queue_t queue, const void *key, void *context, dispatch_function_t destructor);
```

## Discussion

Use this method to associate custom context data with a dispatch queue. Blocks executing on the queue can use the [`dispatch_get_specific`](./dispatch_get_specific.md) function to retrieve this data while they are running.

## Parameters

- `queue`: The queue on which to set the specified key/value data. This parameter must not be `NULL`.
- `key`: The key you want to use to identify the associated context data. Keys are only compared as pointers and are never dereferenced. Thus, you can use a pointer to a static variable for a specific subsystem or any other value that allows you to identify the value uniquely. Specifying a pointer to a string constant is not recommended. `NULL` is not a valid value for the key and attempts to set context data with a `NULL` key are ignored.
- `context`: The context data to associate with `key`. This parameter may be `NULL`.
- `destructor`: A destructor function that you can use to release your context data. This parameter may be `NULL`. If `context` is `NULL`, your destructor function is ignored.

## See Also

### Getting and Setting Contextual Data
- [dispatch_get_specific](./dispatch_get_specific.md)
  Returns the value for the key associated with the current dispatch queue.
- [dispatch_queue_get_specific](./dispatch_queue_get_specific.md)
  Gets the value for the key associated with the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_set_specific)*