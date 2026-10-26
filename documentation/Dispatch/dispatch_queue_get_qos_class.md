# dispatch_queue_get_qos_class

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the quality-of-service class for the specified queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern dispatch_qos_class_t dispatch_queue_get_qos_class(dispatch_queue_t queue, int *relative_priority_ptr);
```

## See Also

### Configuring Queue Execution Parameters
- [typealias dispatch_queue_attr_t](./dispatch_queue_attr_t.md)
  Attributes describing the behaviors of a dispatch queue.
- [dispatch_queue_attr_make_with_qos_class](./dispatch_queue_attr_make_with_qos_class.md)
  Returns attributes suitable for creating a dispatch queue with the desired quality-of-service information.
- [dispatch_qos_class_t](./dispatch_qos_class_t.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_queue_attr_make_initially_inactive](./dispatch_queue_attr_make_initially_inactive.md)
  Returns an attribute that configures a dispatch queue as initially inactive.
- [dispatch_queue_attr_make_with_autorelease_frequency](./dispatch_queue_attr_make_with_autorelease_frequency.md)
  Returns an attribute that specifies how the dispatch queue manages autorelease pools for the blocks it executes.
- [dispatch_autorelease_frequency_t](./dispatch_autorelease_frequency_t.md)
  Constants indicating the frequency with which a dispatch queue creates autorelease pools for its tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_get_qos_class)*