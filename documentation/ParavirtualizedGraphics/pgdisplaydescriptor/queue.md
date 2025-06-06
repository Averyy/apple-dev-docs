# queue

**Framework**: Paravirtualized Graphics  
**Kind**: property

The queue that the framework uses when dispatching messages to any of the display’s registered handlers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var queue: dispatch_queue_t? { get set }
```

#### Discussion

Most often, your app provides a serial queue. If you can benefit from dispatching events out of order, handle the messages on the serial queue and redispatch them to other queues as necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor/queue)*