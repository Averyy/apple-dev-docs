# dispatch_queue_get_specific

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Gets the value for the key associated with the specified dispatch queue.

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
extern void *dispatch_queue_get_specific(dispatch_queue_t queue, const void *key);
```

## Return Value

The context data associated with `key` or `NULL` if no context was found.

## Discussion

You can use this method to get the context data associated with a specific dispatch queue. Blocks executing on a queue can use the [`dispatch_get_specific`](./dispatch_get_specific.md) function to retrieve the context associated with that specific queue instead.

## Parameters

- `queue`: The queue containing the desired context data. This parameter must not be `NULL`.
- `key`: The key that identifies the associated context data. Keys are only compared as pointers and are never dereferenced. Thus, you can use a pointer to a static variable for a specific subsystem or any other value that allows you to identify the value uniquely. Specifying a pointer to a string constant is not recommended.

## See Also

### Getting and Setting Contextual Data
- [dispatch_get_specific](./dispatch_get_specific.md)
  Returns the value for the key associated with the current dispatch queue.
- [dispatch_queue_set_specific](./dispatch_queue_set_specific.md)
  Sets the key/value data for the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_get_specific)*