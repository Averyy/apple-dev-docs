# dispatch_autorelease_frequency_t

**Framework**: Dispatch  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the frequency with which a dispatch queue creates autorelease pools for its tasks.

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
typedef enum { ... } dispatch_autorelease_frequency_t;
```

## Topics

### Autorelease Frequency Options
- [DISPATCH_AUTORELEASE_FREQUENCY_INHERIT](./dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_inherit.md)
  The queue inherits its autorelease frequency from its target queue.
- [DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM](./dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_work_item.md)
  The queue configures an autorelease pool before the execution of a block and releases the objects in that pool after the block finishes executing.
- [DISPATCH_AUTORELEASE_FREQUENCY_NEVER](./dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_never.md)
  The queue does not set up an autorelease pool around executed blocks.

## See Also

### Configuring Queue Execution Parameters
- [typealias dispatch_queue_attr_t](./dispatch_queue_attr_t.md)
  Attributes describing the behaviors of a dispatch queue.
- [dispatch_queue_attr_make_with_qos_class](./dispatch_queue_attr_make_with_qos_class.md)
  Returns attributes suitable for creating a dispatch queue with the desired quality-of-service information.
- [dispatch_queue_get_qos_class](./dispatch_queue_get_qos_class.md)
  Returns the quality-of-service class for the specified queue.
- [dispatch_qos_class_t](./dispatch_qos_class_t.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_queue_attr_make_initially_inactive](./dispatch_queue_attr_make_initially_inactive.md)
  Returns an attribute that configures a dispatch queue as initially inactive.
- [dispatch_queue_attr_make_with_autorelease_frequency](./dispatch_queue_attr_make_with_autorelease_frequency.md)
  Returns an attribute that specifies how the dispatch queue manages autorelease pools for the blocks it executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_autorelease_frequency_t)*