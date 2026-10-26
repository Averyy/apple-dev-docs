# DISPATCH_CURRENT_QUEUE_LABEL

**Framework**: Dispatch  
**Kind**: macro  
**Role**: Macro

Pass this constant to the [`dispatch_queue_get_label`](./dispatch_queue_get_label.md) function to retrieve the label of the current queue.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define DISPATCH_CURRENT_QUEUE_LABEL
```

## See Also

### Managing Queue Attributes
- [dispatch_queue_get_label](./dispatch_queue_get_label.md)
  Returns the label you assigned to the dispatch queue at creation time.
- [func setTarget(queue: dispatch_queue_t?)](./dispatchobject/settarget%28queue%29.md)
  Specifies the dispatch queue on which to perform work associated with the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_current_queue_label)*