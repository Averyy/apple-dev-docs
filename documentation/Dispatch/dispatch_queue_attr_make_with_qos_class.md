# dispatch_queue_attr_make_with_qos_class

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns attributes suitable for creating a dispatch queue with the desired quality-of-service information.

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
extern dispatch_queue_attr_tdispatch_queue_attr_make_with_qos_class(dispatch_queue_attr_t attr, dispatch_qos_class_t qos_class, int relative_priority);
```

#### Return Value

An attribute value that may be passed to the [`dispatch_queue_create`](./dispatch_queue_create.md) function when creating a dispatch queue.

#### Discussion

Call this function prior to calling the [`dispatch_queue_create`](./dispatch_queue_create.md) function when you want to create a dispatch queue with a specific quality-of-service level. This function combines the queue type attributes with the quality-of-service information you specify and returns a value that you can pass to the [`dispatch_queue_create`](./dispatch_queue_create.md) function. The quality-of-service value you specify using this function takes precedence over the priority level inherited from the dispatch queue’s target queue.

The global queue priorities map to the following quality-of-service classes:

- [`DISPATCH_QUEUE_PRIORITY_HIGH`](./dispatch_queue_priority_high.md) maps to the `QOS_CLASS_USER_INITIATED` class.
- [`DISPATCH_QUEUE_PRIORITY_DEFAULT`](./dispatch_queue_priority_default.md) maps to the `QOS_CLASS_DEFAULT` class.
- [`DISPATCH_QUEUE_PRIORITY_LOW`](./dispatch_queue_priority_low.md) maps to the `QOS_CLASS_UTILITY` class.
- [`DISPATCH_QUEUE_PRIORITY_BACKGROUND`](./dispatch_queue_priority_background.md) maps to the `QOS_CLASS_BACKGROUND` class.

## Parameters

- `attr`: A queue attribute value to be combined with the quality-of-service class. Specify [`DISPATCH_QUEUE_SERIAL`](./dispatch_queue_serial.md) if you want submitted tasks to be scheduled serially or [`DISPATCH_QUEUE_CONCURRENT`](./dispatch_queue_concurrent.md) if tasks may be scheduled concurrently. If you specify `NULL`, this function creates a serial queue.
- `qos_class`: The quality of service you want to give to tasks executed using this queue. Quality-of-service helps determine the priority given to tasks executed by the queue. Specify one of the values `QOS_CLASS_USER_INTERACTIVE`, `QOS_CLASS_USER_INITIATED`, `QOS_CLASS_UTILITY`, or `QOS_CLASS_BACKGROUND`. Queues that handle user-interactive or user-initiated tasks have a higher priority than tasks meant to run in the background.
- `relative_priority`: A negative offset from the maximum supported scheduler priority for the given quality-of-service class. This value must be less than `0` and greater than or equal to `QOS_MIN_RELATIVE_PRIORITY`, or else this function returns `NULL`.

## See Also

### Configuring Queue Execution Parameters
- [typealias dispatch_queue_attr_t](./dispatch_queue_attr_t.md)
  Attributes describing the behaviors of a dispatch queue.
- [dispatch_queue_get_qos_class](./dispatch_queue_get_qos_class.md)
  Returns the quality-of-service class for the specified queue.
- [dispatch_qos_class_t](./dispatch_qos_class_t.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_queue_attr_make_initially_inactive](./dispatch_queue_attr_make_initially_inactive.md)
  Returns an attribute that configures a dispatch queue as initially inactive.
- [dispatch_queue_attr_make_with_autorelease_frequency](./dispatch_queue_attr_make_with_autorelease_frequency.md)
  Returns an attribute that specifies how the dispatch queue manages autorelease pools for the blocks it executes.
- [dispatch_autorelease_frequency_t](./dispatch_autorelease_frequency_t.md)
  Constants indicating the frequency with which a dispatch queue creates autorelease pools for its tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_attr_make_with_qos_class)*