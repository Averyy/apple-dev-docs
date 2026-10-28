# dispatch_get_specific

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the value for the key associated with the current dispatch queue.

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
extern void *dispatch_get_specific(const void *key);
```

## Return Value

The context value for the specified key; otherwise `NULL` if the key was not set for the queue (or its target queue) or the queue is a global concurrent queue.

## Discussion

This function is intended to be called from a block executing in a dispatch queue. You use it to obtain context data associated with the queue. Calling this method from code not running in a dispatch queue returns `NULL` because there is no queue to provide context.

## Parameters

- `key`: The key associated with the dispatch queue on which the current block is executing. Keys are only compared as pointers and never dereferenced. Passing a string constant directly is not recommended.

## See Also

### Getting and Setting Contextual Data
- [dispatch_queue_set_specific](./dispatch_queue_set_specific.md)
  Sets the key/value data for the specified dispatch queue.
- [dispatch_queue_get_specific](./dispatch_queue_get_specific.md)
  Gets the value for the key associated with the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_get_specific)*