# dispatch_queue_get_label

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the label you assigned to the dispatch queue at creation time.

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
extern const char *dispatch_queue_get_label(dispatch_queue_t queue);
```

#### Return Value

The label of the queue, or `NULL` if the queue was not provided a label during initialization.

## Parameters

- `queue`: The dispatch queue from which to get the label. Specify [`DISPATCH_CURRENT_QUEUE_LABEL`](./dispatch_current_queue_label.md) to retrieve the label of the current queue.

## See Also

### Managing Queue Attributes
- [DISPATCH_CURRENT_QUEUE_LABEL](./dispatch_current_queue_label.md)
  Pass this constant to the [`dispatch_queue_get_label`](./dispatch_queue_get_label.md) function to retrieve the label of the current queue.
- [func setTarget(queue: dispatch_queue_t?)](./dispatchobject/settarget%28queue%29.md)
  Specifies the dispatch queue on which to perform work associated with the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_get_label)*